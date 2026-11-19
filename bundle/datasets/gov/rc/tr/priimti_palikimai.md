---
type: Dataset
title: "Testamentų registro (TR) duomenys apie priimtą palikimą"
description: "TR duomenys apie priimtą palikimą."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/priimti_palikimai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/priimti_testamentai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/priimti_testamentai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2142/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/tr/priimti_palikimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Testamentų registro (TR) duomenys apie priimtą palikimą

- **Namespace:** `datasets/gov/rc/tr/priimti_palikimai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/tr/priimti_testamentai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/priimti_testamentai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/priimti_palikimai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2142/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/tr/priimti_palikimai`[^dcat]
- **Portal Title (`@lt`):** Testamentų registro (TR) duomenys apie priimtą palikimą[^dcat]
- **Portal Title (`@en`):** TR data on accepted inheritance[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

TR duomenys apie priimtą palikimą. Testamentų registro (TR) duomenys.[^dcat]

### Portal Description (`@en`)

TR data on accepted inheritance. Data from the Register of Wills (TR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PriimtasPalikimas](priimti_palikimai/PriimtasPalikimas.md) | — | `4` | `id` | — | `9` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/priimti_testamentai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/priimti_testamentai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/tr/priimti_palikimai (https://data.gov.lt/datasets/2142/)
