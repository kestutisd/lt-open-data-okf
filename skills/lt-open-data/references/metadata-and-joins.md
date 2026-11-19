# Portal Metadata, Schema Divergence, Statutory References, Units, and Cross-Table Joins

## 1. OKF `v0.3` Concept Anatomy and Provenance (`3,420` Concepts)

- Traverse the five-layer OKF `v0.3` bundle hierarchy inside `bundle/` so column, unit, and join answers always rest on table-level definitions and statutory references:
  1. `bundle/index.md` (`okf_version: "0.3"`, `title`, `description`, `license: "AGPL-3.0-only"`, `# Subdirectories`: `computations/`, `datasasets/`, `datasets/`, `references/`).
  2. `bundle/<namespace>/index.md` and nested provider `index.md` files (navigation indexes without frontmatter).
  3. `bundle/datasets/.../<dataset>.md` and `bundle/datasasets/...` (`1,104` `type: Dataset`): frontmatter `resource: "https://get.data.gov.lt/<dataset>"` + `deployed` tag when listed in `get_data_gov_lt.in` (omitted + `undeployed` tag otherwise), `sources` (`manifest` with `author: "team:vssa"`, plus `dcat` with `author: "team:vda"` when matched to `data.gov.lt`), `# Portal Metadata (DCAT-AP)` (`dct:accrualPeriodicity`, `dct:modified`, `dct:issued`, `dct:license`, `dct:publisher`, portal `@lt`/`@en` descriptions), `# Tables`, and optional `# Enumerations`, `# Prefixes`, `# Comments`.
  4. `bundle/datasets/.../<dataset>/<Model>.md` (`2,307` `type: Table`): verbatim introductory prose + dataset context, metadata bullets, `# Schema` (`Property | Type | Ref | Level | Access | URI | Title | Description`), and optional `# Enumerations`, `# Translations (@en)`, `# Prefixes`, `# Comments`, and `# Related References`.
  5. `bundle/references/` (`8` `type: Reference`) and `bundle/computations/ltl-to-eur-conversion.md` (`1` `type: Attested Computation`).
- Treat shipped concepts as `unverified` (`0` `verified` entries by default) unless current `verified` events (`at >= generated.at`) exist; attribute claims to `[^manifest]`, `[^dcat]`, and `[^std-*]` entries in `sources` without claiming agency endorsement.

## 2. `data.gov.lt` DCAT-AP Portal Metadata and Live `429`-Safe Fallback

- Check `# Portal Metadata (DCAT-AP)` in `bundle/<dataset>.md` first: matched datasets already carry `dct:accrualPeriodicity`, `dct:modified`, `dct:issued`, `dct:license`, `dct:publisher`, and `@lt`/`@en` descriptions cited via `[^dcat]` (`author: "team:vda"`).
- When a dataset lacks `# Portal Metadata (DCAT-AP)` or live portal freshness must be checked:
  1. Prefer querying a deployed catalog table on `get.data.gov.lt` with one bounded RQL filter (`?limit(5)`).
  2. Include the **trailing slash before `?`** whenever calling the `data.gov.lt` public catalog REST endpoint (`https://data.gov.lt/public/api/1/datasets/?limit=5&...`) because omitting `/` before `?` returns `HTTP 301 Moved Permanently` with an empty body.
  3. Never call `/partner/api/1/` endpoints without user-supplied `ApiKey` credentials, and never download full-catalog RDF dumps (`edp/dcat-ap.rdf`) to inspect one dataset.
  4. Stop immediately without retrying if `data.gov.lt` returns HTTP `429` or a connection error, and report static `[^manifest]` / `[^dcat]` bundle facts alongside which live portal field remained unverified.

```text
https://data.gov.lt/public/api/1/datasets/?limit=5
```

## 3. Manifest-vs-Live Schema Divergence

- Derive endpoint paths exclusively from frontmatter `resource:` (declared `<dataset>/<Model>`), never from the `Manifest CSV` filename bullet, because `151` of `1,100` upstream CSV filenames differ from their declared `dataset` namespaces (e.g., `datasets/gov/vmi/ja_sumoketi_mokesciai.csv` declares `datasets/gov/vmi/ja_mokesciai`, and `datasasets/gov/ivpk/svetainiu_atitikties_vertinimas` `[sic]` is preserved verbatim).
- Distinguish `# Schema` from `# Comments`: rows under `# Comments` (`update(type: "<type>", ref: "<unit>")`, `create(...)`) are unapplied steward backlog proposals, whereas live `get.data.gov.lt` serves the declared `# Schema`.
- Run a single `?limit(1)` probe before constructing wide `select()` projections because production `get.data.gov.lt` deployments can lag recent manifest commits (returning HTTP `400` `PropertyNotFound` on newly added fields) or expose columns documented in `Description` as temporarily empty during upstream IT migrations.

## 4. Hidden Scale Multipliers, Statutory Classifications, and Currency Breaks

- Read the introductory prose directly below `# <Title>` alongside `# Schema` `Ref`, `Title`, and `Description` on every `Table` concept because numeric columns (`integer`, `number`) frequently display `—` in `Ref` while prose states scale multipliers (`10^3`, `10^6`, `tūkst. EUR`, e.g., `datasets/gov/vkc/vvi/Imone`), rate denominators (`EUR/m²`, `m³/parą`), or archival/discontinuation notices.
- Prioritize explicit scale multipliers in introductory prose or column `Description` over boilerplate `# Comments` entries (such as `update(type: "money", ref: "EUR")`) because unapplied backlog comments routinely omit the `10^3` or `10^6` multiplier active in published values.
- Consult the statutory `Reference` and `Attested Computation` concepts before comparing, filtering, or summing codes and monetary amounts across years:
  - `bundle/references/lt-valiutos-istorija.md` & `bundle/computations/ltl-to-eur-conversion.md`: Euro adoption on `2015-01-01` at the irrevocable fixed rate **`1 EUR = 3.45280 LTL`** (Council Reg. (EU) No 851/2014 & Reg. (EC) No 1103/97), plus historical `LTL` (`1993-06-25`–`2014-12-31`), `LTT` (`talonas`), and `SUR` periods. Always use `computations/ltl-to-eur-conversion.md` when converting `LTL` amounts to `EUR`.
  - `bundle/references/evrk-nace-sekcijos.md`: EU Reg. (EC) No 1893/2006 (`EVRK 2` / `NACE Rev. 2`, 21 sections `A`–`U`, 88 divisions, 272 groups) and the **`2025-01-01` `EVRK 2.1` (`NACE Rev. 2.1`, Reg. (EU) 2023/137) break** — section letter shift (`J` splits into `J` publishing/broadcasting + `K` telecom/IT, shifting subsequent section letters `K`–`U`) AND **Division `45` (motor vehicle trade/repair) dissolution** into Divisions `46`, `47`, and `95`.
  - `bundle/references/cpv-bvpz-kodai.md`: EU Reg. (EC) No 213/2008 (`CPV` / `BVPŽ` public procurement vocabulary — 45 2-digit divisions `03`–`98` and 272 3-digit groups).
  - `bundle/references/iso-639-kalbu-kodai.md`: ISO 639-1 / 639-2 / 639-3 language codes plus special codes `zxx` (no linguistic content), `und` (undetermined), `mul` (multiple languages), and `mis` (uncoded).
  - `bundle/references/spinta-dsa-guide.md`: Spinta DSA architecture, maturity levels `0`–`5`, `access` semantics, and `get.data.gov.lt` vs `api.dataportal.gov.lt` rules.

## 5. Cross-Table Joins, Canonical Join Guides, Access Tiers, and Count Traps

- Join tables strictly according to `# Schema` `Level` and `Ref` on the referencing column:
  - `level >= 4`: join `<Model>.<fk>._id` to `<TargetModel>._id` (UUID match) even when `# Schema` `Ref` writes `<TargetModel>[<pk>]`.
  - `level = 3`: join `<Model>.<fk>.<pk>` to `<TargetModel>.<pk>` (natural-key match).
  - `level <= 2`: treat values as unlinked scalars with zero server-enforced referential integrity, and inspect a live sample (`?select(<field>)&limit(10)`) on both tables to verify leading zeros, formatting, code-vs-label usage, and null rates before joining client-side.
- Follow the canonical hub join references in `bundle/references/joins/` whenever linking legal entities, addresses, or procurements:
  - `bundle/references/joins/jar-legal-entities.md`: Joining against `datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo` (`level >= 4` UUID `_id` vs 9-digit `ja_kodas` two-step lookup).
  - `bundle/references/joins/ar-address-hierarchy.md`: Traversing `datasets/gov/rc/ar/*` (`Apskritis` -> `Savivaldybe` -> `Seniunija` -> `Gyvenviete` -> `Gatve` -> `AdresoObjektas`) and reconciling Lithuanian national grid **`LKS-94` (`EPSG:3346`, meters)** against **`WGS 84` (`EPSG:4326`, degrees)**.
  - `bundle/references/joins/vpt-procurement-notices.md`: Joining `datasets/gov/vpt/new/*` and `datasets/gov/vpt/old/*` procurement notices, contracts, CPV codes, and supplier/buyer JAR references.
- Never join two tables solely because they share a generic `<Model>` or `<field>` name (`kodas`, `id`, `savivaldybe`, `data`) unless `# Schema` `Ref` or `URI` binds both columns to the same canonical target.
- Verify Spinta `Access` on every target table and column before proposing anonymous access: only `open` and `open (inherited)` are unrestricted open data; `public` requires GDPR-authorized recipients and purpose limitation; `protected` and `private` are non-open; `—` means `access` was left blank in the manifest.
- Never report `len(_data)` from a `?limit(<N>)` sample or a `100`-row HTML page as total dataset rows, and never compute shares or rankings over page 1 when `"_page": {"next": "..."}` exists; run `?count()` (or `?<filter>&count()`) first.
