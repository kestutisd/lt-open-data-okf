---
type: Dataset
title: "Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas"
description: "Informacija apie gydymo įstaigas, vaistines ir kitas įmones."
resource: "https://get.data.gov.lt/datasets/gov/vlk/istaigos"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/vlk_istg.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1386/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/istaigos"
    author: "team:vda"
    last_modified: "2026-06-10T00:00:00Z"
---

# Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas

- **Namespace:** `datasets/gov/vlk/istaigos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/vlk_istg.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/istaigos` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1386/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/istaigos`[^dcat]
- **Portal Title (`@lt`):** Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas[^dcat]
- **Portal Title (`@en`):** List of medical institutions, pharmacies and other companies[^dcat]
- **Issued (`dct:issued`):** `2023-08-16`[^dcat]
- **Last Modified (`dct:modified`):** `2026-06-10`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-17` .. `2026-03-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie gydymo įstaigas, vaistines ir kitas įmones. IS SVEIDRA informacija[^dcat]

### Portal Description (`@en`)

List of medical institutions, pharmacies and other companies[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Istaiga](istaigos/Istaiga.md) | Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas | `4` | `kodas` | — | `18` | Informacija apie gydymo įstaigas, vaistines ir kitas įmones. |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bool` | `"Ne"` | — | — | Ne | — |
| `bool` | `"Taip"` | — | — | Taip | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vlk_istg.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/istaigos (https://data.gov.lt/datasets/1386/)
