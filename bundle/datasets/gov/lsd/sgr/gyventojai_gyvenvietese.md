---
type: Dataset
title: "gyventojų skaičius gyvenvietėse"
description: "\"Gyventojų skaičius gyvenvietėse\""
resource: "https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese"
tags: [gov, lsd, deployed, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2938/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sgr/gyventojai_gyvenvietese"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# gyventojų skaičius gyvenvietėse

"Gyventojų skaičius gyvenvietėse"[^manifest]

- **Namespace:** `datasets/gov/lsd/sgr/gyventojai_gyvenvietese`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2938/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese`[^dcat]
- **Portal Title (`@lt`):** Lietuvos gyventojų skaičius gyvenvietėse[^dcat]
- **Portal Title (`@en`):** Population of Lithuania in settlements[^dcat]
- **Issued (`dct:issued`):** `2025-02-19`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `OTHER` (`http://publications.europa.eu/resource/authority/frequency/OTHER`)[^dcat]
- **Distribution Date Span:** `2025-02-19` .. `2026-01-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys apima visas Lietuvos Respublikos teritorijoje esančias gyvenvietes su priskirtais gyventojų skaičiaus atributais. Rinkinys sudarytas remiantis Valstybės duomenų agentūros 2021 metais atlikto visuotinio gyventojų surašymo duomenimis. Duomenų rinkinį sudaro: •	Gyvenvietės identifikatorius; •	Gyvenvietės pavadinimas; •	Gyvenvietės koordinatės; •	Gyventojų skaičius gyvenvietėje. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall comprise all settlements located in the territory of the Republic of Lithuania with assigned population attributes. The set is based on data from the World Census conducted by the State Data Agency in 2021. The dataset shall consist of: • Settlement identifier; • name of the settlement; • Settlement coordinates; • Number of inhabitants in the settlement. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyventojuSkaiciusGyvenvietese](gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese.md) | — | `4` | `gr_gyv_id` | — | `4` | "Gyventojų skaičius gyvenvietėse ir gyvenviečių koordinates. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sgr/gyventojai_gyvenvietese (https://data.gov.lt/datasets/2938/)
