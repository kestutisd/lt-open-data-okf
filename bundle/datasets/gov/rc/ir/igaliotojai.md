---
type: Dataset
title: "Įgaliojimų registro (ĮR) įgaliotojų duomenys"
description: "Įgaliotojų duomenys​ (amžius, gyvenamoji vieta)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/igaliotojai"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotojai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/igaliotojai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2164/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/igaliotojai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Įgaliojimų registro (ĮR) įgaliotojų duomenys

- **Namespace:** `datasets/gov/rc/ir/igaliotojai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/igaliotojai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotojai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/igaliotojai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2164/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ir/igaliotojai`[^dcat]
- **Portal Title (`@lt`):** Įgaliojimų registro (ĮR) įgaliotojų duomenys[^dcat]
- **Portal Title (`@en`):** Data of authorized persons of the Register of Authorizations (RA).[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-01-09` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Įgaliotojų duomenys​ (amžius, gyvenamoji vieta). Įgaliojimų registro (ĮR) pirminiai duomenys ( RAW DATA).[^dcat]

### Portal Description (`@en`)

Details of authorized persons (age, place of residence). Initial data of the authorization register (RAW DATA). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Igaliotojas](igaliotojai/Igaliotojas.md) | Įgaliotojų duomenys | `4` | `nr` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/igaliotojai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotojai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/igaliotojai (https://data.gov.lt/datasets/2164/)
