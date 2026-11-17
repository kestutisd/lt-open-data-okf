---
type: Table
title: "MotersVardas — Populiariausi moterų vardai Lietuvoje nuo 1900 metų, TOP 50"
description: "Spinta table datasets/gov/rc/gr/moteru_vardai/MotersVardas (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/moteru_vardai/MotersVardas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/moteru_vardai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/moteru_vardai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# MotersVardas — Populiariausi moterų vardai Lietuvoje nuo 1900 metų, TOP 50

- **Model:** `datasets/gov/rc/gr/moteru_vardai/MotersVardas`[^manifest]
- **Dataset:** [Populiariausi moterų vardai Lietuvoje nuo 1900 metų, TOP 50](../moteru_vardai.md) (`datasets/gov/rc/gr/moteru_vardai`)
- **Manifest CSV:** [datasets/gov/rc/gr/moteru_vardai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/moteru_vardai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/moteru_vardai/MotersVardas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `vardas` | `string` | — | `3` | `open` | — | Moters vardas | — |
| `viso_vardas` | `integer` | `U` | `4` | `open` | — | Moterų, gimusių nuo 1900 m. ir kurioms suteiktas toks vardas, skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/moteru_vardai.csv
