---
type: Table
title: "Aircraft"
description: "Spinta table datasets/gov/rrt/aircrafts/Aircraft (11 columns)."
tags: [gov, rrt, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/aircrafts.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/aircrafts.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Aircraft

- **Model:** `datasets/gov/rrt/aircrafts/Aircraft`[^manifest]
- **Dataset:** [datasets/gov/rrt/aircrafts](../aircrafts.md) (`datasets/gov/rrt/aircrafts`)
- **Manifest CSV:** [datasets/gov/rrt/aircrafts.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/aircrafts.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `registration_no` | `string` | — | `4` | `open` | — | Orlaivio nacionalinis ir registracijos ženklai | — |
| `serial_no` | `string` | — | `4` | `open` | — | Orlaivio serijos numeris | — |
| `aircraft_model` | `string` | — | `4` | `open` | — | Orlaivio modelis | — |
| `licence_no` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `valid_from` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `valid_to` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `equipment_name` | `string` | — | `3` | `open` | — | Įrangos pavadinimas | — |
| `power` | `number` | `W` | `4` | `open` | — | Įrangos siųstuvo galia | — |
| `emission_class` | `string` | — | `3` | `open` | — | Spinduliavimo klasė | — |
| `frequency_band` | `string` | — | `3` | `open` | — | Dažnis arba dažnių juosta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/aircrafts.csv
