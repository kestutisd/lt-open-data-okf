---
type: Table
title: "Programa — Studijų programos"
description: "Kurias yra baigę visuomenės sveikatos specialistai"
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Programa"
tags: [gov, hi, programa, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1106/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Programa — Studijų programos

Kurias yra baigę visuomenės sveikatos specialistai[^manifest]

- **Model:** `datasets/gov/hi/specialistai/Programa`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Programa` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sritis` | `string` | — | `4` | `open` | — | Visuomenės sveikatos specialisto studijų krypties grupė | — |
| `kryptis` | `string` | — | `4` | `open` | — | Visuomenės sveikatos specialisto studijų kryptis | VSPSR klasifikatorių sąraše studijų kryptys yra suvestos ir pagal seną galiojusį LR švietimo, mokslo ir sporto ministro 2007 m. liepos 23 d. įsakymą Nr. ISAK-1540 ir naujai patvirtintą LR švietimo, mokslo ir sporto ministro 2016 m. gruodžio 1 d. įsakymą Nr. V-1075 „Dėl studijų krypčių ir krypčių grupių, pagal kurias vyksta studijos aukštosiose mokyklose, sąrašo, jo keitimo tvarkos, kvalifikacinių laipsnių sąrangos ir studijų programų pavadinimų sudarymo principų patvirtinimo“ (todėl yra du kodai). |
| `count` | `integer` | `U` | `4` | `open` | — | Skaičius visuomenės sveikatos specialistų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/specialistai (https://data.gov.lt/datasets/1106/)
