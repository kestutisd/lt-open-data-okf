---
type: Table
title: "VandensMatavimoStotis"
description: "Spinta table datasets/gov/lhmt/hidrologija/VandensMatavimoStotis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/hidrologija/VandensMatavimoStotis"
tags: [gov, lhmt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lhmt/hidrologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/hidrologija.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VandensMatavimoStotis

- **Model:** `datasets/gov/lhmt/hidrologija/VandensMatavimoStotis`[^manifest]
- **Dataset:** [datasets/gov/lhmt/hidrologija](../hidrologija.md) (`datasets/gov/lhmt/hidrologija`)
- **Manifest CSV:** [datasets/gov/lhmt/hidrologija.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/hidrologija.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/hidrologija/VandensMatavimoStotis`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vms` | `string` | — | `3` | `open` | — | vandens matavimo stotis | — |
| `vand_telk_pvd` | `string` | — | `3` | `open` | — | vandens telkinio pavadinimas | — |
| `ats_nuo_ziociu` | `number` | — | `3` | `open` | — | atstumas nuo žiočių, km | — |
| `koord` | `geometry(point,4326)` | `m` | `4` | `open` | — | vandens matavimo stoties koordinatės (WGS) | — |
| `isteigta` | `integer` | — | `3` | `open` | — | vandens matavimo stoties įsteigimo metai | — |
| `vand_telk_tipas` | `string` | — | `3` | `open` | — | vandens telkinio tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/hidrologija.csv
