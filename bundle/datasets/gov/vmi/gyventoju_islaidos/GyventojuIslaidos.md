---
type: Table
title: "GyventojuIslaidos — Duomenys apie mokėtojo deklaruotas išlaidas, kuriomis pagal GPMĮ 21 str. gali būti mažinamos apmokestinamosios pajamos"
description: "Spinta table datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/gyventoju_islaidos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyventojuIslaidos — Duomenys apie mokėtojo deklaruotas išlaidas, kuriomis pagal GPMĮ 21 str. gali būti mažinamos apmokestinamosios pajamos

- **Model:** `datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos`[^manifest]
- **Dataset:** [datasets/gov/vmi/gyventoju_islaidos](../gyventoju_islaidos.md) (`datasets/gov/vmi/gyventoju_islaidos`)
- **Manifest CSV:** [datasets/gov/vmi/gyventoju_islaidos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `4` | `open` | — | Mokestinio laikotarpio metai | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Sistemos subjekto savivaldybes kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Sistemos subjekto savivaldybes pavadinimas | — |
| `mm_kodas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo identifikacinis numeris | — |
| `ir_kodas` | `string` | — | `4` | `open` | — | Išlaidų rūšies kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Išlaidų pavadinimas | — |
| `suma` | `number` | — | `4` | `open` | — | Išlaidų suma | Išlaidų suma esanti virš 600000 eurų yra fiksuojama 600000 verte |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/gyventoju_islaidos.csv
