---
type: Table
title: "PastatoElementoNusidevejimas"
description: "Spinta table datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoNusidevejimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoNusidevejimas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# PastatoElementoNusidevejimas

- **Model:** `datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoNusidevejimas`[^manifest]
- **Dataset:** [Pastatų ir jo elementų nusidėvėjimas ir rizikos](../pastatu_duomenu_bankas.md) (`datasets/gov/ssva/pastatu_duomenu_bankas`)
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoNusidevejimas`
- **Primary Key (`ref`):** `elemento_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `elemento_id` | `string` | — | `4` | `open` | — | Pastato elemento identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Pastato identifikatorius | — |
| `statybos_metai` | `integer` | — | `4` | `open` | — | Pastato statybos metai | — |
| `elemento_pavadinimas` | `string` | — | `4` | `open` | — | Pastato elemento pavadinimas | — |
| `tarnavimo_trukme_metais` | `string` | — | `4` | `open` | — | Elemento tarnavimo trukmė metais | — |
| `nusidevejimo_vertinimas` | `number` | — | `4` | `open` | — | Elemento nusidėvėjimo vertinimas | — |
| `objekto_adresas` | `string` | — | `4` | `open` | — | Pastato adresas | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Pastato vietos koordinatės LKS-94 (EPSG:3346) sistemoje | — |
| `iraso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv
