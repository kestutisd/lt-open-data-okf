---
type: Table
title: "Korekcija — Atestavimo veiksmų istoriniai įrašai"
description: "Spinta table datasets/gov/ssva/pense_atestatai/Korekcija (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Korekcija"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Korekcija — Atestavimo veiksmų istoriniai įrašai

- **Model:** `datasets/gov/ssva/pense_atestatai/Korekcija`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikavimo ekspertų kvalifikacijos atestatus (fiziniai asmenys)](../pense_atestatai.md) (`datasets/gov/ssva/pense_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/atestatai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Korekcija`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `ref` | [Atestatas](Atestatas.md) | `4` | `open` | — | Kvalifikacijos atestato numeris | — |
| `veiksmas` | `integer` | — | `4` | `open` | — | Atestavimo etapas ar poveikio priemonė | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Atestavimo etapo ar poveikio priemonės pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Atestavimo etapo ar poveikio priemonės pabaiga | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `1` | — | — | Išduotas neriboto galiojimo atestatas | — |
| `veiksmas` | `2` | — | — | Išduotas riboto galiojimo atestatas | — |
| `veiksmas` | `3` | — | — | Atestato galiojimas patvirtintas | — |
| `veiksmas` | `4` | — | — | Nepatvirtintas atestato galiojimas | — |
| `veiksmas` | `5` | — | — | Pratęstas riboto galiojimo atestatas | — |
| `veiksmas` | `6` | — | — | Ekspertui pareikštas įspėjimas | — |
| `veiksmas` | `7` | — | — | Atestato galiojimas laikinai sustabdytas | — |
| `veiksmas` | `8` | — | — | Atestato galiojimas panaikintas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv
