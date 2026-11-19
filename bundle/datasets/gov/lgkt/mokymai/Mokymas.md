---
type: Table
title: "Mokymas — Mokymų ir konsultacijų apie lygias galimybes duomenys"
description: "Lentelėje pateikti Lygių galimybių kontrolieriaus tarnybos (LGKT) vedamų mokymų ir teikiamų konsultacijų įvairioms Lietuvoje veikiančioms institucijoms duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/mokymai/Mokymas"
tags: [gov, lgkt, mokymas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/mokymai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lgkt/mokymai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2819/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgkt/mokymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mokymas — Mokymų ir konsultacijų apie lygias galimybes duomenys

Lentelėje pateikti Lygių galimybių kontrolieriaus tarnybos (LGKT) vedamų mokymų ir teikiamų konsultacijų įvairioms Lietuvoje veikiančioms institucijoms duomenys. Šioje lentelėje - nuo duomenų rinkimo pradžios, 2018 metų, iki 2024 metų sukaupta informacija. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lgkt/mokymai/Mokymas`[^manifest]
- **Dataset:** [Mokymų ir konsultacijų apie lygias galimybes duomenys](../mokymai.md) (`datasets/gov/lgkt/mokymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgkt/mokymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/mokymai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/mokymai/Mokymas` (`deployed`)[^manifest]
- **Provider:** `lgkt` — Lygių galimybių kontrolieriaus tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/mokymai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/mokymai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgkt/mokymai (https://data.gov.lt/datasets/2819/)
