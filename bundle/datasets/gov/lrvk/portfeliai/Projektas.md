---
type: Table
title: "Projektas — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys"
description: "Lentelės objektas - vienas vykdomas ar baigtas vykdyti projektas."
resource: "https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Projektas"
tags: [gov, lrvk, projektas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1550/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Projektas — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys

Lentelės objektas - vienas vykdomas ar baigtas vykdyti projektas. Per lauką "projekto_id" jungiasi su kitomis rinkinio lentelėmis.[^manifest]

- **Model:** `datasets/gov/lrvk/portfeliai/Projektas`[^manifest]
- **Dataset:** [Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys](../portfeliai.md) (`datasets/gov/lrvk/portfeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrvk/portfeliai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Projektas` (`deployed`)[^manifest]
- **Provider:** `lrvk` — Lietuvos Respublikos Vyriausybės Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai (https://data.gov.lt/datasets/1550/)
