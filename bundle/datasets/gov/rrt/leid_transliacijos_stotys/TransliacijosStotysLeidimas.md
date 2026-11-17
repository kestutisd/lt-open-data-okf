---
type: Table
title: "TransliacijosStotysLeidimas — Transliacijos stočių leidimai"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos)."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys/TransliacijosStotysLeidimas"
tags: [gov, rrt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_transliacijos_stotys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TransliacijosStotysLeidimas — Transliacijos stočių leidimai

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos). Rinkinyje naudojamos WGS koordinatės, nurodančios antenos lokaciją. Pateikiami tik šiuo metu galiojantys leidimai. Duomenys atnaujinami kasdien.

- **Model:** `datasets/gov/rrt/leid_transliacijos_stotys/TransliacijosStotysLeidimas`[^manifest]
- **Dataset:** [Transliacijos stočių leidimai](../leid_transliacijos_stotys.md) (`datasets/gov/rrt/leid_transliacijos_stotys`)
- **Manifest CSV:** [datasets/gov/rrt/leid_transliacijos_stotys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys/TransliacijosStotysLeidimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `leidimo_turetojas` | `string` | — | `4` | `open` | — | Leidimo turėtojo pavadinimas | — |
| `transliavimo_sistemos_tipas` | `string` | — | `4` | `open` | — | Transliavimo sistemos tipas | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `leidimas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Atrankiojo kvietimo numeris | — |
| `leidimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `centrinis_siustuvo_daznis_mhz` | `number` | `mHz` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `kanalo_plotis_mhz` | `number` | `mHz` | `4` | `open` | — | Centrinis siųstuvo dažnis, Mhz | — |
| `kanalo_nr` | `string` | — | `4` | `open` | — | Kanalo plotis, Mhz | — |
| `antenos_aukstis_m` | `number` | `m` | `4` | `open` | — | Antenos aukštis virš žemės lygio, m | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Antenos ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Antenos platumos koordinatė WGS84 koordinačių sistemoje | — |
| `antenos_koordinate` | `geometry(point, 4326)` | — | `4` | `open` | — | Antenos koordinatė | — |
| `maks_spind_galia_erp_dbw` | `number` | — | `4` | `open` | — | Maksimali spinduliavimo galia ERP | — |
| `antenos_poliarizacija` | `string` | — | `4` | `open` | — | Antenos poliarizacija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `transliavimo_sistemos_tipas` | `"RADIO"` | — | — | Garso transliacija | — |
| `transliavimo_sistemos_tipas` | `"DVB"` | — | — | Skaitmeninio vaizdo transliacija | — |
| `transliavimo_sistemos_tipas` | `"DAB"` | — | — | Skaitmeninio garso transliacija | — |
| `leidimo_tipas` | `"Analoginio radijo dažniui"` | — | — | Leidimas analoginio radijo dažniui | — |
| `leidimo_tipas` | `"Skaitmeninės televizijos kanalui / stočiai"` | — | — | Leidimas skaitmeninės televizijos kanalui / stočiai | — |
| `leidimo_tipas` | `"Skaitmeninio radijo blokui"` | — | — | Leidimas Skaitmeninio radijo blokui | — |
| `antenos_poliarizacija` | `"H"` | — | — | Horizontali poliarizacija | — |
| `antenos_poliarizacija` | `"V"` | — | — | Vertikali poliarizacija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_transliacijos_stotys.csv
