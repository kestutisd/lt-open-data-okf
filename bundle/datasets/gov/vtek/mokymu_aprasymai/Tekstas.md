---
type: Table
title: "Tekstas — Nuotolinių mokymų aprašymai"
description: "Siekdama padėti deklaruojantiesiems geriau suprasti, kaip taikyti Viešųjų ir privačių interesų derinimo įstatymo nuostatas bei tinkamai deklaruoti interesus, Vyriausioji tarnybinės etikos komisija organizuoja nuotolinius mokymų kursus."
resource: "https://get.data.gov.lt/datasets/gov/vtek/mokymu_aprasymai/Tekstas"
tags: [gov, vtek, tekstas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/mokymai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/vtek/mokymai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3799/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vtek/mokymu_aprasymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Tekstas — Nuotolinių mokymų aprašymai

Siekdama padėti deklaruojantiesiems geriau suprasti, kaip taikyti Viešųjų ir privačių interesų derinimo įstatymo nuostatas bei tinkamai deklaruoti interesus, Vyriausioji tarnybinės etikos komisija organizuoja nuotolinius mokymų kursus. Kursai skirti viešojo sektoriaus darbuotojams bei deklaracijas teikiantiems asmenims. Rinkinyje pateikiami nuotolinių mokymų duomenys.[^manifest]

- **Model:** `datasets/gov/vtek/mokymu_aprasymai/Tekstas`[^manifest]
- **Dataset:** [Nuotolinių mokymų aprašymai](../mokymu_aprasymai.md) (`datasets/gov/vtek/mokymu_aprasymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/mokymai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/mokymai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/mokymu_aprasymai/Tekstas` (`deployed`)[^manifest]
- **Provider:** `vtek` — Vyriausioji tarnybinės etikos komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `mokymas` | `string` | — | `4` | `open` | — | Mokymų kurso pavadinimas | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | Paskutinė teksto atnaujinimo data | — |
| `aprasymas_lt` | `string` | — | `2` | `open` | — | Mokymų aprašymas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mokymas` | `"Privačių interesų deklaravimas"` | — | — | — | — |
| `mokymas` | `"Lobistinė veikla"` | — | — | — | — |
| `mokymas` | `"Interesų konflikto identifikavimas ir valdymas"` | — | — | — | — |
| `mokymas` | `"Apribojimai pasibaigus tarnybai"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/mokymai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/mokymai.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vtek/mokymu_aprasymai (https://data.gov.lt/datasets/3799/)
