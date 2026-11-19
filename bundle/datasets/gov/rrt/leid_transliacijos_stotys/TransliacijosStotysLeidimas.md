---
type: Table
title: "TransliacijosStotysLeidimas — Transliacijos stočių leidimai"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos)."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys/TransliacijosStotysLeidimas"
tags: [gov, rrt, transliacijosstotysleidimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_transliacijos_stotys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2729/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rrt/leid_transliacijos_stotys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TransliacijosStotysLeidimas — Transliacijos stočių leidimai

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos). Rinkinyje naudojamos WGS koordinatės, nurodančios antenos lokaciją. Pateikiami tik šiuo metu galiojantys leidimai. Duomenys atnaujinami kasdien.[^manifest]

- **Model:** `datasets/gov/rrt/leid_transliacijos_stotys/TransliacijosStotysLeidimas`[^manifest]
- **Dataset:** [Transliacijos stočių leidimai](../leid_transliacijos_stotys.md) (`datasets/gov/rrt/leid_transliacijos_stotys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/leid_transliacijos_stotys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys/TransliacijosStotysLeidimas` (`deployed`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `transliavimo_sistemos_tipas` | `"RADIO"` | — | — | Garso transliacija | — |
| `transliavimo_sistemos_tipas` | `"DVB"` | — | — | Skaitmeninio vaizdo transliacija | — |
| `transliavimo_sistemos_tipas` | `"DAB"` | — | — | Skaitmeninio garso transliacija | — |
| `leidimo_tipas` | `"Analoginio radijo dažniui"` | — | — | Leidimas analoginio radijo dažniui | — |
| `leidimo_tipas` | `"Skaitmeninės televizijos kanalui / stočiai"` | — | — | Leidimas skaitmeninės televizijos kanalui / stočiai | — |
| `leidimo_tipas` | `"Skaitmeninio radijo blokui"` | — | — | Leidimas Skaitmeninio radijo blokui | — |
| `antenos_poliarizacija` | `"H"` | — | — | Horizontali poliarizacija | — |
| `antenos_poliarizacija` | `"V"` | — | — | Vertikali poliarizacija | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_transliacijos_stotys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rrt/leid_transliacijos_stotys (https://data.gov.lt/datasets/2729/)
