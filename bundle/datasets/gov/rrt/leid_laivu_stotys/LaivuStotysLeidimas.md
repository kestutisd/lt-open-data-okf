---
type: Table
title: "LaivuStotysLeidimas — Leidimai naudoti laivų stotis"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti laivų radijo ryšio įrenginių stotis."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_laivu_stotys/LaivuStotysLeidimas"
tags: [gov, rrt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_laivu_stotys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_laivu_stotys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaivuStotysLeidimas — Leidimai naudoti laivų stotis

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti laivų radijo ryšio įrenginių stotis. Pateikiami tik šiuo metu galiojantys leidimai. Jie yra išduodami 5 metų laikotarpiui. Duomenys atnaujinami kasdien.

- **Model:** `datasets/gov/rrt/leid_laivu_stotys/LaivuStotysLeidimas`[^manifest]
- **Dataset:** [Leidimai naudoti laivų stotis](../leid_laivu_stotys.md) (`datasets/gov/rrt/leid_laivu_stotys`)
- **Manifest CSV:** [datasets/gov/rrt/leid_laivu_stotys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_laivu_stotys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_laivu_stotys/LaivuStotysLeidimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `laivo_pavadinimas` | `string` | — | `4` | `open` | — | Laivo pavadinimas arba registro numeris | — |
| `laivo_saukinys` | `string` | — | `4` | `open` | — | Šaukinys | — |
| `laivo_mmsi` | `string` | — | `4` | `open` | — | MMSI numeris | — |
| `laivo_sel_nr` | `string` | — | `4` | `open` | — | Atrankiojo kvietimo numeris | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `leidimas_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `leidimas_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `irangos_pavadinimas` | `string` | — | `4` | `open` | — | Įrangos pavadinimas | — |
| `irangos_galia_w` | `number` | `W` | `4` | `open` | — | Įrangos siųstuvo galia, W (Vatais) | — |
| `spinduliavimo_klase` | `string` | — | `4` | `open` | — | Spinduliavimo klasė | — |
| `suteikti_dazniai` | `string` | — | `4` | `open` | — | Dažnis arba dažnių juosta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_laivu_stotys.csv
