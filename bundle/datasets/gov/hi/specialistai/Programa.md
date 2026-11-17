---
type: Table
title: "Programa — Studijų programos"
description: "Kurias yra baigę visuomenės sveikatos specialistai"
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Programa"
tags: [gov, hi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# Programa — Studijų programos

Kurias yra baigę visuomenės sveikatos specialistai

- **Model:** `datasets/gov/hi/specialistai/Programa`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Programa`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sritis` | `string` | — | `4` | `open` | — | Visuomenės sveikatos specialisto studijų krypties grupė | — |
| `kryptis` | `string` | — | `4` | `open` | — | Visuomenės sveikatos specialisto studijų kryptis | VSPSR klasifikatorių sąraše studijų kryptys yra suvestos ir pagal seną galiojusį LR švietimo, mokslo ir sporto ministro 2007 m. liepos 23 d. įsakymą Nr. ISAK-1540 ir naujai patvirtintą LR švietimo, mokslo ir sporto ministro 2016 m. gruodžio 1 d. įsakymą Nr. V-1075 „Dėl studijų krypčių ir krypčių grupių, pagal kurias vyksta studijos aukštosiose mokyklose, sąrašo, jo keitimo tvarkos, kvalifikacinių laipsnių sąrangos ir studijų programų pavadinimų sudarymo principų patvirtinimo“ (todėl yra du kodai). |
| `count` | `integer` | `U` | `4` | `open` | — | Skaičius visuomenės sveikatos specialistų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv
