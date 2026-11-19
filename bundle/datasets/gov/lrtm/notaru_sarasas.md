---
type: Dataset
title: "Notarų sąrašo duomenų rinkinys"
description: "Informacija apie Lietuvoje veikiančius notarus"
resource: "https://get.data.gov.lt/datasets/gov/lrtm/notaru_sarasas"
tags: [gov, lrtm, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrtm/notaru_sarasas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lrtm/notaru_sarasas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3846/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrtm/notaru_sarasas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Notarų sąrašo duomenų rinkinys

Informacija apie Lietuvoje veikiančius notarus[^manifest]

- **Namespace:** `datasets/gov/lrtm/notaru_sarasas`[^manifest]
- **Manifest CSV:** [datasets/gov/lrtm/notaru_sarasas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrtm/notaru_sarasas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrtm/notaru_sarasas` (`deployed`)[^manifest]
- **Provider:** `lrtm` — Lietuvos Respublikos teisingumo ministerija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3846/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrtm/notaru_sarasas`[^dcat]
- **Portal Title (`@lt`):** Notarų sąrašas[^dcat]
- **Portal Title (`@en`):** List of Notaries[^dcat]
- **Issued (`dct:issued`):** `2025-06-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2025-05-29` .. `2025-06-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiamas Lietuvos Respublikos notarų sąrašas, užtikrinantis notariato veiklos skaidrumą, teisinį reguliavimą ir priežiūrą. Rinkinį sudaro istoriniai ir aktualūs duomenys apie notarus, jų paskyrimus, atleidimus, veiklą ir įgaliojimų sustabdymus. Vienoje duomenų rinkinio eilutėje pateikiama informacija apie notarą konkrečiame notarų biure. Duomenų teikėjas – Lietuvos Respublikos teisingumo ministerija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection includes a list of notaries of the Republic of Lithuania ensuring transparency, legal regulation and supervision of the activities of the notariat. The collection consists of historical and relevant data about notaries, their appointments, dismissals, activities and suspension of powers. One line of the data set shall contain information about a notary in a particular notary office. Data provider shall mean the Ministry of Justice of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NotaruSarasas](notaru_sarasas/NotaruSarasas.md) | Notarų sąrašas | `4` | `vda_prime_key` | — | `16` | Rinkinyje pateikiamas Lietuvos Respublikos notarų sąrašas, užtikrinantis notariato veiklos skaidrumą, teisinį reguliavimą ir priežiūrą. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrtm/notaru_sarasas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrtm/notaru_sarasas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrtm/notaru_sarasas (https://data.gov.lt/datasets/3846/)
