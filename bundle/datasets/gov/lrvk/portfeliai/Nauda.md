---
type: Table
title: "Nauda — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio teikiamų naudų duomenys"
description: "Lentelės objektas - projekto teikiama nauda."
resource: "https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Nauda"
tags: [gov, lrvk, nauda, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1550/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nauda — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio teikiamų naudų duomenys

Lentelės objektas - projekto teikiama nauda. Per lauką "projekto_id" jungiasi su kitomis rinkinio lentelėmis.[^manifest]

- **Model:** `datasets/gov/lrvk/portfeliai/Nauda`[^manifest]
- **Dataset:** [Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys](../portfeliai.md) (`datasets/gov/lrvk/portfeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrvk/portfeliai.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Nauda` (`deployed`)[^manifest]
- **Provider:** `lrvk` — Lietuvos Respublikos Vyriausybės Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `naudos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `naudos_id` | `string` | — | `4` | `open` | — | Naudos identifikatorius | — |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `institucija` | `string` | — | `4` | `open` | — | Projektą vykdanti institucija | — |
| `nauda` | `string` | — | `4` | `open` | — | Projekto teikiamos naudos | — |
| `naudos_aprasymas` | `string` | — | `3` | `open` | — | Projekto teikiamos naudos aprašymas | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Siekiamos naudos rekšmės mato vienetas | — |
| `atskaitos_rodiklio_reiksme` | `number` | — | `4` | `open` | — | Naudos atskaitos rodiklio reikšmė | — |
| `siekiama_rodiklio_reiksme` | `number` | — | `4` | `open` | — | Siekiama naudos rodiklio rekšmė | — |
| `ar_pasiekta` | `boolean` | — | `4` | `open` | — | Požymis, ar nauda buvo pasiekta | — |
| `pasiekimo_terminas` | `date` | `D` | `4` | `open` | — | Naudos pasiekimo data | — |
| `duomenu_atnaujinimas` | `datetime` | — | — | — | — | Duomenų apie naudą atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai (https://data.gov.lt/datasets/1550/)
