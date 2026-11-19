---
type: Dataset
title: "Valstybės strategijų elementų finansiniai duomenys"
description: "Lentelėje pateikti valstybės strategijų objektų elementų, kurie turi priskirtas pinigines vertes (pvz., lėšų projekcijas), finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Strateginio valdymo informacinės sistemos (SVIS)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/strategiju_finansiniai_duomenys"
tags: [gov, finmin, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2846/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/strategiju_finansiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Valstybės strategijų elementų finansiniai duomenys

- **Namespace:** `datasets/gov/finmin/strategiju_finansiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/strategiju_finansiniai_duomenys` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2846/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/finmin/strategiju_finansiniai_duomenys`[^dcat]
- **Portal Title (`@lt`):** Valstybės strategijų elementų finansiniai duomenys[^dcat]
- **Portal Title (`@en`):** Financial data of State Strategy Elements[^dcat]
- **Issued (`dct:issued`):** `2024-11-05`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-05-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti valstybės strategijų objektų elementų, kurie turi priskirtas pinigines vertes (pvz., lėšų projekcijas), finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Strateginio valdymo informacinės sistemos (SVIS). Informacija pateikiama nuo duomenų rinkimo pradžios (2023 metų) atnaujinant kas ketvirtį. Duomenų teikėjas – Lietuvos Respublikos finansų ministerija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table contains financial data from the Strategic Management Information System (Svis) of the Ministry of Finance of the Republic of Lithuania on elements of objects of state strategies that have assigned monetary values (E.G. funds projections). The information shall be provided from the beginning of data collection (2023) by quarterly updating. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FinStrategija](strategiju_finansiniai_duomenys/FinStrategija.md) | Valstybės strategijų elementų finansiniai duomenys | `4` | `iraso_id` | — | `14` | Lentelėje pateikti valstybės strategijų objektų elementų, kurie turi priskirtas pinigines vertes (pvz., lėšų projekcijas), finansiniai duomenys iš Lietuvos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/strategiju_finansiniai_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/strategiju_finansiniai_duomenys (https://data.gov.lt/datasets/2846/)
