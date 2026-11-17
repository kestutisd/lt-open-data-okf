---
type: Table
title: "SKLiga"
description: "Spinta table datasets/gov/santara/skl/SKLiga (13 columns)."
tags: [gov, santara, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/santara/skl.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/skl.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# SKLiga

- **Model:** `datasets/gov/santara/skl/SKLiga`[^manifest]
- **Dataset:** [Širdies ir kraujagyslių ligomis sergančių pacientų apsilankymų statistiniai duomenys](../skl.md) (`datasets/gov/santara/skl`)
- **Manifest CSV:** [datasets/gov/santara/skl.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/skl.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `apskritis` | `string` | — | `3` | `open` | — | Apskritis | — |
| `pateikimo_metai` | `integer` | `yr` | `2` | `open` | — | Pateikimo metai | — |
| `ketvirtis` | `string` | — | `2` | `open` | — | Ketvirtis | — |
| `ugis` | `string` | — | `3` | `open` | — | Ūgis | — |
| `svoris` | `string` | — | `3` | `open` | — | Svoris | — |
| `juosmuo` | `string` | — | `3` | `open` | — | Juosmuo | — |
| `saks` | `integer` | — | `4` | `open` | — | Sistolinis arterinis kraujo spaudimas | — |
| `daks` | `integer` | — | `4` | `open` | — | Diastolinis arterinis kraujo spaudimas | — |
| `rukymas` | `integer` | — | `4` | `open` | — | Rūkymo statusas | — |
| `fizinis_aktyvumas` | `string` | — | `4` | `open` | — | Fizinis aktyvumas | — |
| `mityba` | `string` | — | `4` | `open` | — | Mityba | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `rukymas` | `1` | — | — | Rūko | — |
| `rukymas` | `2` | — | — | Nerūko | — |
| `fizinis_aktyvumas` | `"Aktyvus"` | — | — | Fiziškai aktyvus | — |
| `fizinis_aktyvumas` | `"Neaktyvus"` | — | — | Fiziškai neaktyvus | — |
| `mityba` | `"Subalansuota"` | — | — | Subalansuota mityba | — |
| `mityba` | `"Nesubalansuota"` | — | — | Nesubalansuota mityba | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/santara/skl.csv
