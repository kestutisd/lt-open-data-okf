---
type: Dataset
title: "Valstybės kontrolės biudžeto vykdymo ataskaitų duomenys"
description: "Valstybės kontrolės biudžeto išlaidų sąmatos vykdymo duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/bva"
tags: [gov, vk, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bva.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vk/bva.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1847/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/bva"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės kontrolės biudžeto vykdymo ataskaitų duomenys

- **Namespace:** `datasets/gov/vk/bva`[^manifest]
- **Manifest CSV:** [datasets/gov/vk/bva.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bva.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/bva` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1847/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos Respublikos valstybės kontrolė[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vk/bva`[^dcat]
- **Portal Title (`@lt`):** Valstybės kontrolės biudžeto vykdymo ataskaitų duomenys[^dcat]
- **Portal Title (`@en`):** Data on the reports on the implementation of the budget of the State Audit Office[^dcat]
- **Issued (`dct:issued`):** `2023-02-20`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-02-20` .. `2026-10-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės kontrolės biudžeto išlaidų sąmatos vykdymo duomenys[^dcat]

### Portal Description (`@en`)

Data on the execution of the budget expenditure estimate of the State Audit Office[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BiudzetoVykdymoAtaskaita](bva/BiudzetoVykdymoAtaskaita.md) | Biudžeto vykdymo ataskaita | `4` | — | — | `18` | Valstybės kontrolės biudžeto išlaidų sąmatos vykdymo duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/bva.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bva.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/bva (https://data.gov.lt/datasets/1847/)
