---
type: Table
title: "LaboratorijuRezultataiEvrk — COVID-19 laboratorijų rezultatai pagal EVRK"
description: "Covid-19 diagnostinių tyrimų rezultatai, agreguoti pagal datą ir ekonominės veiklos rūšis (EVRK 2)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/LaboratorijuRezultataiEvrk"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L46"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaboratorijuRezultataiEvrk — COVID-19 laboratorijų rezultatai pagal EVRK

Covid-19 diagnostinių tyrimų rezultatai, agreguoti pagal datą ir ekonominės veiklos rūšis (EVRK 2)

- **Model:** `datasets/gov/lsd/covid19/LaboratorijuRezultataiEvrk`[^manifest]
- **Dataset:** [datasets/gov/lsd/covid19](../covid19.md) (`datasets/gov/lsd/covid19`)
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L46)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/LaboratorijuRezultataiEvrk`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `test_date` | `date` | `D` | `4` | `open` | — | Diagnostinių laboratorinių tyrimų atlikimo data | — |
| `evrk_group_code` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis](../cl/evrk/EkonominesVeiklosRusis.md) | `4` | `open` | — | Tiriamųjų asmenų aktualios darbovietės ekonominės veiklos rūšių klasifikatoriaus (2 redakcija) grupės kodas. | nuoroda: https://osp.stat.gov.lt/static/evrk2.htm |
| `tests_positive` | `integer` | `U` | `4` | `open` | — | Teigiamų atsakymų skaičius (virusas aptiktas) | — |
| `tests_negative` | `integer` | `U` | `4` | `open` | — | Neigiamų atsakymų skaičius (virusas neaptiktas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
