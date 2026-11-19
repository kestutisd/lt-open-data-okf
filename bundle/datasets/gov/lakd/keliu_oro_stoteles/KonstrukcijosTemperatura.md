---
type: Table
title: "KonstrukcijosTemperatura"
description: "Spinta table datasets/gov/lakd/keliu_oro_stoteles/KonstrukcijosTemperatura (3 columns)."
tags: [gov, lakd, konstrukcijostemperatura, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L96"
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliu_oro_stoteles.csv#L96"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# KonstrukcijosTemperatura

- **Model:** `datasets/gov/lakd/keliu_oro_stoteles/KonstrukcijosTemperatura`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliu_oro_stoteles](../keliu_oro_stoteles.md) (`datasets/gov/lakd/keliu_oro_stoteles`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/keliu_oro_stoteles.csv#L96](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L96)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `irenginys, kodas`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginys` | `ref` | [WeatherCondition](WeatherCondition.md) (`level=4 UUID`: `irenginys._id`) | `4` | `open` | — | — | — |
| `kodas` | `string` | — | `3` | `open` | — | — | — |
| `temperatura` | `number` | `°C` | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliu_oro_stoteles.csv#L96 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliu_oro_stoteles.csv#L96)
