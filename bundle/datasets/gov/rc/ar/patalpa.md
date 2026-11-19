---
type: Dataset
title: "Adresų registras"
description: "Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys (duomenų rinkinių grupė (60 vnt.))."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/patalpa"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/patalpa.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1343/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/patalpa"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/patalpa`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/patalpa.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/patalpa` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1343/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/patalpa`[^dcat]
- **Portal Title (`@lt`):** Adresų registro gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys[^dcat]
- **Portal Title (`@en`):** Textual data describing the addresses of residential and non-residential premises from the Address Register[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-08-18` .. `2024-05-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys (duomenų rinkinių grupė (60 vnt.)).[^dcat]

### Portal Description (`@en`)

Textual dataset describing the addresses of residential and non-residential premises from the Address Register of the Republic of Lithuania (textual data describing the addresses of residential and non-residential premises (group of datasets (60 units)). Geographical coverage — entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Patalpa](patalpa/Patalpa.md) | Adresų registro gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys | `4` | `aob_kodas` | — | `4` | Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/patalpa.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/patalpa (https://data.gov.lt/datasets/1343/)
