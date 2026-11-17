---
type: Table
title: "Trip — Reisas"
description: "Spinta table datasets/gov/sumin/vintra/Trip (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sumin/vintra/Trip"
tags: [gov, sumin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sumin/vintra.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# Trip — Reisas

- **Model:** `datasets/gov/sumin/vintra/Trip`[^manifest]
- **Dataset:** [datasets/gov/sumin/vintra](../vintra.md) (`datasets/gov/sumin/vintra`)
- **Manifest CSV:** [datasets/gov/sumin/vintra.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sumin/vintra/Trip`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency` | `ref` | [Agency](Agency.md) | `4` | `open` | — | Paslaugų teikėjas | — |
| `trip_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `start_time` | `time` | — | `3` | `open` | — | Pradžios laikas | — |
| `route` | `string` | — | `4` | `open` | — | Maršruto numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sumin/vintra.csv
