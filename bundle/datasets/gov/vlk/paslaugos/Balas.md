---
type: Table
title: "Balas — Bazinių kainų balais sąrašas"
description: "Asmens sveikatos priežiūros paslaugų bazinių balų sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/paslaugos/Balas"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# Balas — Bazinių kainų balais sąrašas

Asmens sveikatos priežiūros paslaugų bazinių balų sąrašas

- **Model:** `datasets/gov/vlk/paslaugos/Balas`[^manifest]
- **Dataset:** [datasets/gov/vlk/paslaugos](../paslaugos.md) (`datasets/gov/vlk/paslaugos`)
- **Manifest CSV:** [datasets/gov/vlk/paslaugos.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/paslaugos/Balas`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paslauga` | `ref` | [Paslauga](Paslauga.md) | `4` | `open` | — | Nuoroda į paslaugas | — |
| `lovadieniui` | `number` | — | `4` | `open` | — | Balai lovadieniui | — |
| `atvejui` | `number` | — | `4` | `open` | — | Balai atvejui | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | — |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | — |
| `verte` | `number` | — | `4` | `open` | — | Bazinio balo vertė | — |
| `trukme` | `integer` | `U` | `4` | `open` | — | Vidutinė paslaugos trukmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv
