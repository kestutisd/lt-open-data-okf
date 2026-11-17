---
type: Table
title: "Priemone"
description: "Spinta table datasets/gov/ssva/tpv_atestatai/Priemone (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai/Priemone"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priemone

- **Model:** `datasets/gov/ssva/tpv_atestatai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie teritorijų planavimo vadovų atestatus (fiziniai asmenys)](../tpv_atestatai.md) (`datasets/gov/ssva/tpv_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai/Priemone`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `nr` | `ref` | [Atestatas](Atestatas.md) | `4` | `open` | — | Atestato numeris | — |
| `tipas` | `string` | — | `4` | `open` | — | Poveikio priemonės tipas | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pradžia | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pabaiga | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Poveikio priemonės aprašymas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Panaikintas"` | — | — | — | — |
| `tipas` | `"Sustabdytas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv
