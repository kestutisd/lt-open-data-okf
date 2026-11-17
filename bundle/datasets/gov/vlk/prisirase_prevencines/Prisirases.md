---
type: Table
title: "Prisirases — Asmenų, galinčių dalyvauti prevencinėse programose, skaičius"
description: "Informacija apie asmenų, galinčių dalyvauti prevencinėje programoje, skaičius"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase_prevencines/Prisirases"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase_prevencines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_prevencines.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prisirases — Asmenų, galinčių dalyvauti prevencinėse programose, skaičius

Informacija apie asmenų, galinčių dalyvauti prevencinėje programoje, skaičius

- **Model:** `datasets/gov/vlk/prisirase_prevencines/Prisirases`[^manifest]
- **Dataset:** [datasets/gov/vlk/prisirase_prevencines](../prisirase_prevencines.md) (`datasets/gov/vlk/prisirase_prevencines`)
- **Manifest CSV:** [datasets/gov/vlk/prisirase_prevencines.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_prevencines.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase_prevencines/Prisirases`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `istaiga` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga[kodas]](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, prie kurios prisirašę asmenys, ID |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `draustumas` | `integer` | — | `3` | `open` | — | Draustumas | Požymis, parodantis, ar asmenys buvo apdrausti PSD nurodytu laikotarpiu |
| `programa` | `string` | — | `4` | `open` | — | Prevencinė programa | Nurodomas sutrumpintas prevencinės programos pavadinimas |
| `skaicius` | `number` | `U` | `4` | `open` | — | Prisirašiusių asmenų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | — | — |
| `lytis` | `"Vyras"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase_prevencines.csv
