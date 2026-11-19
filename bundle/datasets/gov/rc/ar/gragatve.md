---
type: Dataset
title: "Adresų registras"
description: "Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gragatve"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gragatve.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1349/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/gragatve"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/gragatve`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/gragatve.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gragatve` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1349/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/gragatve`[^dcat]
- **Portal Title (`@lt`):** Adresų registro gatvių ašinių linijų erdviniai duomenys[^dcat]
- **Portal Title (`@en`):** Spatial data of street centrelines from the Address Register[^dcat]
- **Issued (`dct:issued`):** `2023-09-01`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-08-18` .. `2025-10-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

Spatial dataset of the street centrelines from the Address Register of the Republic of Lithuania (data describing street centrelines). Geographical coverage — entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GraGatve](gragatve/GraGatve.md) | Adresų registro gatvių ašinių linijų erdviniai duomenys | `4` | `gat_kodas` | — | `7` | Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys). |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gragatve.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/gragatve (https://data.gov.lt/datasets/1349/)
