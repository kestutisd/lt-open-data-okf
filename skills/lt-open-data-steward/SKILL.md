---
name: lt-open-data-steward
description: >-
  Creates, refreshes, migrates, enriches, deprecates, records verified sign-offs
  on, or validates Lithuanian Open Data Open Knowledge Format (OKF v0.3) bundles
  and Attested Computation contracts. Use when generating or updating bundle
  concepts from atviriduomenys/manifest (get_data_gov_lt.in and
  inputs.lock.json), data.gov.lt DCAT-AP metadata, or EU/ISO statutory sources;
  recording human, team, or process verification events; retiring or renaming
  Spinta models with deprecated status and superseded_by; migrating OKF
  v0.1/v0.2 bundles to v0.3; or running validate.py conformance and Spinta/PII
  checks. Use this skill, not lt-open-data, to repair a bundle or to record a
  verification.
license: AGPL-3.0-only
compatibility: >-
  Requires Python 3.9+ with PyYAML (pip install pyyaml) for validate.py. Works
  across POSIX and Windows with strict UTF-8 (no BOM) and LF line endings; uses
  optional git and HTTPS access when refreshing upstream inputs.
metadata:
  author: kestutisd
  publisher: kestutisd
  version: "0.3.0"
  okf_version: "0.3"
---

# Steward and Validate Lithuanian Open Data (`OKF v0.3`) Bundles

To answer questions from an existing bundle or query live `get.data.gov.lt` Spinta RQL endpoints without changing the bundle, stop and use the `lt-open-data` skill instead.

This skill produces, maintains, verifies, migrates, and validates OKF `v0.3` bundles conforming to [`SPEC.md`](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md) and Lithuanian Open Data Spinta DSA invariants.

## Mandatory Producer and Steward Rules

1. **Write only source-backed facts.** Never invent columns, types, maturity `level`s, `access` tiers, `resource:` URLs, DCAT-AP metadata, owners, or `stale_after` dates. Cite every specific claim with a `[^id]` footnote matching `sources[].id` (`[^manifest]`, `[^dcat]`, `[^std-*]`), keeping a strict 1:1 bijection between inline citations, footnote definitions, and `sources[].id`.
2. **Record `generated` authorship honestly.** Set `generated.by` to your agent actor `"<tool>/<model>"` (e.g., `"claude-code/<model>"`, `"codex/<model>"`, `"antigravity/<model>"`) on agent-authored edits, or `"lt-open-data-okf/0.3.0"` on deterministic pipeline runs. Update `generated.at` (UTC RFC 3339 date-time) **only** when content meaning changes — never bump `generated.at` for formatting, whitespace, or link-only fixes because bumping `generated.at` invalidates prior `verified` events (OKF §5.3).
3. **Never fabricate `verified` events.** Never add `verified` to content generated in the same unreviewed run. Add a `human:<id>` entry **only** when that person explicitly confirmed the current content, asked you to record it, and stated their `<id>`. Never infer `<id>` from OS login names, environment variables, or `git config`; if no explicit `<id>` was given, record no verification and explain why.
4. **Never write `Attested Computation` logic yourself.** Copy the computation verbatim from a sanctioned statutory law (such as Council Reg. (EU) No 851/2014 `1 EUR = 3.45280 LTL`) or approved agency repository, and cite that source. Store unapproved queries only if explicitly requested, as `type: Reference` with `status: draft`, never linked as a computation.
5. **Scrub PII and upstream noise.** Remove personal email addresses (`firstname.lastname@...`, consumer domains), phone numbers (`+370...`, `(8 5)...`, `8 6...`), personal manager lines, and `comment.source` personal names from upstream Spinta descriptions and comments while preserving institutional role contacts (`info@...`, `atverimas@...`, `duomenys@...`).
6. **Preserve unowned fields and write UTF-8 LF.** Retain unknown `x-*` extension keys, historical `verified` entries, and human-authored prose when updating files. Write every file as UTF-8 (no BOM) with LF (`\n`) line endings.

## Reference Routing

- Read [references/frontmatter-and-provenance.md](references/frontmatter-and-provenance.md) for all OKF `v0.3` frontmatter fields, YAML 1.2 Core Schema quoting rules, actor/timestamp/path formats, and copy-ready `Dataset`, `Table`, `Reference`, `Attested Computation`, and `deprecated` templates.
- Read [references/steward-workflows.md](references/steward-workflows.md) for detailed runbooks covering `inputs.lock.json` upstream refresh, steward sign-off, model retirement/renaming, executor/attester authoring, `v0.1`/`v0.2` -> `v0.3` migration, and validator codes.

## Steward Workflows

### 1. Refresh from `atviriduomenys/manifest` and `dcat-ap.rdf`

1. Verify upstream inputs against `inputs.lock.json` (`manifest.commit_sha`, `manifest.deployment_list_sha256` for `get_data_gov_lt.in`, `dcat_ap_rdf.sha256`, and `standards_inputs`).
2. Emit concept paths from declared Spinta `dataset` and `model` identifiers (`bundle/<dataset>.md` and `bundle/<dataset>/<Model>.md`), preserving upstream `[sic]` namespaces such as `datasasets/` rather than CSV filenames (`151` CSV paths diverge).
3. Emit `resource: "https://get.data.gov.lt/<path>"` and tag `deployed` **only** when the source CSV appears in `get_data_gov_lt.in`; otherwise omit `resource` and tag `undeployed`.
4. Set `status: draft` for tables with `model.level == "0"` or `/provisional/`; omit `status` for normal `stable` concepts, and keep archival notices in prose rather than auto-deprecating historical tables.
5. Record `manifest` (`author: "team:vssa"`) and matched `dcat` (`author: "team:vda"`) in `sources`, scrub PII, update changed `index.md` files (root `index.md` carries `okf_version: "0.3"`, `title`, one-sentence `description`, `license: "AGPL-3.0-only"`; nested `index.md` and `log.md` carry **no** frontmatter), and prepend a `## YYYY-MM-DD` entry to `bundle/log.md`.

### 2. Record Steward Verifications (`verified`)

1. Confirm the verifier's explicit actor string (`"human:<id>"`, `"team:<id>"`, or `"process:<id>"`) and exact UTC RFC 3339 date-time (`"YYYY-MM-DDTHH:MM:SSZ"` >= `generated.at`).
2. Append `{ by: "<actor>", at: "<UTC-datetime>" }` to `verified` (converting a single mapping to a YAML list if needed), keeping all prior `verified` history intact and leaving `generated` untouched.

### 3. Deprecate or Rename Spinta Models

1. **Retire in place:** Keep the concept file and its `verified` history, set `status: deprecated`, set `superseded_by: "/datasets/..."` (always `/`-rooted in OKF `v0.3`) when a replacement exists, and state the reason and replacement link in the body.
2. **Move or rename without meaning change:** Copy the concept to the new path **preserving its existing `generated` and `verified` values**, and leave a short `status: deprecated` stub at the old path with `superseded_by: "/<new-path>.md"`.

### 4. Author Statutory or Agency `Attested Computation`s

1. Create `bundle/computations/<slug>.md` with `type: Attested Computation` and required `runtime` (e.g., `python`, `bigquery`).
2. Declare `parameters` (`[{ name, type, required }]`), place the verbatim sanctioned code in **one** fenced block under `# Computation` (or set `/`-rooted `computation`, never both), set `executor: { resource: "/references/executors/<name>.py", receipt: [...] }`, and set deterministic LLM-free `attester: { resource: "/references/attesters/<name>.py" }` returning `{ ok: bool, reason?: str }`.
3. Link to the computation from related `Table` or `Reference` concepts under `# Related References`.

### 5. Migrate Older (`v0.1` / `v0.2`) Bundles to OKF `v0.3`

Follow [references/steward-workflows.md](references/steward-workflows.md#5-migrate-okf-v01--v02-bundles-to-v03): add `okf_version: "0.3"`, `title`, `description`, `license` to root `index.md`; prefix bundle-root frontmatter path fields with `/`; strip frontmatter from `log.md` and nested `index.md`; convert scalar `tags` to YAML lists; add `superseded_by` to deprecated concepts; ensure UTC offsets on timestamps; and convert `v0.1` `timestamp` / `# Citations` to `generated` / `sources` + footnotes.

### 6. Validate and Report (`scripts/validate.py`)

Run [scripts/validate.py](scripts/validate.py) with both strict OKF `v0.3` and Spinta/PII/bijection checks:

```bash
python3 <skill_dir>/scripts/validate.py <bundle-root> --strict --spinta-checks
```

1. Fix all conformance errors (`E002`–`E007`), OKF warnings (`W101`–`W126`), and Spinta warnings (`W130` `deployed`/`resource:` mismatch, `W131` personal email/phone PII leak, `W132` footnote/`sources` bijection mismatch).
2. Inspect info findings (`I201` stale concepts, `I203` non-`x-` extension keys, `I204` verifications invalidated by newer `generated.at`, `I205` missing attester).
3. Report created/updated files, `draft`/`deprecated` concepts, concepts needing re-verification (`I204`), unsourced gaps, and validator output.
