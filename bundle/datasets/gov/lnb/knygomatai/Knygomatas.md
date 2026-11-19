---
type: Table
title: "Knygomatas — Knygomatai"
description: "Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai."
resource: "https://get.data.gov.lt/datasets/gov/lnb/knygomatai/Knygomatas"
tags: [gov, lnb, knygomatas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lnb/knygomatai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2624/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/knygomatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Knygomatas — Knygomatai

Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai.[^manifest]

- **Model:** `datasets/gov/lnb/knygomatai/Knygomatas`[^manifest]
- **Dataset:** [Knygomatai](../knygomatai.md) (`datasets/gov/lnb/knygomatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/knygomatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/knygomatai/Knygomatas` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/knygomatai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/knygomatai (https://data.gov.lt/datasets/2624/)
