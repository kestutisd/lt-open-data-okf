# OKF v0.3 Frontmatter Fields, Provenance Rules, and Spinta Templates

This reference documents every OKF `v0.3` frontmatter field ([`SPEC.md`](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md) §§4–10) and the canonical templates for Lithuanian Open Data concepts.

## 1. YAML 1.2 Syntax Rules (`SPEC.md` §4)

- Begin frontmatter on line 1 with `---` and close with `---`.
- Parse strictly under the YAML 1.2 Core Schema mapping rules: **never repeat a key** (`E007`) and never use custom YAML tags.
- Quote strings that resemble numbers, booleans, dates, or colon-delimited actors (`okf_version: "0.3"`, `at: "2026-11-11T14:39:20Z"`, `by: "human:vardas-pavarde"`).
- Prefix custom producer extension fields with `x-<producer>-<name>` (unprefixed unknown keys trigger `I203`).
- Write `tags` as a YAML list (`tags: [gov, vmi, deployed]`) — scalar `tags: a, b` is read by consumers as a single tag `"a, b"` (`W110`).

## 2. Core, Provenance, Trust, Lifecycle, and Computation Fields

| Group | Field | Requirement | Format & Lithuanian Open Data Convention |
| --- | --- | --- | --- |
| **Core (§4.1)** | `type` | Required | `Dataset`, `Table`, `Reference`, or `Attested Computation`. |
| | `title` | Optional | Display title (`"<Model> — <LT Title>"` on tables). |
| | `description` | Optional | One concise sentence used in `index.md` and `scan.py`. |
| | `resource` | Optional | `https://get.data.gov.lt/<dataset>[/<Model>]` **only** when in `get_data_gov_lt.in`; omit when `undeployed` or abstract. |
| | `tags` | Optional | YAML list including provider segments and `deployed` or `undeployed` (plus `level-<N>` on tables). |
| **Provenance (§5.1)** | `sources` | Optional | List of `{ id, resource, title?, author?, last_modified?, usage_count?, usage_window? }`. |
| | `sources[].id` | Required if cited | Stable footnote key (`manifest`, `dcat`, `std-eur`, `std-evrk`, `std-cpv`, `std-iso639`). |
| | `sources[].resource` | Required | External URL, `/`-rooted bundle path, or space-containing scope descriptor. |
| | `sources[].author` | Optional | `"team:vssa"` (`atviriduomenys/manifest`), `"team:vda"` (`data.gov.lt` DCAT-AP), etc. |
| | `usage_window` | Required w/ `usage_count` | `{ from: "<timestamp>", to: "<timestamp>" }` at concept or source level. |
| **Trust (§§5.2–5.3)** | `generated` | Optional | `{ by: "<actor>", at: "<RFC3339-datetime>" }`. Bump `at` **only** when meaning changes. |
| | `verified` | Optional | List of `{ by: "<actor>", at: "<RFC3339-datetime>" }`. Current iff `at >= generated.at`. |
| **Lifecycle (§§5.4–5.5)** | `status` | Optional | Omit for `stable`; `draft` (`level == 0` / `/provisional/`); `deprecated` for retired concepts. |
| | `superseded_by` | Optional | `/`-rooted bundle path (`/datasets/.../<Replacement>.md`), valid only with `status: deprecated`. |
| | `stale_after` | Optional | RFC 3339 date-time or `YYYY-MM-DD` when a known review cycle exists; never guess. |
| **Computation (§10)** | `runtime` | Required | Execution engine (`python`, `bigquery`, `postgres`, `dbt`). |
| | `parameters` | Optional | List of `{ name, type, required }` (`type`: `number`, `integer`, `string`, `boolean`, `date`, `timestamp`). |
| | `computation` | Optional | `/`-rooted path to code file; omit when `# Computation` contains the single fenced code block. |
| | `executor` | Optional | `{ resource: "/references/executors/<name>.py", receipt: [<fields>] }`. |
| | `attester` | Optional | `{ resource: "/references/attesters/<name>.py" }` (deterministic, no LLM, returns `{ ok, reason? }`). |
| **Root Index (§8.1)** | `okf_version` | Root `index.md` only | `"0.3"` (quoted string). Subdirectory `index.md` and `log.md` have **no** frontmatter (`E004`, `E006`). |
| | `title`, `description`, `license` | Root `index.md` only | Bundle title, one-sentence routing scope, and SPDX expression `"AGPL-3.0-only"`. |

## 3. Actor, Timestamp, and Path Formats (`SPEC.md` §§5–7)

- **Actors (§7):** Either `<producer>/<version>` (`"lt-open-data-okf/0.3.0"`, `"antigravity/gemini-2.5-pro"`) or `<scheme>:<id>` (`"human:vardas-pavarde"`, `"team:vssa"`, `"team:vda"`, `"process:ci-manifest-sync"`). Only `human:<id>` yields `human-reviewed`; non-`human:` actors yield `machine-confirmed`.
- **Timestamps (§5):** Always use full UTC RFC 3339 date-times (`"2026-11-11T14:39:20Z"`) for `generated.at` and `verified[].at` (`W122` warns on date-only values there). `stale_after`, `last_modified`, and `usage_window` accept either RFC 3339 date-times or `YYYY-MM-DD` (`00:00:00Z`).
- **Paths (§6):** Write frontmatter path fields (`sources[].resource`, `computation`, `executor.resource`, `attester.resource`, `superseded_by`) with a leading `/` (`/references/attesters/ltl_to_eur_attester.py`) so they resolve from `BUNDLE_DIR`. Write Markdown links in the body relative to the containing file (`../ja_mokesciai.md`) so links work directly on GitHub. Percent-encode spaces (`%20`).

## 4. Lithuanian Open Data Concept Templates

### `Dataset` Concept (`bundle/datasets/.../<dataset>.md`)

````markdown
---
type: Dataset
title: "<Dataset Title>"
description: "<One-sentence dataset summary.>"
resource: "https://get.data.gov.lt/<dataset>"
tags: [gov, <agency>, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "<YYYY-MM-DDTHH:MM:SSZ>" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — <csv_path>"
    resource: "https://github.com/atviriduomenys/manifest/blob/<commit>/<csv_path>#L<line>"
    author: "team:vssa"
    last_modified: "<YYYY-MM-DDTHH:MM:SSZ>"
  - id: dcat
    title: "data.gov.lt DCAT-AP — <Portal Title>"
    resource: "https://data.gov.lt/datasets/<portal_id>/"
    author: "team:vda"
    last_modified: "<YYYY-MM-DDTHH:MM:SSZ>"
---

# <Dataset Title>

<Dataset introductory description.>[^manifest]

# Portal Metadata (DCAT-AP)

- **Publisher (`dct:publisher`):** <Agency Name>[^dcat]
- **Update Frequency (`dct:accrualPeriodicity`):** `<uri>`
- **Modified (`dct:modified`):** `<date>`
- **License (`dct:license`):** `<uri>`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [<Model>](<dataset_leaf>/<Model>.md) | <Model Title> | `4` | `id` | `open` | 12 | — |

[^manifest]: atviriduomenys/manifest — <csv_path>
[^dcat]: data.gov.lt DCAT-AP — <Portal Title>
````

### `Table` Concept (`bundle/datasets/.../<dataset>/<Model>.md`)

````markdown
---
type: Table
title: "<Model> — <Model Title>"
description: "Spinta table <dataset>/<Model> (<N> columns)."
resource: "https://get.data.gov.lt/<dataset>/<Model>"
tags: [gov, <agency>, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "<YYYY-MM-DDTHH:MM:SSZ>" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — <csv_path>"
    resource: "https://github.com/atviriduomenys/manifest/blob/<commit>/<csv_path>#L<line>"
    author: "team:vssa"
    last_modified: "<YYYY-MM-DDTHH:MM:SSZ>"
---

# <Model> — <Model Title>

<Verbatim scrubbed table description, including any scale multipliers or archival notes.>[^manifest]

- **Model:** `<dataset>/<Model>`[^manifest]
- **Dataset:** [<Dataset Title>](../<dataset_leaf>.md) (`<dataset>`)
- **Primary Key (`ref`):** `<pk>`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | <Title> | — |

[^manifest]: atviriduomenys/manifest — <csv_path>
````

### `Attested Computation` Concept (`bundle/computations/<slug>.md`)

````markdown
---
type: Attested Computation
title: "<Computation Title>"
description: "<One-sentence summary of the statutory computation.>"
tags: [currency, eur, ltl, statutory]
runtime: python
parameters:
  - { name: ltl_amount, type: number, required: true }
executor:
  resource: "/references/executors/ltl_to_eur.py"
  receipt: [ltl_amount, rate_used, unrounded_eur, eur_amount, computation_sha256]
attester:
  resource: "/references/attesters/ltl_to_eur_attester.py"
generated: { by: "lt-open-data-okf/0.3.0", at: "<YYYY-MM-DDTHH:MM:SSZ>" }
sources:
  - id: std-eur
    title: "Council Regulation (EU) No 851/2014 & Reg. (EC) No 1103/97"
    resource: "https://publications.europa.eu/resource/celex/32014R0851"
---

# Computation

```python
# Exact sanctioned statutory formula (1 EUR = 3.45280 LTL, half-up to 2 decimals)
```

Implements the irrevocable conversion rate `1 EUR = 3.45280 LTL`.[^std-eur]

[^std-eur]: Council Regulation (EU) No 851/2014 & Reg. (EC) No 1103/97
````

### `Deprecated` Concept Stub

````markdown
---
type: Table
title: "<OldModel> (Deprecated)"
description: "Retired Spinta table replaced by <NewModel>."
tags: [gov, <agency>, undeployed]
status: deprecated
superseded_by: "/datasets/gov/<agency>/<dataset>/<NewModel>.md"
generated: { by: "<tool>/<model>", at: "<YYYY-MM-DDTHH:MM:SSZ>" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — <csv_path>"
    resource: "https://github.com/atviriduomenys/manifest/blob/<commit>/<csv_path>"
    author: "team:vssa"
---

This table is retired.[^manifest] Use [<NewModel>](<relative-path-to-NewModel>.md) instead.

[^manifest]: atviriduomenys/manifest — <csv_path>
````
