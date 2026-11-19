---
type: Dataset
title: "Švietimo ir mokslo institucijos"
description: "Duomenų rinkinys parengtas remiantis Švietimo ir mokslo institucijų registru."
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimo_istaigos"
tags: [gov, lsd, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimo_istaigos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/svietimo_istaigos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2024/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimo_istaigos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Švietimo ir mokslo institucijos

- **Namespace:** `datasets/gov/lsd/svietimo_istaigos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/svietimo_istaigos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimo_istaigos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimo_istaigos` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2024/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/svietimo_istaigos`[^dcat]
- **Portal Title (`@lt`):** Švietimo ir mokslo institucijų duomenys[^dcat]
- **Portal Title (`@en`):** Data of educational and scientific institutions[^dcat]
- **Issued (`dct:issued`):** `2022-11-09`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2022-09-27` .. `2026-05-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys parengtas remiantis Švietimo ir mokslo institucijų registru. Rinkinyje pateikiami duomenys apie šiuo metu veikiančias švietimo ir mokslo institucijas (mokyklas, universitetus, darželius, profesinį mokymą, neformalųjį ugdymą teikiančias ir kt. įstaigas) arba institucijas, kurios šiuo metu neveikia, bet veikė po 2001 m. spalio 12 d. Rinkinyje rasite institucijų pavadinimus, JAR kodus arba, jei institucija neturi JAR kodo, ŠMIR suteikiamus institucijos padalinio kodus, institucijos registravimo datą, geoerdvines koordinates, adresą ir kt. Duomenys pateikiami ir apie savarankiškas institucijas, ir apie kitų institucijų padalinius. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data of educational and scientific institutions are provided based on the Register of Educational and Scientific Institutions. The data is updated once a month. (Point) geospatial coordinates of all currently registered (operating) and part of previously registered institutions are provided.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SvietimoIstaiga](svietimo_istaigos/SvietimoIstaiga.md) | Švietimo ir mokslo institucijos | `4` | `ins_id` | — | `16` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/svietimo_istaigos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimo_istaigos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimo_istaigos (https://data.gov.lt/datasets/2024/)
