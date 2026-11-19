---
type: Dataset
title: "Adresų registras"
description: "Žemės sklypams, pastatams ir patalpoms suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams, pastatams ir patalpoms suteiktus adresus apibūdinantys duomenys (duomenų rinkinių grupė, 60 vnt.)) - adresų taškai."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/adresotaskas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1351/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresotaskas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/adresotaskas`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/adresotaskas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1351/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas`[^dcat]
- **Portal Title (`@lt`):** Adresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenys[^dcat]
- **Portal Title (`@en`):** Spatial data of the addresses allocated to land parcels and buildings from the Address Register[^dcat]
- **Issued (`dct:issued`):** `2023-09-01`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-08-25` .. `2023-11-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Žemės sklypams, pastatams ir patalpoms suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams, pastatams ir patalpoms suteiktus adresus apibūdinantys duomenys (duomenų rinkinių grupė, 60 vnt.)) - adresų taškai.[^dcat]

### Portal Description (`@en`)

Spatial dataset of the addresses allocated to land parcels and buildings from the Address Register (data describing the addresses allocated to land parcels and buildings (a group of datasets, 60 units)). Geographical coverage — entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AdresoTaskas](adresotaskas/AdresoTaskas.md) | Adresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenysAdresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenys | `4` | `aob_kodas` | — | `14` | Žemės sklypams ir pastatams suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ir pastatams suteiktus adresus... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/adresotaskas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/adresotaskas (https://data.gov.lt/datasets/1351/)
