---
type: Table
title: "RailwayIncident — Ištirti geležinkelio eismo įvykiai"
description: "Spinta table datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident"
tags: [gov, ltsa, railwayincident, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2093/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai"
    author: "team:vda"
    last_modified: "2026-02-02T00:00:00Z"
---

# RailwayIncident — Ištirti geležinkelio eismo įvykiai

- **Model:** `datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident`[^manifest]
- **Dataset:** [Ištirti geležinkelio eismo įvykiai](../gelezinkeliu_eismo_ivykiai.md) (`datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai/RailwayIncident` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `incident_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-02-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_eismo_ivykiai (https://data.gov.lt/datasets/2093/)
