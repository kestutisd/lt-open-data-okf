---
type: Dataset
title: "Nusikalstamų veikų statistiniai duomenys"
description: "Nusikalstamų veikų statistiniai duomenys"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas"
tags: [gov, ird, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1235/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Nusikalstamų veikų statistiniai duomenys

Informatikos ir ryšių departamentas prie LR Vidaus reikalų ministerijos[^manifest]

- **Namespace:** `datasets/gov/ird/nusikalstamumas`[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `11` (11 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1235/`[^dcat]
- **Publisher (`dct:publisher`):** Informatikos ir ryšių departamentas prie Lietuvos Respublikos vidaus reikalų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas`[^dcat]
- **Portal Title (`@lt`):** Nusikalstamų veikų statistiniai duomenys[^dcat]
- **Portal Title (`@en`):** Crime statistics[^dcat]
- **Issued (`dct:issued`):** `2021-11-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-12-14` .. `2023-12-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Nusikalstamų veikų statistiniai duomenys[^dcat]

### Portal Description (`@en`)

Crime statistics[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IndicatorsDimension](nusikalstamumas/IndicatorsDimension.md) | IndicatorsDimension | `4` | `id` | — | `4` | Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų ir jų pavadinimai, kodai ir aprašymai |
| [IndicatorsDimensionsI18N](nusikalstamumas/IndicatorsDimensionsI18N.md) | IndicatorsDimensionsI18N | `4` | `id` | — | `4` | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsDimensionsValue](nusikalstamumas/IndicatorsDimensionsValue.md) | IndicatorsDimensionsValue | `4` | `id` | — | `5` | Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų reikšmės |
| [IndicatorsDimensionsValuesI18N](nusikalstamumas/IndicatorsDimensionsValuesI18N.md) | IndicatorsDimensionsValuesI18N | `4` | `id` | — | `5` | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsItem](nusikalstamumas/IndicatorsItem.md) | IndicatorsItem | `4` | `id` | — | `3` | Lentelė, kurioje apibrėžiami statistinių reikšmių rodikliai |
| [IndicatorsItemsI18N](nusikalstamumas/IndicatorsItemsI18N.md) | IndicatorsItemsI18N | `4` | `id` | — | `4` | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsKeyFamilie](nusikalstamumas/IndicatorsKeyFamilie.md) | IndicatorsKeyFamilie | `4` | `id` | — | `4` | Lentelė, kurioje saugomi rodikliai ir juos sudarančios dimensijos |
| [IndicatorsKeyFamiliesI18N](nusikalstamumas/IndicatorsKeyFamiliesI18N.md) | IndicatorsKeyFamiliesI18N | `4` | `id` | — | `4` | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsMapping](nusikalstamumas/IndicatorsMapping.md) | IndicatorsMapping | `4` | `id` | — | `4` | Lentelė, kurioje yra saugomi duomenys apie ataskaitas |
| [IndicatorsMetadata](nusikalstamumas/IndicatorsMetadata.md) | IndicatorsMetadata | `4` | `id` | — | `4` | Lentelė, kurioje yra saugomos rodiklių metaduomenys |
| [IndicatorsOb](nusikalstamumas/IndicatorsOb.md) | IndicatorsOb | `4` | `item, dt` | — | `2` | Lentelė, kurioje yra saugomos rodiklių reikšmės |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/nusikalstamumas (https://data.gov.lt/datasets/1235/)
