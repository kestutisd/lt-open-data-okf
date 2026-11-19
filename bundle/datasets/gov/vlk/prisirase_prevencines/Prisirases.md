---
type: Table
title: "Prisirases — Asmenų, galinčių dalyvauti prevencinėse programose, skaičius"
description: "Informacija apie asmenų, galinčių dalyvauti prevencinėje programoje, skaičius"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase_prevencines/Prisirases"
tags: [gov, vlk, prisirases, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_prevencines.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase_prevencines.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2323/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase_prevencines"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Prisirases — Asmenų, galinčių dalyvauti prevencinėse programose, skaičius

Informacija apie asmenų, galinčių dalyvauti prevencinėje programoje, skaičius[^manifest]

- **Model:** `datasets/gov/vlk/prisirase_prevencines/Prisirases`[^manifest]
- **Dataset:** [Asmenų, galinčių dalyvauti prevencinėse programose, skaičius](../prisirase_prevencines.md) (`datasets/gov/vlk/prisirase_prevencines`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/prisirase_prevencines.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_prevencines.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase_prevencines/Prisirases` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID` via `Istaiga[kodas]`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, prie kurios prisirašę asmenys, ID |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `draustumas` | `integer` | — | `3` | `open` | — | Draustumas | Požymis, parodantis, ar asmenys buvo apdrausti PSD nurodytu laikotarpiu |
| `programa` | `string` | — | `4` | `open` | — | Prevencinė programa | Nurodomas sutrumpintas prevencinės programos pavadinimas |
| `skaicius` | `number` | `U` | `4` | `open` | — | Prisirašiusių asmenų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | — | — |
| `lytis` | `"Vyras"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase_prevencines.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_prevencines.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase_prevencines (https://data.gov.lt/datasets/2323/)
