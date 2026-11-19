---
type: Table
title: "Atvejis — Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG"
description: "Informacija apie stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai/Atvejis"
tags: [gov, vlk, atvejis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg_atvejai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2259/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/drg_atvejai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atvejis — Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG

Informacija apie stacionarinio aktyviojo gydymo atvejų skaičių pagal DRG[^manifest]

- **Model:** `datasets/gov/vlk/drg_atvejai/Atvejis`[^manifest]
- **Dataset:** [Stacionarinio aktyviojo gydymo atvejų skaičius pagal DRG](../drg_atvejai.md) (`datasets/gov/vlk/drg_atvejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg_atvejai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg_atvejai/Atvejis` (`deployed`)[^manifest]
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
| `istg_id` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID`: `istg_id._id`) | `4` | `open` | — | Nuoroda į Įstaiga | — |
| `drg_kodas` | `string` | — | `4` | `open` | — | DRG kodas | Giminingų diagnozių grupės kodas |
| `dchir` | `string` | — | `4` | `open` | — | Dienos chirurgija | Požymis, nurodantis, ar tai dienos chirurgijos paslauga |
| `dchir_gr` | `integer` | — | `3` | `open` | — | Dienos chirurgijos paslaugų grupė | Požymis, nurodantis dienos chirurgijos paslaugų grupę |
| `kiekis` | `number` | `U` | `4` | `open` | — | Kiekis | Atvejų (etapų) kiekis |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dchir` | `"Ne"` | — | `open` | — | — |
| `dchir` | `"Taip"` | — | `open` | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg_atvejai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg_atvejai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/drg_atvejai (https://data.gov.lt/datasets/2259/)
