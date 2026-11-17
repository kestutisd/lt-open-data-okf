---
type: Table
title: "PastatoElementoRizika"
description: "Spinta table datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PastatoElementoRizika

- **Model:** `datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika`[^manifest]
- **Dataset:** [Pastatų ir jo elementų nusidėvėjimas ir rizikos](../pastatu_duomenu_bankas.md) (`datasets/gov/ssva/pastatu_duomenu_bankas`)
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika`
- **Primary Key (`ref`):** `rizikos_vertinimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rizikos_vertinimo_id` | `string` | — | `4` | `open` | — | Rizikos vertinimo įrašo unikalus identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Pastato identifikatorius | — |
| `statybos_metai` | `integer` | — | `4` | `open` | — | Pastato statybos metai | — |
| `elemento_pavadinimas` | `string` | — | `4` | `open` | — | Pastato elemento pavadinimas | — |
| `rizikos_balas` | `string` | — | `4` | `open` | — | Pastato elemento rizikos vertinimo balas | — |
| `ivertinimo_balas` | `string` | — | `4` | `open` | — | Apžiūros ar vertinimo metu suteiktas balas | — |
| `didziausias_galimas_balas` | `string` | — | `4` | `open` | — | Didžiausias galimas vertinimo balas | — |
| `ar_kritinis` | `string` | — | `4` | `open` | — | Požymis, ar rizikos vertinimas yra kritinis | — |
| `kategorijos_pavadinimas` | `string` | — | `4` | `open` | — | Vertinimo kategorijos pavadinimas | — |
| `dokumento_numeris` | `string` | — | `4` | `open` | — | Dokumento numeris | — |
| `apziuros_tipas` | `string` | — | `4` | `open` | — | Pastato elemento apžiūros tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Pastato adresas | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Pastato vietos koordinatės LKS-94 (EPSG:3346) sistemoje | — |
| `sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv
