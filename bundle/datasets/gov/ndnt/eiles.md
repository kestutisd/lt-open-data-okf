---
type: Dataset
title: "Asmenų apgyvendinimo globos namuose eilių duomenys"
description: "Lentelėje pateikti asmenų apgyvendinimo globos namuose 2022 ir 2023 metų eilių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ndnt/eiles"
tags: [gov, ndnt, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/eiles.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ndnt/eiles.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2907/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ndnt/eiles"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Asmenų apgyvendinimo globos namuose eilių duomenys

- **Namespace:** `datasets/gov/ndnt/eiles`[^manifest]
- **Manifest CSV:** [datasets/gov/ndnt/eiles.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/eiles.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ndnt/eiles` (`deployed`)[^manifest]
- **Provider:** `ndnt` — Asmens su negalia teisių apsaugos agentūra (buv. NDNT) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2907/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ndnt/eiles`[^dcat]
- **Portal Title (`@lt`):** Asmenų apgyvendinimo globos namuose eilių duomenys[^dcat]
- **Portal Title (`@en`):** Home Accommodation Sequence Data[^dcat]
- **Issued (`dct:issued`):** `2024-12-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-12-20` .. `2024-12-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti asmenų apgyvendinimo globos namuose 2022 ir 2023 metų eilių duomenys. Duomenų teikėjas – Asmens su negalia teisių apsaugos agentūra prie LR socialinės apsaugos ir darbo ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table shows the ranking data for the accommodation of individuals in foster homes for 2022 and 2023. Data provider shall mean the Agency for the Protection of Rights of Persons with Disabilities under the Ministry of Social Security and Labour of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ApgyvendinimoEile](eiles/ApgyvendinimoEile.md) | Asmenų apgyvendinimo globos namuose eilių duomenys | `4` | `iraso_id` | — | `13` | Lentelėje pateikti asmenų apgyvendinimo globos namuose 2022 ir 2023 metų eilių duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ndnt/eiles.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/eiles.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ndnt/eiles (https://data.gov.lt/datasets/2907/)
