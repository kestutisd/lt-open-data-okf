---
type: Table
title: "Priemone — Poveikio priemonės"
description: "Spinta table datasets/gov/ssva/vadovu_atestatai/Priemone (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/vadovu_atestatai/Priemone"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priemone — Poveikio priemonės

- **Model:** `datasets/gov/ssva/vadovu_atestatai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos techninės veiklos pagrindinių sričių vadovų kvalifikacijos atestatus ir teisės pripažinimo dokumentus (fiziniai asmenys)](../vadovu_atestatai.md) (`datasets/gov/ssva/vadovu_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/vadovu_atestatai/Priemone`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Poveikio priemonės ID | — |
| `nr` | `ref` | [Atestatas](Atestatas.md) | `4` | `open` | — | Teisės dokumento numeris | — |
| `spr_nr` | `integer` | — | `4` | `open` | — | Sprendimo dėl poveikio taikymo numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Sprendimo dėl poveikio taikymo data | — |
| `tipas` | `integer` | — | `4` | `open` | — | Poveikio priemonės tipas | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pradžia | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pabaiga | — |
| `aprasas` | `string` | — | `4` | `open` | — | Poveikio priemonės aprašymas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `1` | — | — | Panaikintas | — |
| `tipas` | `2` | — | — | Sustabdytas | — |
| `tipas` | `3` | — | — | Stabdyti | — |
| `tipas` | `4` | — | — | Įspėjimas | — |
| `tipas` | `5` | — | — | Pastaba | — |
| `tipas` | `6` | — | — | Įspėti | — |
| `tipas` | `7` | — | — | Atšauktas panaikinimas | — |
| `tipas` | `8` | — | — | Atšaukimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv
