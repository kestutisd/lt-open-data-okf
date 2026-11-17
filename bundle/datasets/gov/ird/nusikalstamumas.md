---
type: Dataset
title: "datasets/gov/ird/nusikalstamumas"
description: "Informatikos ir ryšių departamentas prie LR Vidaus reikalų ministerijos"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas"
tags: [gov, ird, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/ird/nusikalstamumas

- **Namespace:** `datasets/gov/ird/nusikalstamumas`[^manifest]
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas`
- **Parent Namespace (`ns`):** Informatikos ir ryšių departamentas (`datasets/gov/ird`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IndicatorsDimension](nusikalstamumas/IndicatorsDimension.md) | IndicatorsDimension | `4` | `id` | — | 4 | Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų ir jų pavadinimai, kodai ir aprašymai |
| [IndicatorsDimensionsI18N](nusikalstamumas/IndicatorsDimensionsI18N.md) | IndicatorsDimensionsI18N | `4` | `id` | — | 4 | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsDimensionsValue](nusikalstamumas/IndicatorsDimensionsValue.md) | IndicatorsDimensionsValue | `4` | `id` | — | 5 | Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų reikšmės |
| [IndicatorsDimensionsValuesI18N](nusikalstamumas/IndicatorsDimensionsValuesI18N.md) | IndicatorsDimensionsValuesI18N | `4` | `id` | — | 5 | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsItem](nusikalstamumas/IndicatorsItem.md) | IndicatorsItem | `4` | `id` | — | 3 | Lentelė, kurioje apibrėžiami statistinių reikšmių rodikliai |
| [IndicatorsItemsI18N](nusikalstamumas/IndicatorsItemsI18N.md) | IndicatorsItemsI18N | `4` | `id` | — | 4 | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsKeyFamilie](nusikalstamumas/IndicatorsKeyFamilie.md) | IndicatorsKeyFamilie | `4` | `id` | — | 4 | Lentelė, kurioje saugomi rodikliai ir juos sudarančios dimensijos |
| [IndicatorsKeyFamiliesI18N](nusikalstamumas/IndicatorsKeyFamiliesI18N.md) | IndicatorsKeyFamiliesI18N | `4` | `id` | — | 4 | Lentelė, kurioje yra saugomas dimensijų aprašymas |
| [IndicatorsMapping](nusikalstamumas/IndicatorsMapping.md) | IndicatorsMapping | `4` | `id` | — | 4 | Lentelė, kurioje yra saugomi duomenys apie ataskaitas |
| [IndicatorsMetadata](nusikalstamumas/IndicatorsMetadata.md) | IndicatorsMetadata | `4` | `id` | — | 4 | Lentelė, kurioje yra saugomos rodiklių metaduomenys |
| [IndicatorsOb](nusikalstamumas/IndicatorsOb.md) | IndicatorsOb | `4` | `item, dt` | — | 2 | Lentelė, kurioje yra saugomos rodiklių reikšmės |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv
