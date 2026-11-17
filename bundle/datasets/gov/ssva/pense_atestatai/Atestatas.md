---
type: Table
title: "Atestatas — PENS Ekspertų Atestatai"
description: "Spinta table datasets/gov/ssva/pense_atestatai/Atestatas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Atestatas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atestatas — PENS Ekspertų Atestatai

- **Model:** `datasets/gov/ssva/pense_atestatai/Atestatas`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikavimo ekspertų kvalifikacijos atestatus (fiziniai asmenys)](../pense_atestatai.md) (`datasets/gov/ssva/pense_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/atestatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Atestatas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Kvalifikacijos atestato numeris | — |
| `gavejas` | `string` | — | `4` | `public` | — | Ekspertas | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Pirmojo atestato išdavimo data | — |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Naujausiojo atestato išdavimo data | — |
| `statusas` | `integer` | — | `4` | `open` | — | Atestato statusas | — |
| `galiojimas` | `string` | — | `2` | `open` | — | Atestato galiojimo laiko ribos (jei taikoma) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `0` | — | — | Negalioja | — |
| `statusas` | `1` | — | — | Galioja | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv
