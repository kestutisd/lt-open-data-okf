---
type: Table
title: "PastatoRizikaNusidevejimas"
description: "Spinta table datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas"
tags: [gov, ssva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# PastatoRizikaNusidevejimas

- **Model:** `datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas`[^manifest]
- **Dataset:** [Pastatų ir jo elementų nusidėvėjimas ir rizikos](../pastatu_duomenu_bankas.md) (`datasets/gov/ssva/pastatu_duomenu_bankas`)
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas`
- **Primary Key (`ref`):** `objekto_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_id` | `string` | — | `4` | `open` | — | Pastato identifikatorius | — |
| `nusidevejimo_balas` | `number` | — | `4` | `open` | — | Pastato nusidėvvėjimo balas | — |
| `rizikos_balas` | `number` | — | `4` | `open` | — | Pastato rizikos balas | — |
| `statybos_metai` | `integer` | — | `4` | `open` | — | Pastato statybos metai | — |
| `adresas` | `string` | — | `4` | `open` | — | Pastato adresas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Pastato vietos koordinatės LKS-94 (EPSG:3346) sistemoje | — |
| `iraso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv
