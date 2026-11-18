---
name: lt-open-data
description: >-
  Explores and queries Lithuanian Open Data schemas and APIs across the
  data.gov.lt DCAT-AP catalog, get.data.gov.lt Spinta DSA REST/RQL endpoints,
  and the atviriduomenys/manifest OKF v0.2 knowledge bundle. Use when searching
  Lithuanian open data ("Lietuvos atviri duomenys", "atvirų duomenų rinkiniai",
  "atviru duomenu schemos", "lentelių schemos", "atviru duomenu uzklausos"),
  resolving local or remote OKF bundle caches across OS shells, constructing
  Spinta RQL filters, format suffixes, or cursor pagination, or validating
  foreign-key joins, access tiers, units, and portal metadata. Don't use for
  api.dataportal.gov.lt analytical lakehouse APIs, non-Spinta open-data
  portals, or general SQL query authoring.
license: AGPL-3.0
compatibility: >-
  Works across POSIX sh/bash/zsh, Windows PowerShell/CMD, minimal LC_ALL=C
  containers, and restricted no-shell sandboxes. Uses optional git
  (sparse-checkout cache), ripgrep/grep, and HTTPS access to github.com,
  get.data.gov.lt, and data.gov.lt.
metadata:
  author: kestutisd
  version: "0.3.0"
---

# Lithuanian Open Data (`OKF v0.2` and Spinta DSA)

## Scope and Trust Boundaries

- Cover strictly `data.gov.lt` portal metadata (DCAT-AP), `get.data.gov.lt` Spinta DSA REST/RQL APIs, and the `atviriduomenys/manifest` OKF `v0.2` bundle distributed in `https://github.com/kestutisd/lt-open-data-okf`.
- Exclude `api.dataportal.gov.lt` analytical lakehouse APIs and non-Spinta portals because they use incompatible namespace identifiers, integer keys, flattened schemas, and query engines.
- Treat every bundle concept as `unverified` because frontmatter omits `verified:` (`0` human steward verifications).
- Attribute structural schema claims to the `[^manifest]` source entry (`atviriduomenys/manifest` CSV path and `#L<line>`) and never claim official agency endorsement.

## Reference Routing

- Read [references/cross-os-bundle.md](references/cross-os-bundle.md) when resolving `BUNDLE_DIR`, bootstrapping or refreshing the sparse Git cache without `viz.html`, running UTF-8 Lithuanian stem searches across POSIX, PowerShell, CMD, or `LC_ALL=C` containers, or using raw HTTPS in restricted sandboxes.
- Read [references/spinta-rql.md](references/spinta-rql.md) when building `get.data.gov.lt` RQL filters, `select()` projections, `/:format/<fmt>` routes, cursor pagination (`page()`), exact counts (`count()`), or handling HTTP `400`, `401`, `403`, `404`, and `429` responses.
- Read [references/metadata-and-joins.md](references/metadata-and-joins.md) when fetching `data.gov.lt` DCAT-AP metadata, reconciling manifest-vs-live drift, resolving foreign-key (`ref`) serialization by maturity `level`, checking prose scale units vs `# Comments`, or joining tables.

## Execution Workflow

### 1. Resolve the OKF Bundle (`BUNDLE_DIR`)

- Prefer built-in harness Read, Glob, and Grep tools over shell commands because native tools avoid shell quoting bugs, locale encoding mismatches, and subprocess overhead.
- Check `./bundle/index.md` first (workspace clone), then `${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle/index.md` on POSIX, `$HOME/.cache/lt-open-data-okf/bundle/index.md` in PowerShell, or `%USERPROFILE%\.cache\lt-open-data-okf\bundle\index.md` in CMD.
- Bootstrap a missing user cache with shallow sparse-checkout (`--depth 1 --filter=blob:none --sparse` with `'bundle/**'` and `'!bundle/viz.html'`) so Git skips the multi-megabyte graph viewer (see [references/cross-os-bundle.md](references/cross-os-bundle.md)).
- Traverse `https://raw.githubusercontent.com/kestutisd/lt-open-data-okf/main/bundle/<path>` directly over HTTPS only when local files and `git` are unavailable.

### 2. Search Schemas with Paired Stems and Exclusions

- Pair inflected Lithuanian stems with unaccented ASCII stems (`<lt_stem>|<ascii_stem>`) because titles and descriptions inflect across grammatical cases while paths, `<Model>` names, and `<field>` identifiers use ASCII `snake_case` or `PascalCase`.
- Exclude `viz.html`, `index.md` (`':!index.md'` and `':!**/index.md'`), and `log.md` on every content search so single-line graph JSON, navigation indexes, and changelog entries never flood or dilute schema matches.

```sh
if [ -f "./bundle/index.md" ]; then
  BUNDLE_DIR="./bundle"
else
  BUNDLE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle"
fi
PATTERN="${PATTERN:-type: Table}"
if command -v rg >/dev/null 2>&1; then
  rg -ni -g '*.md' -g '!index.md' -g '!log.md' -- "$PATTERN" "$BUNDLE_DIR"
elif git -C "$BUNDLE_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$BUNDLE_DIR" grep -niE -- "$PATTERN" . ':!viz.html' ':!index.md' ':!**/index.md' ':!log.md'
else
  find "$BUNDLE_DIR" -type f -name '*.md' ! -name 'index.md' ! -name 'log.md' -exec grep -niHE -- "$PATTERN" {} +
fi
```

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$CacheRepo = if ($env:XDG_CACHE_HOME) { "$env:XDG_CACHE_HOME/lt-open-data-okf" } else { "$HOME/.cache/lt-open-data-okf" }
$BundleDir = if (Test-Path "./bundle/index.md") { "./bundle" } else { "$CacheRepo/bundle" }
$Pattern = if ($Pattern) { $Pattern } else { "type: Table" }
if (Get-Command git -ErrorAction SilentlyContinue) {
    git -C "$BundleDir" grep -niE -- "$Pattern" . ':!viz.html' ':!index.md' ':!**/index.md' ':!log.md'
} else {
    Get-ChildItem -LiteralPath $BundleDir -Recurse -Filter "*.md" -File |
        Where-Object { $_.Name -notin 'index.md', 'log.md' } |
        Select-String -Pattern $Pattern -Encoding UTF8
}
```

### 3. Follow Progressive Disclosure to `<Model>.md`

1. Open `bundle/index.md` (`okf_version: "0.2"`, `# Subdirectories`) and drill into `bundle/<namespace>/index.md` when browsing provider hierarchies.
2. Open `bundle/<dataset>.md` (`type: Dataset`) to check frontmatter `resource:` deployment and the `# Tables` inventory.
3. Always open `bundle/<dataset>/<Model>.md` (`type: Table`) before answering any column, unit, key, or API question because dataset files omit property schemas.
4. Read introductory prose below `# <Title>`, metadata bullets, `# Schema` (`Property | Type | Ref | Level | Access | URI | Title | Description`), and optional `# Enumerations`, `# Translations`, `# Prefixes`, and `# Comments`.

### 4. Validate Deployment, Access, and Query Bounds

1. Confirm frontmatter `resource:` (`https://get.data.gov.lt/<dataset>/<Model>`) exists before calling the API because concepts tagged `undeployed` omit `resource:` and return HTTP `404`.
2. Confirm `# Schema` `Access` is `open` or `open (inherited)` because `public` requires GDPR-authorized recipients and `protected` or `private` endpoints return HTTP `401` or `403`.
3. Append `/:format/json` (or `/:format/jsonl`, `/:format/csv`) with an explicit `?limit(<N>)` because programmatic formats omit the `100`-row HTML cap and stream up to `100000` rows per batch by default.
4. Run `/:format/json?count()` (or `?<filter>&count()`) whenever reporting row totals because sample slices and page-1 payloads truncate underlying table sizes.

## Mandatory Guardrails

- Build endpoint URLs exclusively from frontmatter `resource:` (declared `<dataset>/<Model>`), never from the manifest CSV filename, because upstream CSV paths frequently diverge from declared namespaces.
- Query `level >= 4` `ref` columns via `<fk>._id` (`{"_id": "<uuid>"}`) because Spinta serializes UUID references at `level >= 4` even when `# Schema` `Ref` displays `<TargetModel>[<pk>]`.
- Query `level = 3` `ref` columns via `<fk>.<pk>` (`{"<pk>": "<val>"}`) because `level = 3` exposes natural keys without `_id`.
- Treat `level <= 2` columns as plain `<field>` scalars with zero referential integrity, and inspect live samples on both tables before joining client-side.
- Never join tables on matching generic `<Model>` or `<field>` names unless `# Schema` `Ref` or `URI` binds both sides to the same canonical target, because unrelated providers reuse generic names with incompatible code spaces and coordinate systems (`EPSG:3346` vs `EPSG:4326`).
- Never send SQL aggregates (`sum()`, `avg()`, `min()`, `max()`) to `get.data.gov.lt` because Spinta implements only `count()` server-side and rejects other aggregates with HTTP `400` `UnknownMethod`.
- Check `?count()` before computing client-side totals or averages over `select(...)`, and aggregate client-side only when total row volume is small; otherwise state that server-side aggregation is unsupported.
- Never send SQL clauses (`GROUP BY`, `HAVING`, `JOIN`, `OFFSET`, `WHERE`) because Spinta evaluates single-model RQL expressions and rejects SQL syntax with HTTP `400` `InvalidSyntax`.
- Never send unprefixed REST pagination keys (`?page=1`, `?offset=20`, `?per_page=50`) because Spinta parses unprefixed keys as column filters and returns HTTP `400` `PropertyNotFound`.
- Paginate exclusively via cursor tokens from `"_page": {"next": "<token>"}` using `?limit(<N>)&page("<token>")` because Spinta supports no numeric row offsets.
- Keep URLs below `2000` bytes and pass `-g -m 15` to `curl` / `curl.exe` (never bare `curl` in PowerShell 5.1, which aliases `Invoke-WebRequest`) to avoid HTTP `414` proxy rejections and shell glob expansion.
- Prioritize scale multipliers (`10^3`, `10^6`) and archival notices in introductory prose below `# <Title>` over blank `# Schema` `Ref` cells and unapplied `# Comments` `update(...)` backlog notes.
- Inspect multi-year date spans for historical currency transitions and statutory classification revision breaks before comparing or summing values across years.
- Query a deployed catalog table on `get.data.gov.lt` (`?limit(5)`) first when operational DCAT-AP metadata (`dct:accrualPeriodicity`, `dct:license`, `dct:publisher`, `dct:modified`) is absent from `# Prefixes` or `URI`.
- Include the trailing slash before `?` on `https://data.gov.lt/public/api/1/datasets/?limit=5` because omitting `/` before `?` returns `HTTP 301` with an empty body.
- Send single sequential requests and stop immediately without automatic retries on HTTP `401`, `403`, `429`, or `5xx` to respect portal rate limits and authorization boundaries.
- Degrade gracefully to verified `[^manifest]` schema definitions when sandboxes block network access or live endpoints throttle requests, stating explicitly which live runtime field remained unverified.

## Pre-Answer Verification Checklist

- [ ] Opened `bundle/<dataset>/<Model>.md` (`type: Table`) and inspected introductory prose, `# Schema`, and `# Comments`.
- [ ] Verified frontmatter `resource:` exists (`deployed`) and `# Schema` `Access` is `open` or `open (inherited)` before proposing anonymous API calls.
- [ ] Matched foreign-key projections, filters, and joins to `# Schema` `Level` (`>= 4` `_id`, `3` `<pk>`, `<= 2` unverified scalar).
- [ ] Included `/:format/<fmt>` and explicit `?limit(<N>)` on exploratory `get.data.gov.lt` URLs, and used `?count()` for exact totals.
- [ ] Checked introductory prose and multi-year spans for scale multipliers, archival notices, currency transitions, and classification breaks.
- [ ] Attributed schema claims to `[^manifest]` (`unverified` bundle tier) without claiming agency verification.
