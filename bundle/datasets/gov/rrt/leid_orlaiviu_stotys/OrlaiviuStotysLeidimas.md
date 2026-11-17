---
type: Table
title: "OrlaiviuStotysLeidimas — Leidimai naudoti orlaivių stotis"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduotus leidimus naudoti orlaivių radijo ryšio įrenginių stotis."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_orlaiviu_stotys/OrlaiviuStotysLeidimas"
tags: [gov, rrt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_orlaiviu_stotys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# OrlaiviuStotysLeidimas — Leidimai naudoti orlaivių stotis

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduotus leidimus naudoti orlaivių radijo ryšio įrenginių stotis. Pateikiami tik šiuo metu galiojantys leidimai. Jie yra išduodami 5 metų laikotarpiui. Duomenys atnaujinami kasdien.

- **Model:** `datasets/gov/rrt/leid_orlaiviu_stotys/OrlaiviuStotysLeidimas`[^manifest]
- **Dataset:** [Leidimai naudoti orlaivių stotis](../leid_orlaiviu_stotys.md) (`datasets/gov/rrt/leid_orlaiviu_stotys`)
- **Manifest CSV:** [datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_orlaiviu_stotys/OrlaiviuStotysLeidimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Orlaivio nacionalinis ir registracijos ženklai | — |
| `serijos_nr` | `string` | — | `4` | `open` | — | Orlaivio serijos numeris | — |
| `lektuvo_modelis` | `string` | — | `4` | `open` | — | Orlaivio modelis | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `leidimas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `leidimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `irangos_tipas` | `string` | — | `4` | `open` | — | Įrangos pavadinimas | — |
| `irangos_galingumas_w` | `number` | `W` | `4` | `open` | — | Įrangos siųstuvo galia, W (Vatais) | — |
| `spinduliavimo_klase` | `string` | — | `4` | `open` | — | Spinduliavimo klasė | — |
| `dazniu_diapazonas` | `string` | — | `4` | `open` | — | Dažnis arba dažnių juosta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_orlaiviu_stotys.csv
