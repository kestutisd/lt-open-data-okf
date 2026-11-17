---
type: Table
title: "Projektas — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys"
description: "Lentelės objektas - vienas vykdomas ar baigtas vykdyti projektas."
resource: "https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Projektas"
tags: [gov, lrvk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projektas — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys

Lentelės objektas - vienas vykdomas ar baigtas vykdyti projektas. Per lauką "projekto_id" jungiasi su kitomis rinkinio lentelėmis.

- **Model:** `datasets/gov/lrvk/portfeliai/Projektas`[^manifest]
- **Dataset:** [Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys](../portfeliai.md) (`datasets/gov/lrvk/portfeliai`)
- **Manifest CSV:** [datasets/gov/lrvk/portfeliai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Projektas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros unikalus įrašo identifikatorius | — |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto identifikacinis numeris | — |
| `strat_portfelis` | `string` | — | `4` | `open` | — | Vyriausybės kadencijos klasifikatorius | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `institucija` | `string` | — | `4` | `open` | — | Projektą vykdanti institucija | — |
| `institucijos_portfelis` | `string` | — | `4` | `open` | — | Projektą vykdančios institucijos portfelio pavadinimas | — |
| `etapas` | `string` | — | `4` | `open` | — | Projekto etapo pavadinimas duomenų atnaujinimo metu | — |
| `projekto_aprasymas` | `string` | — | `4` | `open` | — | Projekto aprašymas | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Projekto pradÅ¾ios data | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Projekto pabaigos data | — |
| `biudzetas_eur` | `number` | — | `2` | `open` | — | Projekto biudžetas eurais | — |
| `proj_tikslas` | `string` | — | `4` | `open` | — | Projekto tikslai | — |
| `strat_tikslas` | `string` | — | `4` | `open` | — | Strateginiai projekto tikslai | — |
| `suinteresuota_salis` | `string` | — | `4` | `open` | — | Projekto vykdymu suinteresuotos šalys | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `biudzetas_eur` | `update(type: "money", ref: "EUR")` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv
