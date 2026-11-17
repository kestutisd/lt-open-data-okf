---
type: Table
title: "VeiklosEfektyvumoRodiklis — ASPĮ veiklos kokybės ir efektyvumo vertinimo rodiklių suvestinė"
description: "Informacija apie gydymo įstaigų, teikiančių stacionarines asmens sveikatos priežiūros paslaugas, veiklos kokybės ir efektyvumo vertinimo rodiklių duomenis"
resource: "https://get.data.gov.lt/datasets/gov/vlk/veiklos_efektyvumo_rodikliai/VeiklosEfektyvumoRodiklis"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeiklosEfektyvumoRodiklis — ASPĮ veiklos kokybės ir efektyvumo vertinimo rodiklių suvestinė

Informacija apie gydymo įstaigų, teikiančių stacionarines asmens sveikatos priežiūros paslaugas, veiklos kokybės ir efektyvumo vertinimo rodiklių duomenis

- **Model:** `datasets/gov/vlk/veiklos_efektyvumo_rodikliai/VeiklosEfektyvumoRodiklis`[^manifest]
- **Dataset:** [datasets/gov/vlk/veiklos_efektyvumo_rodikliai](../veiklos_efektyvumo_rodikliai.md) (`datasets/gov/vlk/veiklos_efektyvumo_rodikliai`)
- **Manifest CSV:** [datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/veiklos_efektyvumo_rodikliai/VeiklosEfektyvumoRodiklis`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Data metų tikslumu |
| `rodiklis` | `string` | — | `4` | `open` | — | Rodiklis | Rodiklio pavadinimas |
| `istaiga` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga[kodas]](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri teikė paslaugas, ID |
| `reiksme` | `number` | — | `4` | `open` | — | Reikšmė | Rodiklio reikšmė procentais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv
