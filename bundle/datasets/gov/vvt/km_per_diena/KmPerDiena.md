---
type: Table
title: "KmPerDiena — Per pamainą nuvažiuoti kilometrai"
description: "Vilniaus viešojo transporto vairuotojų per pamainą nuvažiuoti kilometrai"
resource: "https://get.data.gov.lt/datasets/gov/vvt/km_per_diena/KmPerDiena"
tags: [gov, vvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvt/km_per_diena.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvt/km_per_diena.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# KmPerDiena — Per pamainą nuvažiuoti kilometrai

Vilniaus viešojo transporto vairuotojų per pamainą nuvažiuoti kilometrai

- **Model:** `datasets/gov/vvt/km_per_diena/KmPerDiena`[^manifest]
- **Dataset:** [Vilniaus viešojo transporto vairuotojų nuvažiuoti kilometrai](../km_per_diena.md) (`datasets/gov/vvt/km_per_diena`)
- **Manifest CSV:** [datasets/gov/vvt/km_per_diena.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvt/km_per_diena.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvt/km_per_diena/KmPerDiena`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `vairuotojo_id` | `string` | — | `4` | `open` | — | Vairuotojo identifikatorius | — |
| `pamainos_numeris` | `string` | — | `4` | `open` | — | Darbo grafiko identifikatorius | — |
| `darbo_pradzia` | `datetime` | `S` | `4` | `open` | — | Darbo pradžia | — |
| `darbo_pabaiga` | `datetime` | `S` | `4` | `open` | — | Darbo pabaiga | — |
| `vt_tipas` | `string` | — | `4` | `open` | — | Viešojo transporto tipas | — |
| `tp_garazinis_nr` | `string` | — | `4` | `open` | — | Transporto priemonės garažinis numeris | — |
| `tp_gamintojas` | `string` | — | `4` | `open` | — | Transporto priemonės gamintojo pavadinimas | — |
| `tp_modelis` | `string` | — | `4` | `open` | — | Transporto priemonės modelis | — |
| `marsruto_id` | `string` | — | `4` | `open` | — | Maršruto identifikatorius | — |
| `marsruto_nr` | `string` | — | `4` | `open` | — | Maršruto numeris | — |
| `reisu_sk` | `integer` | — | `4` | `open` | — | Planuotų reisų skaičius | — |
| `km` | `number` | — | `4` | `open` | — | Nuvažiuotų kilometrų kiekis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pamainos_numeris` | `"1D"` | — | — | "1D" - pirma pamaina | — |
| `pamainos_numeris` | `"2D"` | — | — | "2D" - antra pamaina | — |
| `pamainos_numeris` | `"3D"` | — | — | "3D" - trečia pamaina | — |
| `pamainos_numeris` | `"4D"` | — | — | "4D" - ketvirta pamaina | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvt/km_per_diena.csv
