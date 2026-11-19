---
name: lt-open-data
description: >-
  Explores and queries Lithuanian Open Data schemas, EU/ISO standards, and
  Spinta APIs across the data.gov.lt DCAT-AP catalog, get.data.gov.lt REST/RQL
  endpoints, and the Lithuanian Open Data OKF v0.3 knowledge bundle, reporting
  provenance, trust tier, freshness, and attestation status for every concept
  used. Use when searching Lithuanian open data ("Lietuvos atviri duomenys",
  "atvirų duomenų rinkiniai", "atviru duomenu schemos", "lentelių schemos",
  "atviru duomenu uzklausos"), resolving local or remote OKF bundle caches
  across OS shells, constructing Spinta RQL filters, format suffixes, or cursor
  pagination, validating foreign-key joins, access tiers, units, and portal
  metadata, or executing statutory LTL/EUR, EVRK/NACE, CPV/BVPŽ, and ISO 639
  rules. Don't use for api.dataportal.gov.lt analytical lakehouse SQL/Iceberg
  APIs, non-Spinta open-data portals, or general SQL query authoring.
license: AGPL-3.0-only
compatibility: >-
  Works across POSIX sh/bash/zsh, Windows PowerShell 5.1/7+ and CMD, minimal
  LC_ALL=C containers, and restricted no-shell sandboxes. Includes Python 3.9+
  scanner (PyYAML optional with zero-dependency stdlib fallback) and optional
  git, ripgrep/grep, curl, and HTTPS access to github.com, get.data.gov.lt, and
  data.gov.lt.
metadata:
  author: kestutisd
  publisher: kestutisd
  version: "0.3.0"
  okf_version: "0.3"
---

# Lithuanian Open Data (`OKF v0.3` and Spinta DSA)

This skill only reads an OKF bundle and queries read-only Spinta endpoints. If the task is to create, refresh, edit, migrate, record a verification on, or validate an OKF bundle, stop and use the `lt-open-data-steward` skill instead.

## Scope and OKF v0.3 Trust Boundaries

- Cover strictly `data.gov.lt` portal metadata (DCAT-AP), `get.data.gov.lt` Spinta DSA REST/RQL APIs, and the Lithuanian Open Data OKF `v0.3` bundle (`okf_version: "0.3"`, `3,420` concepts) distributed in `https://github.com/kestutisd/lt-open-data-okf` per [`SPEC.md`](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md).
- Exclude `api.dataportal.gov.lt` analytical lakehouse Iceberg APIs and non-Spinta portals because they use incompatible 9-digit publisher JAR namespaces, 20-digit integer `_id` keys, flattened foreign keys, and SQL engines.
- Treat shipped concepts as `unverified` by default (`0` `verified` entries; never claim agency endorsement). Derive trust strictly from current `verified` events (`at >= generated.at`), never reject concepts for low trust, unknown keys/types, or broken links (OKF §11.2), and attribute claims to `sources` entries (`[^manifest]`, `[^dcat]`, `[^std-*]`), labeling any general knowledge explicitly.
- Never modify the bundle, and never write your own formula or query when an `Attested Computation` defines the value.

## Reference Routing

- Read [references/cross-os-bundle.md](references/cross-os-bundle.md) when resolving `BUNDLE_DIR`, bootstrapping the sparse Git cache without `viz.html`, running [scripts/scan.py](scripts/scan.py) or paired-stem UTF-8 searches across POSIX, PowerShell, CMD, or `LC_ALL=C` containers, or falling back to raw HTTPS.
- Read [references/spinta-rql.md](references/spinta-rql.md) when building `get.data.gov.lt` RQL/UAPI filters, `select()` projections, `/:format/<fmt>` suffixes, cursor pagination (`page()`), exact counts (`count()`), or handling HTTP `400`, `401`, `403`, `404`, `414`, and `429` responses.
- Read [references/metadata-and-joins.md](references/metadata-and-joins.md) when inspecting `# Portal Metadata (DCAT-AP)`, `data.gov.lt` live fallbacks, manifest-vs-live drift, prose scale multipliers vs `# Comments`, statutory `bundle/references/*` breaks, or foreign-key joins.
- Read [references/okf-trust-and-attestation.md](references/okf-trust-and-attestation.md) for exact OKF `v0.3` trust tier, `status` / `superseded_by`, `stale_after` freshness, conflict resolution, `/`-rooted path rules, `<= 0.2` fallbacks, and the 6-case `Attested Computation` gate.

## Execution Workflow

### 1. Resolve `BUNDLE_DIR` and Read Root `index.md`

- Prefer built-in harness Read, Glob, and Grep tools over shell subprocesses to avoid quoting bugs and locale encoding mismatches.
- Check `./bundle/index.md` first, then `${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle/index.md` (POSIX), `$HOME/.cache/lt-open-data-okf/bundle/index.md` (PowerShell), or `%USERPROFILE%\.cache\lt-open-data-okf\bundle\index.md` (CMD).
- Bootstrap a missing cache with shallow sparse-checkout (`--depth 1 --filter=blob:none --sparse` and `--no-cone 'bundle/**' '!bundle/viz.html'`), or traverse `https://raw.githubusercontent.com/kestutisd/lt-open-data-okf/main/bundle/<path>` when `git` and local files are unavailable ([references/cross-os-bundle.md](references/cross-os-bundle.md)).
- Read `bundle/index.md` (`okf_version`, `title`, `description`, `license`, `# Subdirectories`: `computations/`, `datasasets/`, `datasets/`, `references/`). Apply OKF §12.1 fallbacks when `okf_version` is `<= 0.2` or absent.

### 2. Discover Concepts (`scan.py` or Paired-Stem Search)

- Run [scripts/scan.py](scripts/scan.py) for fast, diacritic- and Lithuanian-stem-aware discovery (works with `PyYAML` or zero-dependency stdlib):

```bash
python3 <skill_dir>/scripts/scan.py "$BUNDLE_DIR" --grep "mokesčių" --deployed
```

- Filter with `--type`, `--tag`, `--grep`, `--deployed`, `--undeployed`, `--current`, `--stale`, `--deprecated`, `--unverified`, `--limit N`, or `--json`.
- When using native Grep or shell fallbacks ([references/cross-os-bundle.md](references/cross-os-bundle.md)), pair inflected Lithuanian stems with ASCII stems (`<lt_stem>|<ascii_stem>`) and **always** exclude `viz.html`, `index.md` (`':!index.md'`, `':!**/index.md'`), and `log.md`. Search broadly enough to detect conflicting concepts on the same topic.

### 3. Follow Progressive Disclosure to `<Model>.md` and `references/`

1. Browse `bundle/index.md` -> `bundle/<namespace>/index.md` -> `bundle/<dataset>.md` (`type: Dataset`: check frontmatter `resource:`, `deployed`/`undeployed` tag, `# Portal Metadata (DCAT-AP)`, and `# Tables`).
2. **Always** open `bundle/<dataset>/<Model>.md` (`type: Table`) before answering any column, unit, key, join, or API question; read introductory prose below `# <Title>`, metadata bullets, `# Schema` (`Property | Type | Ref | Level | Access | URI | Title | Description`), and optional `# Enumerations`, `# Translations (@en)`, `# Prefixes`, `# Comments`, and `# Related References`.
3. Follow relevant links to `bundle/references/*.md` (`spinta-dsa-guide.md`, `iso-639-kalbu-kodai.md`, `cpv-bvpz-kodai.md`, `evrk-nace-sekcijos.md`, `lt-valiutos-istorija.md`, `joins/*.md`) and `bundle/computations/*.md`. Resolve `/`-rooted paths from `BUNDLE_DIR` and relative paths from the containing file's directory; never read local paths resolving outside `BUNDLE_DIR`.

### 4. Judge OKF v0.3 Trust, Lifecycle, Freshness, and Conflicts

1. **Trust tier:** Consider only current `verified` events (`at >= generated.at`, or `generated` absent): none -> `unverified`; non-`human:` actors only (`team:`, `process:`, `<producer>/<ver>`) -> `machine-confirmed`; any `human:` actor -> `human-reviewed`. If all events predate `generated.at`, state that the concept was verified only before its last change.
2. **Status:** Missing = `stable`; `draft` = note draft status; `deprecated` = never present as current, follow `superseded_by` (or body links) and state the replacement; any other value = not current, report raw value.
3. **Freshness:** Stale when `now >= stale_after` (date-only = `00:00:00Z`; unparseable = stale + report malformed). Stale means "check again", not "false".
4. **Conflicts:** Prefer (1) current (`stable`/`draft`), (2) higher trust tier (`human-reviewed` > `machine-confirmed` > `unverified`), (3) not stale, (4) later `generated.at`. Report conflicts and weigh `sources` facts (`author`, `usage_count`/`usage_window` by order of magnitude, `last_modified`).

### 5. Execute Attested Computations and Spinta RQL Queries

- **Attested Computations** (e.g., `computations/ltl-to-eur-conversion.md`): Bind declared `parameters` (`ltl_amount`) only, run `executor.resource` (`/references/executors/ltl_to_eur.py`) verbatim to collect `executor.receipt`, and run `attester.resource` (`/references/attesters/ltl_to_eur_attester.py`) on `(receipt, value)`. Enforce the 6-case gate ([references/okf-trust-and-attestation.md](references/okf-trust-and-attestation.md#attestation-gate)): never show a value if attestation fails; if execution cannot run, show the parameter-bound computation marked `not attested`.
- **Spinta RQL Guardrails** ([references/spinta-rql.md](references/spinta-rql.md)):
  - Require frontmatter `resource:` (`deployed`) and `# Schema` `Access` `open` or `open (inherited)` (`public` = GDPR-restricted, `protected`/`private` = `401`/`403`, `undeployed` = `404`).
  - Build URLs strictly from `resource:` (never from divergent CSV filenames), append `/:format/json` (or `jsonl`/`csv`) with `?limit(<N>)` (`100000` default batch without it), and run `?count()` for exact row totals.
  - Match foreign keys to `# Schema` `Level`: `level >= 4` uses `<fk>._id` (`{"_id": "<uuid>"}` even when `Ref` writes `<TargetModel>[<pk>]`); `level = 3` uses `<fk>.<pk>`; `level <= 2` is an unlinked scalar requiring sample inspection before client-side joins. Never join solely on homonymous names (`EPSG:3346` vs `EPSG:4326`).
  - Never send SQL aggregates (`sum()`, `avg()`, `min()`, `max()` -> `400 UnknownMethod`), SQL clauses (`GROUP BY`, `HAVING`, `JOIN`, `OFFSET`, `WHERE` -> `400 InvalidSyntax`), or unprefixed pagination keys (`?page=1`, `?offset=20`, `?per_page=50` -> `400 PropertyNotFound`); paginate strictly via `?limit(<N>)&page("<token>")`.
  - Keep URLs `< 2000` bytes, pass `-g -m 15` to `curl` / `curl.exe` (never bare `curl` in PowerShell 5.1), include the trailing `/` before `?` on `https://data.gov.lt/public/api/1/datasets/?limit=5` (avoiding empty-body `301`), and stop immediately without retries on `401`, `403`, `429`, or `5xx`.
  - Prioritize scale multipliers (`10^3`, `10^6`, `tūkst. EUR`) and archival notices in introductory prose over blank `# Schema` `Ref` cells and unapplied `# Comments` `update(...)` proposals; check multi-year spans for `2015-01-01` `LTL`->`EUR` (`1 EUR = 3.45280 LTL`) and `2025-01-01` EVRK 2.1 (`J`->`J`+`K`, Division `45` dissolution) breaks.

### 6. Format the Answer (Mandatory OKF v0.3 Footer)

Give the answer first, then append these exact items using exact OKF terms (never paraphrases):

- **Concepts used:** each concept ID with its trust tier (`unverified`, `machine-confirmed`, or `human-reviewed`), its `status`, and its freshness (plus `attested` or `not attested` and a receipt reference when an `Attested Computation` was used).
- **Citations:** for each supporting footnote `[^id]`, the `title` and `resource` of the matching `sources` entry.
- **Gaps:** parts of the question not covered by the bundle, or live runtime fields left unverified when offline or rate-limited.
