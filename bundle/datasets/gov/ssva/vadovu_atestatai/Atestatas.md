---
type: Table
title: "Atestatas — Statinio statybos techninės veiklos pagrindinių sričių vadovų kvalifikacijos atestatų ir teisės pripažinimo dokumentų registras"
description: "Spinta table datasets/gov/ssva/vadovu_atestatai/Atestatas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/vadovu_atestatai/Atestatas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atestatas — Statinio statybos techninės veiklos pagrindinių sričių vadovų kvalifikacijos atestatų ir teisės pripažinimo dokumentų registras

- **Model:** `datasets/gov/ssva/vadovu_atestatai/Atestatas`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos techninės veiklos pagrindinių sričių vadovų kvalifikacijos atestatus ir teisės pripažinimo dokumentus (fiziniai asmenys)](../vadovu_atestatai.md) (`datasets/gov/ssva/vadovu_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/vadovu_atestatai/Atestatas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo ID | — |
| `nr` | `integer` | — | `4` | `open` | — | Teisės dokumento numeris | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Teisės dokumento išdavimo data | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Teisės dokumento galiojimo pabaiga | — |
| `registruota` | `date` | `D` | `4` | `open` | — | Pirmoji teisės dokumento išdavimo data | — |
| `gavejas` | `string` | — | `4` | `public` | — | Vardas Pavardė | Atestato savininkas |
| `pareigos` | `string` | — | `3` | `open` | — | Suteikta arba pripažinta teisė - pareigos | — |
| `statusas` | `string` | — | `3` | `open` | — | Suteikta arba pripažinta teisė - statinių grupės, darbo sritys ir kt. | — |
| `tipas` | `string` | — | `4` | `open` | — | Teisės dokumento tipas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pripažinas teisės dokumentas | — |
| `vertinimas` | `date` | `D` | `4` | `open` | — | Kvalifikacijos įvertinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"KA"` | — | — | Kvalifikacijos atestatas | — |
| `tipas` | `"TPD"` | — | — | Teisės pripažinimo dokumentas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/vadovu_kvalifikacijos_atestatai.csv
