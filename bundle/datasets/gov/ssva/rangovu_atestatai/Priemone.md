---
type: Table
title: "Priemone — Poveikio priemonės"
description: "Spinta table datasets/gov/ssva/rangovu_atestatai/Priemone (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Priemone"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priemone — Poveikio priemonės

- **Model:** `datasets/gov/ssva/rangovu_atestatai/Priemone`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos ir ekspertizės rangovų atestatus, apie statinio statybos, ekspertizės rangovų ir projektuotojų teisės pripažinimo dokumentus (juridiniai asmenys)](../rangovu_atestatai.md) (`datasets/gov/ssva/rangovu_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Priemone`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus ID | — |
| `dok_id` | `ref` | [Dokumentas](Dokumentas.md) | `4` | `open` | — | Teisės dokumento ID | — |
| `nr` | `string` | — | `4` | `open` | — | Sprendimo dėl poveikio taikymo numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Sprendimo dėl poveikio taikymo data | — |
| `tipas` | `string` | — | `4` | `open` | — | Poveikio priemonės tipas | — |
| `registruota` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pradžia | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Poveikio priemonės taikymo pabaiga | — |
| `tekstas` | `string` | — | `4` | `open` | — | Poveikio priemonės aprašymas | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastaba dėl poveikio priemonės taikymo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Naikinimas"` | — | — | — | — |
| `tipas` | `"Stabdymas"` | — | — | — | — |
| `tipas` | `"Įspejimas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv
