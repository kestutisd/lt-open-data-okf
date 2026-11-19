---
type: Table
title: "ArestuStatistika — Nuteistųjų arešto bausme statistika"
description: "Lietuvos kalėjimų departamentas (LKD) kaupia asmenų, nuteistų arešto bausme, statistinius duomenis nuo 2021 m., atnaujinamus kasmet, gaunamus iš kalinimo įstaigų."
resource: "https://get.data.gov.lt/datasets/gov/lkd/arestai/ArestuStatistika"
tags: [gov, lkd, arestustatistika, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/arestai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lkd/arestai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2631/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lkd/arestai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ArestuStatistika — Nuteistųjų arešto bausme statistika

Lietuvos kalėjimų departamentas (LKD) kaupia asmenų, nuteistų arešto bausme, statistinius duomenis nuo 2021 m., atnaujinamus kasmet, gaunamus iš kalinimo įstaigų. Rinkinys apima punkto numerį, naudojamą atskirti atitinkamus duomenis pagal konkrečius metus. Punkto numeriai gali būti pateikti tiksliau naudojant daugiau skaitmenų, atskirtų taškais. Tarp minėtų duomenų patenka nusikaltimai, išvykimo iš kalinimo įstaigos pobūdžiai, nuteistųjų amžiaus grupės. Rinkinyje minėti duomenys matuojami vienetais nuteistųjų asmenų arba metais, mėnesiais ir dienomis. Patogumo dėlei taip pat naudojami rinkinio eilučių numeriai.[^manifest]

- **Model:** `datasets/gov/lkd/arestai/ArestuStatistika`[^manifest]
- **Dataset:** [Nuteistųjų arešto bausme statistika](../arestai.md) (`datasets/gov/lkd/arestai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lkd/arestai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/arestai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lkd/arestai/ArestuStatistika` (`deployed`)[^manifest]
- **Provider:** `lkd` — Lietuvos kalėjimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros unikalus identifikatorius | — |
| `punkto_nr` | `string` | — | `4` | `open` | — | Atitinkamais metais matuojamo duomens teisinis identifikatorius | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Kada aktualūs šios eilutės skaičiai | — |
| `duomenu_pavadinimas` | `string` | — | `4` | `open` | — | Matuojamo duomens pavadinimas | — |
| `skaicius_1` | `integer` | — | `4` | `open` | — | Pirmojo vieneto reikšmė | — |
| `vienetas_1` | `string` | — | `4` | `open` | — | Pirmasis vienetas: vienetas arba metų skaičius | — |
| `skaicius_2` | `integer` | — | `4` | `open` | — | Antrojo vieneto reikšmė | — |
| `vienetas_2` | `string` | — | `4` | `open` | — | Antrasis vienetas mėnesiais | — |
| `skaicius_3` | `integer` | — | `4` | `open` | — | Trečiojo vieneto reikšmė | — |
| `vienetas_3` | `string` | — | `4` | `open` | — | Trečiasis vienetas dienomis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lkd/arestai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/arestai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lkd/arestai (https://data.gov.lt/datasets/2631/)
