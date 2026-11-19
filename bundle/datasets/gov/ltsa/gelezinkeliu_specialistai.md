---
type: Dataset
title: "Geležinkelio specialistų pažymėjimai"
description: "Geležinkelių specialistų sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai"
tags: [gov, ltsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2333/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Geležinkelio specialistų pažymėjimai

- **Namespace:** `datasets/gov/ltsa/gelezinkeliu_specialistai`[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2333/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos transporto saugos administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_specialistai`[^dcat]
- **Portal Title (`@lt`):** Geležinkelių specialistų pažymėjimai[^dcat]
- **Portal Title (`@en`):** Railway specialits[^dcat]
- **Issued (`dct:issued`):** `2023-10-04`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-09-18` .. `2023-09-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Geležinkelių specialistų sąrašas[^dcat]

### Portal Description (`@en`)

Railway specialist list[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [RailwaySpecialist](gelezinkeliu_specialistai/RailwaySpecialist.md) | Geležinkelio specialistų pažymėjimai | `2` | `document_number` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_specialistai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_specialistai (https://data.gov.lt/datasets/2333/)
