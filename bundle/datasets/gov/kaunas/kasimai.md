---
type: Dataset
title: "Kauno miesto savivaldybės teikiami duomenys"
description: "Kauno mieste vykdomi kasimo darbai"
resource: "https://get.data.gov.lt/datasets/gov/kaunas/kasimai"
tags: [gov, kaunas, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/kasimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kaunas/kasimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2078/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kaunas/kasimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kauno miesto savivaldybės teikiami duomenys

Kauno mieste vykdomi kasimo darbai[^manifest]

- **Namespace:** `datasets/gov/kaunas/kasimai`[^manifest]
- **Manifest CSV:** [datasets/gov/kaunas/kasimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/kasimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kaunas/kasimai` (`deployed`)[^manifest]
- **Provider:** `kaunas` — Kauno miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2078/`[^dcat]
- **Publisher (`dct:publisher`):** Kauno miesto savivaldybės administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kaunas/kasimai`[^dcat]
- **Portal Title (`@lt`):** Kasimų darbai[^dcat]
- **Portal Title (`@en`):** Excavation works[^dcat]
- **Issued (`dct:issued`):** `2022-12-15`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-05-23` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Išduoti leidimai kasimų darbų vykdymui miesto viešose erdvėse[^dcat]

### Portal Description (`@en`)

Permits have been issued for the execution of excavation works in the city&#39;s public spaces[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kasimai](kasimai/Kasimai.md) | Kasimo darbai | `4` | `id` | — | `21` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kaunas/kasimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/kasimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kaunas/kasimai (https://data.gov.lt/datasets/2078/)
