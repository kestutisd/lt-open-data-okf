---
type: Table
title: "Mokymas — Mokymų ir konsultacijų apie lygias galimybes duomenys"
description: "Lentelėje pateikti Lygių galimybių kontrolieriaus tarnybos (LGKT) vedamų mokymų ir teikiamų konsultacijų įvairioms Lietuvoje veikiančioms institucijoms duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/mokymai/Mokymas"
tags: [gov, lgkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgkt/mokymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/mokymai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Mokymas — Mokymų ir konsultacijų apie lygias galimybes duomenys

Lentelėje pateikti Lygių galimybių kontrolieriaus tarnybos (LGKT) vedamų mokymų ir teikiamų konsultacijų įvairioms Lietuvoje veikiančioms institucijoms duomenys. Šioje lentelėje - nuo duomenų rinkimo pradžios, 2018 metų, iki 2024 metų sukaupta informacija.

- **Model:** `datasets/gov/lgkt/mokymai/Mokymas`[^manifest]
- **Dataset:** [Mokymų ir konsultacijų apie lygias galimybes duomenys](../mokymai.md) (`datasets/gov/lgkt/mokymai`)
- **Manifest CSV:** [datasets/gov/lgkt/mokymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/mokymai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/mokymai/Mokymas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Mokymų ar konsultacijos data | — |
| `tema` | `string` | — | `4` | `open` | — | Mokymų ar konsultacijos tema | — |
| `formatas` | `string` | — | `4` | `open` | — | Mokymų ar konsultacijos formatas | — |
| `trukme` | `string` | — | `4` | `open` | — | Mokymų ar konsultacijos trukmė | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos ar įstaigos, kuriai buvo vedami mokymai, pavadinimas | — |
| `tiksline_grupe` | `string` | — | `4` | `open` | — | Mokymų ar konsultacijos tikslinė grupė | — |
| `dalyviu_skaicius_orig` | `string` | — | `4` | `open` | — | Originalus dalyvių skaičius (skliausteliuose pateiktas dalyvavusių vyrų skaičius) | — |
| `dalyviu_skaicius_viso` | `integer` | — | `4` | `open` | — | Dalyvavusių asmenų skaičius (ištrauktas iš dalyviu_skaicius_orig stulpelio) | — |
| `vyru_sk` | `integer` | — | `4` | `open` | — | Dalyvavusių vyrų skaičius (ištrauktas iš dalyviu_skaicius_orig stulpelio) | — |
| `moteru_sk` | `integer` | — | `4` | `open` | — | Dalyvavusių moterų skaičius (išskaičiuotas iš dalyviu_skaicius_viso atėmus vyru_sk) | — |
| `vieta` | `string` | — | `4` | `open` | — | Mokymų ar konsultacijos vieta | — |
| `konsultavo_vede_moderavo` | `string` | — | `4` | `open` | — | Asmuo, kuris vedė, moderavo mokymus ar teikė konsultaciją | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/mokymai.csv
