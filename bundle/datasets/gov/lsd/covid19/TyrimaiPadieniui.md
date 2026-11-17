---
type: Table
title: "TyrimaiPadieniui — COVID-19 tyrimai padieniui pagal laboratorijas"
description: "SARS-CoV-2 laboratorinių tyrimų atsakymų agreguoti pagal datą ir laboratoriją duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/TyrimaiPadieniui"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L122"
    last_modified: "2026-11-11T14:39:20Z"
---

# TyrimaiPadieniui — COVID-19 tyrimai padieniui pagal laboratorijas

SARS-CoV-2 laboratorinių tyrimų atsakymų agreguoti pagal datą ir laboratoriją duomenys

- **Model:** `datasets/gov/lsd/covid19/TyrimaiPadieniui`[^manifest]
- **Dataset:** [datasets/gov/lsd/covid19](../covid19.md) (`datasets/gov/lsd/covid19`)
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L122](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L122)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/TyrimaiPadieniui`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lab_name` | `string` | — | `2` | `open` | — | Laboratorijos, atlikusios diagnostinius tyrimus, pavadinimas | — |
| `test_performed` | `date` | `D` | `4` | `open` | — | Diagnostinių laboratorinių tyrimų atlikimo data | — |
| `test_type` | `integer` | — | `4` | `open` | — | Diagnostinių tyrimų tipai | — |
| `tests_positive` | `integer` | `U` | `4` | `open` | — | Teigiamų atsakymų skaičius (virusas aptiktas) | — |
| `tests_negative` | `integer` | `U` | `4` | `open` | — | Neigiamų atsakymų skaičius (virusas neaptiktas) | — |
| `gmp_indication` | `string` | — | `3` | `open` | — | Priežastis, dėl kurios asmuo registravosi tyrimui (nuo 2022-05-01 nebeskelbiama) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `test_type` | `1477` | — | — | PGR testas | — |
| `test_type` | `1537` | — | — | PGR (GeneExpert) testas | — |
| `test_type` | `1557` | — | — | Antigeno testas | — |
| `test_type` | `1678` | — | — | PGR mokamas testas | — |
| `test_type` | `1677` | — | — | PGR (GeneExpert) mokamas testas | — |
| `test_type` | `1697` | — | — | Antigeno mokamas testas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
