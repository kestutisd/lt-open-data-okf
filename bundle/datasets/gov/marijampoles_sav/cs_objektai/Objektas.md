---
type: Table
title: "Objektas — Marijampolės savivaldybėje šiuo metu veikiantys civilinės saugos objektai"
description: "Marijampolės mieste bei rajone šiuo metu veikiančios priedangos ir kolektyvinės apsaugos statiniai"
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/cs_objektai/Objektas"
tags: [gov, marijampoles_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/cs_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/cs_objektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Objektas — Marijampolės savivaldybėje šiuo metu veikiantys civilinės saugos objektai

Marijampolės mieste bei rajone šiuo metu veikiančios priedangos ir kolektyvinės apsaugos statiniai

- **Model:** `datasets/gov/marijampoles_sav/cs_objektai/Objektas`[^manifest]
- **Dataset:** [Marijampolės savivaldybėje šiuo metu veikiantys civilinės saugos objektai](../cs_objektai.md) (`datasets/gov/marijampoles_sav/cs_objektai`)
- **Manifest CSV:** [datasets/gov/marijampoles_sav/cs_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/cs_objektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/cs_objektai/Objektas`
- **Primary Key (`ref`):** `vda_eil_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_eil_nr` | `string` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Objekto seniūnija | — |
| `adresas` | `string` | — | `4` | `open` | — | Objekto adresas | — |
| `objekto_pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `su_negalia` | `string` | — | `4` | `open` | — | Ar žmonės su negalia gali naudotis | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS koordinačių sistemoje | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS koordinačių sistemoje | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Priedanga"` | — | — | — | — |
| `tipas` | `"Kolektyvinės apsaugos statinys"` | — | — | — | — |
| `su_negalia` | `"Taip"` | — | — | — | — |
| `su_negalia` | `"Ne"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/cs_objektai.csv
