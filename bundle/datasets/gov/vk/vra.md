---
type: Dataset
title: "Valstybės kontrolės veiklos rezultatai"
description: "Valstybės kontrolės veiklos rezultatų ataskaitos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/vra"
tags: [gov, vk, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/vra.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vk/vra.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1687/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/vra"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės kontrolės veiklos rezultatai

- **Namespace:** `datasets/gov/vk/vra`[^manifest]
- **Manifest CSV:** [datasets/gov/vk/vra.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/vra.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/vra` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1687/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos Respublikos valstybės kontrolė[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vk/vra`[^dcat]
- **Portal Title (`@lt`):** Valstybės kontrolės veiklos rezultatai[^dcat]
- **Portal Title (`@en`):** Performance results of the State Audit Office[^dcat]
- **Issued (`dct:issued`):** `2023-02-20`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-02-20` .. `2026-04-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės kontrolės veiklos rezultatų ataskaitos duomenys[^dcat]

### Portal Description (`@en`)

Data from the State Audit Office Performance Report[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VeiklosRezultatuAtaskaita](vra/VeiklosRezultatuAtaskaita.md) | Veiklos rezultatų ataskaita | `4` | — | — | `9` | Valstybės kontrolės veiklos rezultatų ataskaitos duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/vra.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/vra.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/vra (https://data.gov.lt/datasets/1687/)
