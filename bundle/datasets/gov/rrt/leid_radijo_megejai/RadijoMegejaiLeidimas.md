---
type: Table
title: "RadijoMegejaiLeidimas — Radijo mėgėjams išduoti leidimai"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai radijo mėgėjams užsiimti radijo mėgėjų veikla ir leidimai naudoti radijo šaukinius."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_radijo_megejai/RadijoMegejaiLeidimas"
tags: [gov, rrt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_radijo_megejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_radijo_megejai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# RadijoMegejaiLeidimas — Radijo mėgėjams išduoti leidimai

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai radijo mėgėjams užsiimti radijo mėgėjų veikla ir leidimai naudoti radijo šaukinius. Pateikiami tik šiuo metu galiojantys leidimai. Jie yra išduodami 10 metų laikotarpiui, išskyrus laikinus leidimus radijo mėgėjų veiklai ir leidimus naudoti proginį radijo šaukinį. Išduodant papildomą leidimą naudoti radijo šaukinį, terminas negali būti ilgesnis, nei nurodytas leidime užsiimti radijo mėgėjų veikla. Duomenys atnaujinami kasdien.

- **Model:** `datasets/gov/rrt/leid_radijo_megejai/RadijoMegejaiLeidimas`[^manifest]
- **Dataset:** [Radijo mėgėjams išduoti leidimai](../leid_radijo_megejai.md) (`datasets/gov/rrt/leid_radijo_megejai`)
- **Manifest CSV:** [datasets/gov/rrt/leid_radijo_megejai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_radijo_megejai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_radijo_megejai/RadijoMegejaiLeidimas`
- **Primary Key (`ref`):** `licenzijos_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licenzijos_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `licenzijos_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `saukinys` | `string` | — | `4` | `open` | — | Šaukinys | — |
| `leidimo_klase` | `string` | — | `4` | `open` | — | CERT klasė | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas (klubui arba asmeniui) | — |
| `leid_galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `licenzijos_tipas` | `"A klasės leidimas užsiimti radijo mėgėjų veikla"` | — | — | A klasės leidimas užsiimti radijo mėgėjų veikla | — |
| `licenzijos_tipas` | `"B klasės leidimas užsiimti radijo mėgėjų veikla"` | — | — | B klasės leidimas užsiimti radijo mėgėjų veikla | — |
| `licenzijos_tipas` | `"Leidimas naudoti radijo šaukinį"` | — | — | Leidimas naudoti radijo šaukinį | — |
| `licenzijos_tipas` | `"Leidimas naudoti proginį radijo šaukinį"` | — | — | Leidimas naudoti proginį radijo šaukinį | — |
| `leidimo_tipas` | `"Individualus"` | — | — | Individualus leidimas | — |
| `leidimo_tipas` | `"Klubinis"` | — | — | Klubinis leidimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_radijo_megejai.csv
