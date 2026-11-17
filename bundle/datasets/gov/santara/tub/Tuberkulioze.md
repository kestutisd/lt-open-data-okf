---
type: Table
title: "Tuberkulioze"
description: "Spinta table datasets/gov/santara/tub/Tuberkulioze (9 columns)."
tags: [gov, santara, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/santara/tub.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tuberkulioze

- **Model:** `datasets/gov/santara/tub/Tuberkulioze`[^manifest]
- **Dataset:** [Duomenys apie tuberkuliozės atvejus](../tub.md) (`datasets/gov/santara/tub`)
- **Manifest CSV:** [datasets/gov/santara/tub.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `apskritis` | `string` | — | `3` | `open` | — | Apskritis | — |
| `pateikimo_metai` | `integer` | `yr` | `2` | `open` | — | Pateikimo metai/Vizito metai | — |
| `ketvirtis` | `string` | — | `2` | `open` | — | Ketvirtis | — |
| `vietove` | `string` | — | `4` | `open` | — | Vietovės tipas | — |
| `rukymas` | `integer` | — | `4` | `open` | — | Rūkymo statusas | — |
| `rukymo_stazas` | `integer` | — | `4` | `open` | — | Rūkymo stažas | — |
| `alkoholis` | `integer` | — | `4` | `open` | — | Alkoholio vartojimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `vietove` | `"M"` | — | — | Miestas | — |
| `vietove` | `"K"` | — | — | Kaimas | — |
| `rukymas` | `1` | — | — | Iki 10 cigarečių per dieną | — |
| `rukymas` | `2` | — | — | 11-20 cigarečių per dieną | — |
| `rukymas` | `3` | — | — | Virš 20 cigarečių per dieną | — |
| `rukymas` | `4` | — | — | Nerūko | — |
| `rukymas` | `5` | — | — | Neberūko | — |
| `rukymo_stazas` | `1` | — | — | iki 1 metų | — |
| `rukymo_stazas` | `2` | — | — | 1 - 10 metų | — |
| `rukymo_stazas` | `3` | — | — | 11 - 20 metų | — |
| `rukymo_stazas` | `4` | — | — | Virš 20 metų | — |
| `alkoholis` | `1` | — | — | Nevartoja | — |
| `alkoholis` | `2` | — | — | Vartoja retai | — |
| `alkoholis` | `3` | — | — | Girtauja | — |
| `alkoholis` | `4` | — | — | Alkoholikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/santara/tub.csv
