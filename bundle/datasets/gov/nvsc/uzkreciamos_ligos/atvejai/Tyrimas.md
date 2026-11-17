---
type: Table
title: "Tyrimas — Užkrečiamųjų ligų tyrimai"
description: "Spinta table datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas"
tags: [gov, nvsc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tyrimas — Užkrečiamųjų ligų tyrimai

- **Model:** `datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas`[^manifest]
- **Dataset:** [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys](../atvejai.md) (`datasets/gov/nvsc/uzkreciamos_ligos/atvejai`)
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patvirtinta` | `date` | `M` | `4` | `open` | — | Diagnozės data | — |
| `tlk` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Galutinės diagnozės kodas | — |
| `galutine_diagnoze` | `string` | — | `4` | `open` | — | Galutinė diagnozė | — |
| `laboratoriniai_tyrimai` | `string` | — | `2` | `open` | — | Laboratoriniai tyrimai | — |
| `laboratoriniu_tyrimu_metodai` | `string` | — | `2` | `open` | — | Laboratorinių tyrimų metodai | — |
| `apibr_atitinka_standartini` | `boolean` | — | `4` | `open` | — | Standartinis | Požymis ar laboratorinio tyrimo metodas yra standartinis |
| `atvejai` | `integer` | `U` | `4` | `open` | — | Atvejų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv
