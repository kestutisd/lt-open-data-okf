---
type: Dataset
title: "Medicininių intervencijų sąrašas (ACHI)"
description: "Informacija apie medicinines intervencijas."
resource: "https://get.data.gov.lt/datasets/gov/vlk/achi"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/achi.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1383/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/achi"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Medicininių intervencijų sąrašas (ACHI)

- **Namespace:** `datasets/gov/vlk/achi`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/achi.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/achi` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1383/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/achi`[^dcat]
- **Portal Title (`@lt`):** Medicininių intervencijų sąrašas (ACHI)[^dcat]
- **Portal Title (`@en`):** List of Medical Interventions (ACHI)[^dcat]
- **Issued (`dct:issued`):** `2023-06-30`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-11-16` .. `2025-12-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie medicinines intervencijas. ACHI – tai Australijos medicininių intervencijų klasifikacija. Jos devintasis leidimas pakeičia aštuntąjį, išleistą 2013 metais.[^dcat]

### Portal Description (`@en`)

Information on medical interventions. ACHI is the Australian Classification of Medical Interventions. Its ninth edition replaces the eighth one, released in 2013.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Intervencija](achi/Intervencija.md) | Medicininių intervencijų sąrašas | `4` | `ad_id` | — | `16` | Informacija apie medicinines intervencijas. |
| [Paslauga](achi/Paslauga.md) | Dienos chirurgijos metu atiliekamų intervencijų sąrašas | `4` | `ad_id` | — | `7` | — |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `int_r` | `"Ne"` | — | — | — | — |
| `int_r` | `"Taip"` | — | — | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/achi.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/achi (https://data.gov.lt/datasets/1383/)
