---
type: Table
title: "VeiklosEfektyvumoRodiklis — ASPĮ veiklos kokybės ir efektyvumo vertinimo rodiklių suvestinė"
description: "Informacija apie gydymo įstaigų, teikiančių stacionarines asmens sveikatos priežiūros paslaugas, veiklos kokybės ir efektyvumo vertinimo rodiklių duomenis"
resource: "https://get.data.gov.lt/datasets/gov/vlk/veiklos_efektyvumo_rodikliai/VeiklosEfektyvumoRodiklis"
tags: [gov, vlk, veiklosefektyvumorodiklis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1584/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/veiklos_efektyvumo_rodikliai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VeiklosEfektyvumoRodiklis — ASPĮ veiklos kokybės ir efektyvumo vertinimo rodiklių suvestinė

Informacija apie gydymo įstaigų, teikiančių stacionarines asmens sveikatos priežiūros paslaugas, veiklos kokybės ir efektyvumo vertinimo rodiklių duomenis[^manifest]

- **Model:** `datasets/gov/vlk/veiklos_efektyvumo_rodikliai/VeiklosEfektyvumoRodiklis`[^manifest]
- **Dataset:** [Gydymo įstaigų veiklos kokybės ir efektyvumo vertinimo rodiklių suvestinė](../veiklos_efektyvumo_rodikliai.md) (`datasets/gov/vlk/veiklos_efektyvumo_rodikliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/veiklos_efektyvumo_rodikliai/VeiklosEfektyvumoRodiklis` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Data metų tikslumu |
| `rodiklis` | `string` | — | `4` | `open` | — | Rodiklis | Rodiklio pavadinimas |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID` via `Istaiga[kodas]`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri teikė paslaugas, ID |
| `reiksme` | `number` | — | `4` | `open` | — | Reikšmė | Rodiklio reikšmė procentais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/veiklos_efektyvumo_rodikliai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/veiklos_efektyvumo_rodikliai (https://data.gov.lt/datasets/1584/)
