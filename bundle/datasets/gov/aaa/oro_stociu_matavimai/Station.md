---
type: Table
title: "Station — Oro kokybės matavimo stotys"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Station (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Station — Oro kokybės matavimo stotys

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Station`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Station`
- **Primary Key (`ref`):** `stat_num`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `stat_num` | `string` | — | `4` | `open` | — | Matavimo stoties identifikacinis numeris | — |
| `latitude` | `number` | — | `3` | `open` | — | Geografinė platuma (WGS) | — |
| `longitude` | `number` | — | `3` | `open` | — | Geografinė ilguma (WGS) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv
