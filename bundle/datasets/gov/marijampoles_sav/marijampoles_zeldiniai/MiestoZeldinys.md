---
type: Table
title: "MiestoZeldinys — Marijampolės savivaldybės želdiniai"
description: "Spinta table datasets/gov/marijampoles_sav/marijampoles_zeldiniai/MiestoZeldinys (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/marijampoles_zeldiniai/MiestoZeldinys"
tags: [gov, marijampoles_sav, miestozeldinys, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/marijampoles_zeldiniai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/marijampoles_zeldiniai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MiestoZeldinys — Marijampolės savivaldybės želdiniai

- **Model:** `datasets/gov/marijampoles_sav/marijampoles_zeldiniai/MiestoZeldinys`[^manifest]
- **Dataset:** [Marijampolės savivaldybės želdiniai](../marijampoles_zeldiniai.md) (`datasets/gov/marijampoles_sav/marijampoles_zeldiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/marijampoles_zeldiniai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/marijampoles_zeldiniai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/marijampoles_zeldiniai/MiestoZeldinys` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus želdinio identifikatorius | — |
| `inv_apsk_nr` | `string` | — | `4` | `open` | — | Inventorizacijos apskaitos numeris | — |
| `inv_data` | `date` | `D` | `4` | `open` | — | Želdinio inventorizacijos data | — |
| `zeldyno_kodas` | `string` | — | `4` | `open` | — | Inventorizuoto želdinio želdyno kodas | — |
| `vieta` | `string` | — | `4` | `open` | — | Želdyno vieta | — |
| `sklypo_nr` | `string` | — | `4` | `open` | — | Želdyno sklypo numeris | — |
| `rusis` | `string` | — | `4` | `open` | — | Inventorizuoto želdinio rūšis | — |
| `aukstis_m` | `integer` | — | `4` | `open` | — | Želdinio aukštis metrais | — |
| `skersmuo_cm` | `integer` | — | `4` | `open` | — | Želdinio skersmuo centimetrais po inventorizacijos | — |
| `amzius` | `integer` | — | `4` | `open` | — | Inventorizuoto želdinio amžius | — |
| `tvarkymas` | `string` | — | `4` | `open` | — | Inventorizuoto želdinio rekomenduojami tvarkymo darbai | — |
| `pastaba` | `string` | — | `4` | `open` | — | Pastabos apie inventorizuotą želdinį | — |
| `bukle` | `string` | — | `4` | `open` | — | Inventorizuoto želdinio būklė | — |
| `salinimo_data` | `date` | `D` | `4` | `open` | — | Želdinio šalinimo data | — |
| `zeldinio_vieta` | `geometry(point, 3346)` | — | `4` | `open` | — | Želdinio koordinatės LKS-94 formatu | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Želdinio ilgumos koordinatė | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Želdinio platumos koordinatė | — |
| `koregavimo_data` | `date` | `D` | `4` | `open` | — | Eilutės koregavimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/marijampoles_zeldiniai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/marijampoles_zeldiniai.csv#L6)
