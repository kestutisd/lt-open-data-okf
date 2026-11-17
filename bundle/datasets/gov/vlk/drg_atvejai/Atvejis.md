---
type: Table
title: "Atvejis — Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG"
description: "Informacija apie stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai/Atvejis"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg_atvejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atvejis — Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG

Informacija apie stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG

- **Model:** `datasets/gov/vlk/drg_atvejai/Atvejis`[^manifest]
- **Dataset:** [datasets/gov/vlk/drg_atvejai](../drg_atvejai.md) (`datasets/gov/vlk/drg_atvejai`)
- **Manifest CSV:** [datasets/gov/vlk/drg_atvejai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai/Atvejis`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `istg_id` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga](../istaigos/Istaiga.md) | `4` | `open` | — | Nuoroda į Įstaiga | — |
| `drg_kodas` | `string` | — | `4` | `open` | — | DRG kodas | Giminingų diagnozių grupės kodas |
| `dchir` | `string` | — | `4` | `open` | — | Dienos chirurgija | Požymis, nurodantis, ar tai dienos chirurgijos paslauga |
| `dchir_gr` | `integer` | — | `3` | `open` | — | Dienos chirurgijos paslaugų grupė | Požymis, nurodantis dienos chirurgijos paslaugų grupę |
| `kiekis` | `number` | `U` | `4` | `open` | — | Kiekis | Atvejų (etapų) kiekis |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dchir` | `"Ne"` | — | `open` | — | — |
| `dchir` | `"Taip"` | — | `open` | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg_atvejai.csv
