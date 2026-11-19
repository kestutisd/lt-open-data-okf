---
type: Table
title: "Trukme — Vidutinė hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmė įstaigoje"
description: "Informacija apie vidutinę hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmę įstaigoje"
resource: "https://get.data.gov.lt/datasets/gov/vlk/vidutines_trukmes/Trukme"
tags: [gov, vlk, trukme, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vidutines_trukmes.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/vidutines_trukmes.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2330/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/vidutines_trukmes"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Trukme — Vidutinė hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmė įstaigoje

Informacija apie vidutinę hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmę įstaigoje[^manifest]

- **Model:** `datasets/gov/vlk/vidutines_trukmes/Trukme`[^manifest]
- **Dataset:** [Vidutinė hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo...](../vidutines_trukmes.md) (`datasets/gov/vlk/vidutines_trukmes`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/vidutines_trukmes.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vidutines_trukmes.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/vidutines_trukmes/Trukme` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `istg_id` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID`: `istg_id._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri suteikė paslaugas, ID |
| `grupe` | `string` | — | `3` | `open` | — | Paslaugos grupė | — |
| `vid_trukme` | `number` | `U` | `4` | `open` | — | Vidutinė trukmė dienomis | — |
| `lovadieniai` | `number` | `U` | `4` | `open` | — | Lovadienių skaičius | — |
| `atvejai` | `number` | `U` | `4` | `open` | — | Atvejų (etapų) skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vidutines_trukmes.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vidutines_trukmes.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/vidutines_trukmes (https://data.gov.lt/datasets/2330/)
