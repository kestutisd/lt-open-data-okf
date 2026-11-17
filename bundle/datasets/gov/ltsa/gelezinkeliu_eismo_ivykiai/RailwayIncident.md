---
type: Table
title: "RailwayIncident — Ištirti geležinkelio eismo įvykiai"
description: "Spinta table datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# RailwayIncident — Ištirti geležinkelio eismo įvykiai

- **Model:** `datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident`[^manifest]
- **Dataset:** [Ištirti geležinkelio eismo įvykiai](../gelezinkeliu_eismo_ivykiai.md) (`datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai`)
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident`
- **Primary Key (`ref`):** `incident_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `incident_id` | `integer` | — | `4` | `open` | — | Įvykio ID | — |
| `incident` | `string` | — | `4` | `open` | — | Įvykio laikas | — |
| `infrastructure_manager` | `string` | — | `4` | `open` | — | Infrastruktūros valdytojas | — |
| `line_station_a` | `string` | — | `4` | `open` | — | Tarpstočio stotis A | Įvykio vieta - tarpstotis |
| `line_station_b` | `string` | — | `4` | `open` | — | Tarpstočio stotis B | Įvykio vieta - tarpstotis |
| `casualties` | `string` | — | `4` | `open` | — | Pasėkmės žmogaus sveikatai | — |
| `station` | `string` | — | `4` | `open` | — | Stotis | Įvykio vieta - stotis |
| `type` | `string` | — | `4` | `open` | — | Įvykio tipas | — |
| `railway_untertaking` | `string` | — | `4` | `open` | — | Vežėjas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv
