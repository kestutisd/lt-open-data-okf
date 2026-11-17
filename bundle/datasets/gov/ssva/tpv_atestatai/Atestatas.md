---
type: Table
title: "Atestatas — Teritorijų planavimo vadovų atestatai"
description: "Spinta table datasets/gov/ssva/tpv_atestatai/Atestatas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai/Atestatas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atestatas — Teritorijų planavimo vadovų atestatai

- **Model:** `datasets/gov/ssva/tpv_atestatai/Atestatas`[^manifest]
- **Dataset:** [Duomenys apie teritorijų planavimo vadovų atestatus (fiziniai asmenys)](../tpv_atestatai.md) (`datasets/gov/ssva/tpv_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai/Atestatas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Atestato numeris | — |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Atestato atnaujinimo data | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Atestato galiojimo pabaiga | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Pirmojo atestato išdavimo data | — |
| `gavejas` | `string` | — | `4` | `public` | — | Teritorijų planavimo vadovas | — |
| `planavimo_dok` | `string` | — | `3` | `open` | — | Kompleksinio teritorijų planavimo dokumentų rūšys | — |
| `spec_planavimo_dok` | `string` | — | `3` | `open` | — | Specialiojo teritorijų planavimo dokumentų rūšys | — |
| `vertinimas` | `date` | `D` | `4` | `open` | — | Kvalifikacijos įvertinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv
