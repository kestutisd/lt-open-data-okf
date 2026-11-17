---
type: Table
title: "Transliacija — Lietuvos Respublikos Seimo YouTube transliacijų duomenys"
description: "Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan. Taip pat pateikiama informacija apie transliacijos pradžios ir pabaigos laiko..."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/youtube/Transliacija"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/youtube.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Transliacija — Lietuvos Respublikos Seimo YouTube transliacijų duomenys

Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan. Taip pat pateikiama informacija apie transliacijos pradžios ir pabaigos laiko žymas.

- **Model:** `datasets/gov/lrsk/youtube/Transliacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo YouTube transliacijų duomenys](../youtube.md) (`datasets/gov/lrsk/youtube`)
- **Manifest CSV:** [datasets/gov/lrsk/youtube.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/youtube/Transliacija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Youtube įrašo pavadinimas | — |
| `aprasymas` | `string` | — | `2` | `open` | — | Youtube įrašo aprašymas | — |
| `pradzia` | `datetime` | `L` | `4` | `open` | — | Youtube įrašo pradžia | — |
| `pabaiga` | `datetime` | `L` | `4` | `open` | — | Youtube įrašo pabaiga | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas` | `update(property: "aprasymas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/youtube.csv
