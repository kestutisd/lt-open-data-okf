---
type: Dataset
title: "Adresų registras"
description: "Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gatve"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gatve.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1293/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/gatve"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/gatve`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/gatve.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gatve` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1293/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/gatve`[^dcat]
- **Portal Title (`@lt`):** Adresų registro gatvių tekstinių duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Address register street text data set[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-08-18` .. `2026-10-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatves apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

A set of street text data from the address register of the Republic of Lithuania (data describing streets). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Gatve](gatve/Gatve.md) | Adresų registro gatvių tekstinių duomenų rinkinys | `4` | `gat_kodas` | — | `8` | Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos gatves apibūdinantys duomenys). |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gatve.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/gatve (https://data.gov.lt/datasets/1293/)
