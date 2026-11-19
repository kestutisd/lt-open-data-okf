---
type: Dataset
title: "Valstybės valdomų įmonių sąrašas"
description: "Valstybės valdomų įmonių kolegialių organų sudėtis."
resource: "https://get.data.gov.lt/datasets/gov/vkc/sudetis"
tags: [gov, vkc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vkc/sudetis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vkc/sudetis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės valdomų įmonių sąrašas

- **Namespace:** `datasets/gov/vkc/sudetis`[^manifest]
- **Manifest CSV:** [datasets/gov/vkc/sudetis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkc/sudetis` (`deployed`)[^manifest]
- **Provider:** `vkc` — Valdymo koordinavimo centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2840/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vkc/sudetis`[^dcat]
- **Portal Title (`@lt`):** Kolegialių organų sudėtis[^dcat]
- **Portal Title (`@en`):** Composition of collegial bodies[^dcat]
- **Issued (`dct:issued`):** `2024-10-31`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-10-31` .. `2024-10-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės valdomų įmonių kolegialių organų sudėtis. Duomenų rinkinyje pateikiamas įmonės pavadinimas, įmonės kodas, nario vardas ir pavardė, pareigos, pozicija, informacijos aktualumo data. Rinkinio duomenys ateityje nebus naujinami. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Composition of collegial bodies of state-owned enterprises. The data set shall include the company name, company code, member's name, position, position, date of relevance of the information. The set data will not be updated in the future. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sudetis](sudetis/Sudetis.md) | Valstybės valdomų įmonių sąrašas | `4` | `vda_id` | — | `9` | Valstybės valdomų įmonių sąraše yra pateikiamas - įmonės pavadinimas,įmonės kodas, nario vardas ir pavardė, pareigos, pozicija. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkc/sudetis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vkc/sudetis (https://data.gov.lt/datasets/2840/)
