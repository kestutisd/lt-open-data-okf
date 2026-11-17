---
type: Table
title: "FareRule — Viešojo transporto bilietų tarifų taikymo taisyklės"
description: "Viešojo transporto bilietų tarifų taikymo taisyklės pagal maršrutus ar zonas."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/FareRule"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# FareRule — Viešojo transporto bilietų tarifų taikymo taisyklės

Viešojo transporto bilietų tarifų taikymo taisyklės pagal maršrutus ar zonas. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)

- **Model:** `datasets/gov/ltsa/viesasis_transportas/FareRule`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/FareRule`
- **Primary Key (`ref`):** `fare_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fare_id` | `string` | — | `4` | `open` | — | Tarifo (bilieto) ID, kuriam taikoma ši taisyklė | — |
| `route_id` | `string` | — | `4` | `open` | — | Maršruto ID, kuriam galioja šis tarifas | — |
| `origin_id` | `string` | — | `4` | `open` | — | Pradinės zonos ID | — |
| `destination_id` | `string` | — | `4` | `open` | — | Tikslinės zonos ID | — |
| `contains_id` | `string` | — | `4` | `open` | — | Tarpinės zonos ID | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv
