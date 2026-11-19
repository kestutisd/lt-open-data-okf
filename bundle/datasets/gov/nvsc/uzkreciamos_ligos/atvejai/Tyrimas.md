---
type: Table
title: "Tyrimas — Užkrečiamųjų ligų tyrimai"
description: "Spinta table datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas"
tags: [gov, nvsc, tyrimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124"
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1852/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nvsc/uzkreciamos_ligos/atvejai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Tyrimas — Užkrečiamųjų ligų tyrimai

- **Model:** `datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas`[^manifest]
- **Dataset:** [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys](../atvejai.md) (`datasets/gov/nvsc/uzkreciamos_ligos/atvejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Tyrimas` (`deployed`)[^manifest]
- **Provider:** `nvsc` — Nacionalinis visuomenės sveikatos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patvirtinta` | `date` | `M` | `4` | `open` | — | Diagnozės data | — |
| `tlk` | `ref` | [Tlk10am](../../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `tlk._id`) | `4` | `open` | — | Galutinės diagnozės kodas | — |
| `galutine_diagnoze` | `string` | — | `4` | `open` | — | Galutinė diagnozė | — |
| `laboratoriniai_tyrimai` | `string` | — | `2` | `open` | — | Laboratoriniai tyrimai | — |
| `laboratoriniu_tyrimu_metodai` | `string` | — | `2` | `open` | — | Laboratorinių tyrimų metodai | — |
| `apibr_atitinka_standartini` | `boolean` | — | `4` | `open` | — | Standartinis | Požymis ar laboratorinio tyrimo metodas yra standartinis |
| `atvejai` | `integer` | `U` | `4` | `open` | — | Atvejų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L124)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nvsc/uzkreciamos_ligos/atvejai (https://data.gov.lt/datasets/1852/)
