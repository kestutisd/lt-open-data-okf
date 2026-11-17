---
type: Table
title: "KonstrukcijosTemperatura"
description: "Spinta table datasets/gov/lakd/keliu_oro_stoteles/KonstrukcijosTemperatura (3 columns)."
tags: [gov, lakd, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliu_oro_stoteles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L96"
    last_modified: "2026-11-11T14:39:20Z"
---

# KonstrukcijosTemperatura

- **Model:** `datasets/gov/lakd/keliu_oro_stoteles/KonstrukcijosTemperatura`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliu_oro_stoteles](../keliu_oro_stoteles.md) (`datasets/gov/lakd/keliu_oro_stoteles`)
- **Manifest CSV:** [datasets/gov/lakd/keliu_oro_stoteles.csv#L96](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L96)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `irenginys, kodas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginys` | `ref` | [WeatherCondition](WeatherCondition.md) | `4` | `open` | — | — | — |
| `kodas` | `string` | — | `3` | `open` | — | — | — |
| `temperatura` | `number` | `°C` | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliu_oro_stoteles.csv
