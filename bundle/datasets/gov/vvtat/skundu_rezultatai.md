---
type: Dataset
title: "VVTAT ištirtų skundų rezultatai"
description: "Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai"
tags: [gov, vvtat, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/skundu_rezultatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2684/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/skundu_rezultatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VVTAT ištirtų skundų rezultatai

Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus.[^manifest]

- **Namespace:** `datasets/gov/vvtat/skundu_rezultatai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/skundu_rezultatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2684/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai`[^dcat]
- **Portal Title (`@lt`):** Valstybinės vartotojų teisių apsaugos tarnybos ištirtų skundų rezultatai[^dcat]
- **Portal Title (`@en`):** Results of complaints investigated by the State Consumer Rights Protection Authority[^dcat]
- **Issued (`dct:issued`):** `2024-06-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-06-05` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos (VVTAT) ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on complaints investigated by the State Consumer Rights Protection (VVTAT): dates of registration and completion of the investigation, companies mentioned in complaints and results of the investigation.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Skundas](skundu_rezultatai/Skundas.md) | VVTAT ištirtų skundų rezultatai | `4` | `vda_id` | — | `10` | Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/skundu_rezultatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/skundu_rezultatai (https://data.gov.lt/datasets/2684/)
