---
type: Table
title: "Knygomatas — Knygomatai"
description: "Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai."
resource: "https://get.data.gov.lt/datasets/gov/lnb/knygomatai/Knygomatas"
tags: [gov, lnb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lnb/knygomatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Knygomatas — Knygomatai

Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai.

- **Model:** `datasets/gov/lnb/knygomatai/Knygomatas`[^manifest]
- **Dataset:** [Knygomatai](../knygomatai.md) (`datasets/gov/lnb/knygomatai`)
- **Manifest CSV:** [datasets/gov/lnb/knygomatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/knygomatai/Knygomatas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `knygomato_adresas` | `string` | — | `4` | `open` | — | Knygomato adresas | — |
| `isdavimo_salygos` | `string` | — | `4` | `open` | — | Knygomato išdavimo sąlygos | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Knygomato pavadinimas | — |
| `knygomatas_aktyvus` | `boolean` | — | `4` | `open` | — | Požymis ar aktyvus | — |
| `x_koord` | `integer` | — | `4` | `open` | — | X koordinatės | — |
| `y_koord` | `integer` | — | `4` | `open` | — | Y koordinatės | — |
| `patikimumas` | `integer` | `%` | `4` | `open` | — | Adreso/koordinačių patikimumas procentais | — |
| `aptikta_koordinaciu` | `integer` | — | `4` | `open` | — | Kiek aptikta koordinačių su tokiu patikimumu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/knygomatai.csv
