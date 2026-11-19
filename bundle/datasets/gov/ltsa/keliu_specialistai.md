---
type: Dataset
title: "Kelių specialistų sąrašas"
description: "Kelių specialistų sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai"
tags: [gov, ltsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/keliu_specialistai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2334/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/keliu_specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kelių specialistų sąrašas

- **Namespace:** `datasets/gov/ltsa/keliu_specialistai`[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/keliu_specialistai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2334/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos transporto saugos administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ltsa/keliu_specialistai`[^dcat]
- **Portal Title (`@lt`):** Kelių specialistų sąrašas[^dcat]
- **Portal Title (`@en`):** Road specialists[^dcat]
- **Issued (`dct:issued`):** `2023-10-04`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-09-25` .. `2024-10-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kelių specialistų sąrašas[^dcat]

### Portal Description (`@en`)

Road specialist list[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [RoadSpecialist](keliu_specialistai/RoadSpecialist.md) | Kelių specialistų sąrašas | `4` | `id` | — | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/keliu_specialistai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/keliu_specialistai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/keliu_specialistai (https://data.gov.lt/datasets/2334/)
