---
type: Table
title: "OrlaiviuStotysLeidimas — Leidimai naudoti orlaivių stotis"
description: "\"Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduotus leidimus naudoti orlaivių radijo ryšio įrenginių stotis."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_orlaiviu_stotys/OrlaiviuStotysLeidimas"
tags: [gov, rrt, orlaiviustotysleidimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2730/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rrt/leid_orlaiviu_stotys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# OrlaiviuStotysLeidimas — Leidimai naudoti orlaivių stotis

"Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduotus leidimus naudoti orlaivių radijo ryšio įrenginių stotis. Pateikiami tik šiuo metu galiojantys leidimai. Jie yra išduodami 5 metų laikotarpiui. Duomenys atnaujinami kasdien."[^manifest]

- **Model:** `datasets/gov/rrt/leid_orlaiviu_stotys/OrlaiviuStotysLeidimas`[^manifest]
- **Dataset:** [Leidimai naudoti orlaivių stotis](../leid_orlaiviu_stotys.md) (`datasets/gov/rrt/leid_orlaiviu_stotys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_orlaiviu_stotys/OrlaiviuStotysLeidimas` (`deployed`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `irangos_galingumas_w` | `number` | `W` | `4` | `open` | — | "Įrangos siųstuvo galia, W (Vatais)" | — |
| `spinduliavimo_klase` | `string` | — | `4` | `open` | — | Spinduliavimo klasė | — |
| `dazniu_diapazonas` | `string` | — | `4` | `open` | — | Dažnis arba dažnių juosta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_orlaiviu_stotys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rrt/leid_orlaiviu_stotys (https://data.gov.lt/datasets/2730/)
