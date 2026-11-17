---
type: Table
title: "MeteorologineAikstele"
description: "Spinta table datasets/gov/lhmt/klimatologija/MeteorologineAikstele (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/klimatologija/MeteorologineAikstele"
tags: [gov, lhmt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lhmt/klimatologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/klimatologija.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# MeteorologineAikstele

- **Model:** `datasets/gov/lhmt/klimatologija/MeteorologineAikstele`[^manifest]
- **Dataset:** [datasets/gov/lhmt/klimatologija](../klimatologija.md) (`datasets/gov/lhmt/klimatologija`)
- **Manifest CSV:** [datasets/gov/lhmt/klimatologija.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/klimatologija.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/klimatologija/MeteorologineAikstele`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `meteorologines_aikst_adr` | `string` | — | `3` | `open` | — | Meteorologinės aikštelės adresas | — |
| `mat_stotis` | `string` | — | `3` | `open` | — | Matavimo stoties pavadinimas | — |
| `aukst_virs_jur_lygio` | `number` | — | `3` | `open` | — | Vandens aukštis virš jūros lygio | — |
| `koord` | `geometry(point,4326)` | `m` | `4` | `open` | — | Meteorologinės aikštelės koordinatės (WGS) | — |
| `isteigta` | `integer` | — | `3` | `open` | — | Matavimo stoties įsteigimo metai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/klimatologija.csv
