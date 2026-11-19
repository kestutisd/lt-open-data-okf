---
type: Dataset
title: "Valstybės kontrolės finansinės būklės duomenys"
description: "Valstybės kontrolės finansinės būklės ataskaitos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/fba"
tags: [gov, vk, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/fba.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vk/fba.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1685/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/fba"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės kontrolės finansinės būklės duomenys

- **Namespace:** `datasets/gov/vk/fba`[^manifest]
- **Manifest CSV:** [datasets/gov/vk/fba.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/fba.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/fba` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1685/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos Respublikos valstybės kontrolė[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vk/fba`[^dcat]
- **Portal Title (`@lt`):** Valstybės kontrolės finansinės būklės duomenys[^dcat]
- **Portal Title (`@en`):** Data on the financial condition of the State Audit Office[^dcat]
- **Issued (`dct:issued`):** `2022-10-14`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-02-20` .. `2026-04-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės kontrolės finansinės būklės ataskaitos duomenys[^dcat]

### Portal Description (`@en`)

Data of the report on the financial condition of the State Audit Office[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FinansinesBuklesAtaskaita](fba/FinansinesBuklesAtaskaita.md) | Finansinės būklės ataskaita | `4` | — | — | `12` | Valstybės kontrolės finansinės būklės ataskaitos duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/fba.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/fba.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/fba (https://data.gov.lt/datasets/1685/)
