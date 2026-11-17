---
type: Table
title: "Gelezinkelis"
description: "Spinta table datasets/gov/rrt/gelezinkeliai/Gelezinkelis (20 columns)."
tags: [gov, rrt, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/gelezinkeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/gelezinkeliai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gelezinkelis

- **Model:** `datasets/gov/rrt/gelezinkeliai/Gelezinkelis`[^manifest]
- **Dataset:** [datasets/gov/rrt/gelezinkeliai](../gelezinkeliai.md) (`datasets/gov/rrt/gelezinkeliai`)
- **Manifest CSV:** [datasets/gov/rrt/gelezinkeliai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/gelezinkeliai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data_ir_laikas` | `datetime` | `S` | `4` | `open` | — | Data ir laikas | — |
| `platuma` | `number` | — | `3` | `open` | — | Koordinatė, ilguma | — |
| `ilguma` | `number` | — | `3` | `open` | — | Koordinatė, platuma | — |
| `koordinates_wgs` | `geometry(point)` | — | — | — | — | — | — |
| `operatorius` | `integer` | — | `4` | `open` | — | Ryšio operatorius | — |
| `cell_id` | `string` | — | `4` | `open` | — | Celės numeris | — |
| `rysio_tinklas` | `string` | — | `4` | `open` | — | Ryšio technologija | — |
| `level` | `integer` | — | `3` | `open` | — | Radijo ryšio parametras | — |
| `lterssi` | `integer` | — | `3` | `open` | — | Radijo ryšio parametras | — |
| `qual` | `integer` | — | `3` | `open` | — | Radijo ryšio parametras | — |
| `snr` | `integer` | — | `3` | `open` | — | Radijo ryšio parametras | — |
| `cqi` | `integer` | — | `3` | `open` | — | Radijo ryšio parametras | — |
| `dl_sparta` | `integer` | — | `4` | `open` | — | Duomenų perdavimo sparta, gavimas | — |
| `ul_sparta` | `integer` | — | `4` | `open` | — | Duomenų perdavimo sparta, siuntimas | — |
| `pingavg` | `integer` | — | `3` | `open` | — | Delsa, vidutinė vertė | — |
| `pingmin` | `integer` | — | `3` | `open` | — | Delsa, minimali vertė | — |
| `pingmax` | `integer` | — | `3` | `open` | — | Delsa, maksimali vertė | — |
| `pingstdev` | `integer` | — | `3` | `open` | — | Delsa, standartinis nuokrypis | — |
| `pingloss` | `integer` | — | `3` | `open` | — | Delsa, prarastų verčių dalis | — |
| `test_type` | `string` | — | `4` | `open` | — | Bandymo pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `test_type` | `"DL TEST"` | — | — | Atsisiuntimo (download) testas | — |
| `test_type` | `"UP TEST"` | — | — | Išsiuntimo (upload) testas | — |
| `test_type` | `"PING TEST"` | — | — | Ping testas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/gelezinkeliai.csv
