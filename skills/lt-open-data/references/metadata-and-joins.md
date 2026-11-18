# Portal Metadata, Schema Divergence, Units, and Cross-Table Joins

## 1. OKF `v0.2` Concept Anatomy and Provenance

- Follow the four-step progressive-disclosure hierarchy inside `bundle/` so column answers always rest on table-level definitions:
  1. `bundle/index.md` (`okf_version: "0.2"`, `# Subdirectories`).
  2. `bundle/<namespace>/index.md` and nested provider `index.md` files (`# Subdirectories`, `# Dataset`, `# Table`).
  3. `bundle/<dataset>.md` (`type: Dataset` -- frontmatter `resource:` when deployed, `# Tables`, and optional `# Enumerations`, `# Prefixes`, `# Comments`).
  4. `bundle/<dataset>/<Model>.md` (`type: Table` -- introductory prose below `# <Title>`, metadata bullets, `# Schema`, and optional `# Enumerations`, `# Translations`, `# Prefixes`, `# Comments`).
- Treat every concept in the bundle as `unverified` because `verified:` is omitted across all concepts (`0` human steward verifications).
- Attribute structural schema claims to the `[^manifest]` source citation (`atviriduomenys/manifest` CSV path and `#L<line>`) and never imply official agency endorsement.

## 2. `data.gov.lt` DCAT-AP Portal Metadata Fallback (`429`-Safe)

- Account for what Spinta manifests omit: `bundle/` captures structural Spinta DSA schemas, so operational portal fields (`dct:accrualPeriodicity`, `dct:license`, `dct:publisher`, `dct:issued`, `dct:modified`, `dcat:distribution`) are absent unless mapped under `# Prefixes` or `URI`.
- Prefer querying a deployed catalog table on `get.data.gov.lt` with one bounded RQL filter (`?limit(5)`) whenever a catalog dataset is identified during bundle discovery.
- Include the trailing slash before `?` whenever calling the `data.gov.lt` public catalog REST endpoint (`https://data.gov.lt/public/api/1/datasets/?limit=5&...`) because omitting `/` before `?` returns `HTTP 301 Moved Permanently` with an empty body.
- Never call `/partner/api/1/` endpoints without user-supplied `ApiKey` credentials, and never download full-catalog RDF dumps (`edp/dcat-ap.rdf`) to inspect one dataset.
- Stop immediately without retrying if `data.gov.lt` returns HTTP `429` or a connection error, and report verified `[^manifest]` schema facts alongside which live portal metadata field remained unverified.

```text
https://data.gov.lt/public/api/1/datasets/?limit=5
```

## 3. Manifest-vs-Live Schema Divergence

- Derive endpoint paths exclusively from frontmatter `resource:` (declared `<dataset>/<Model>`), never from the `Manifest CSV` filename bullet, because upstream CSV filenames frequently differ from declared `dataset` namespaces (including preserved upstream spelling typos in path segments).
- Distinguish `# Schema` from `# Comments`: rows under `# Comments` (`update(type: "<type>", ref: "<unit>")`, `create(...)`) are unapplied steward backlog proposals, whereas live `get.data.gov.lt` serves the declared `# Schema`.
- Run a single `?limit(1)` probe before constructing wide `select()` projections because production `get.data.gov.lt` deployments can lag recent manifest commits (returning HTTP `400` `PropertyNotFound` on newly added fields) or expose columns documented in `Description` as temporarily empty during upstream IT migrations.

## 4. Hidden Scale Multipliers, Lifecycle Notices, and Conflicting `# Comments`

- Read the introductory prose paragraph directly below `# <Title>` alongside `# Schema` `Ref`, `Title`, and `Description` on every `Table` concept because numeric columns (`integer`, `number`) often show a blank marker cell in `Ref` while prose states scale multipliers (`10^3`, `10^6`), rate denominators, or archival/discontinuation notices.
- Prioritize explicit scale multipliers in introductory prose or column `Description` over boilerplate `# Comments` entries (such as `update(type: "money", ref: "<currency>")`) because unapplied backlog comments routinely omit the `10^3` or `10^6` multiplier active in published values.
- Inspect date spans on multi-year series for historical currency transitions and statutory classification revision breaks before summing or comparing values across years because pre-transition and post-transition records can share one column without automatic rescaling.

## 5. Cross-Table Joins, Homonym Hazards, Access Tiers, and Count Traps

- Join tables strictly according to `# Schema` `Level` and `Ref` on the referencing column:
  - `level >= 4`: join `<Model>.<fk>._id` to `<TargetModel>._id` (UUID match) even when `# Schema` `Ref` writes `<TargetModel>[<pk>]`.
  - `level = 3`: join `<Model>.<fk>.<pk>` to `<TargetModel>.<pk>` (natural-key match).
  - `level <= 2`: treat values as unlinked scalars with zero server-enforced referential integrity, and inspect a live sample (`?select(<field>)&limit(10)`) on both tables to verify leading zeros, formatting, code-vs-label usage, and null rates before joining client-side.
- Never join two tables solely because they share a generic `<Model>` or `<field>` name because unrelated providers reuse generic names for incompatible identifiers, dates, region codes, and geometry systems (national metric grid `EPSG:3346` vs `EPSG:4326` degrees) unless `# Schema` `Ref` or `URI` binds both columns to the same canonical target.
- Verify Spinta `Access` on every target table and column before promising anonymous access because only `open` and `open (inherited)` are unrestricted open data, whereas `public` requires GDPR-authorized recipients, `protected` and `private` are restricted, and a blank marker cell means `access` was left unset in the manifest.
- Never report `len(_data)` from a `?limit(<N>)` sample or a `100`-row HTML page as total dataset rows, and never compute shares or rankings over page 1 when `"_page": {"next": "..."}` exists; run `?count()` (or `?<filter>&count()`) first.
