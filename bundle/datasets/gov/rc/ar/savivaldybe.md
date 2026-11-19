---
type: Dataset
title: "Adresų registras"
description: "Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/savivaldybe.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1286/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/savivaldybe"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/savivaldybe`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/savivaldybe.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1286/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe`[^dcat]
- **Portal Title (`@lt`):** Adresų registro savivaldybių tekstinių duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Address register municipal textual data set[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-08-18` .. `2025-05-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

A set of textual data of municipalities from the address register of the Republic of Lithuania (data describing the administrative units of the Republic of Lithuania - municipalities). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Savivaldybe](savivaldybe/Savivaldybe.md) | Adresų registro savivaldybių tekstinių duomenų rinkinys | `4` | `sav_kodas` | — | `6` | Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/savivaldybe.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/savivaldybe (https://data.gov.lt/datasets/1286/)
