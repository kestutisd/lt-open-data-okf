---
type: Dataset
title: "Adresų registras"
description: "Istorinių (panaikintų) gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - istorines (panaikintas) gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gragyvenamojivietove"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragyvenamojivietove.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gragyvenamojivietove.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1348/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/gragyvenamojivietove"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/gragyvenamojivietove`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/gragyvenamojivietove.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragyvenamojivietove.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gragyvenamojivietove` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1348/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove`[^dcat]
- **Portal Title (`@lt`):** Adresų registro istorinių (panaikintų) gyvenamųjų vietovių erdviniai duomenys[^dcat]
- **Portal Title (`@en`):** Spatial data of historical (annulled) residential areas from the Address Register[^dcat]
- **Issued (`dct:issued`):** `2023-09-01`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2025-04-23` .. `2025-04-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Istorinių (panaikintų) gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - istorines (panaikintas) gyvenamąsias vietoves apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

Spatial dataset of historical (annulled) residential areas from the Address Register of the Republic of Lithuania (administrative units of the Republic of Lithuania, namely the data describing historical (annulled) residential areas). Geographical coverage — entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GraGyvenamojiVietove](gragyvenamojivietove/GraGyvenamojiVietove.md) | Adresų registro gyvenamųjų vietovių erdviniai duomenys | `4` | `gyv_kodas` | — | `7` | Gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus – gyvenamąsias... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gragyvenamojivietove.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragyvenamojivietove.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/gragyvenamojivietove (https://data.gov.lt/datasets/1348/)
