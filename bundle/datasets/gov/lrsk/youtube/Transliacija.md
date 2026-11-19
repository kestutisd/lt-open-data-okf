---
type: Table
title: "Transliacija — Lietuvos Respublikos Seimo YouTube transliacijų duomenys"
description: "Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/youtube/Transliacija"
tags: [gov, lrsk, transliacija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/youtube.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2614/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/youtube"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Transliacija — Lietuvos Respublikos Seimo YouTube transliacijų duomenys

Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan. Taip pat pateikiama informacija apie transliacijos pradžios ir pabaigos laiko žymas.[^manifest]

- **Model:** `datasets/gov/lrsk/youtube/Transliacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo YouTube transliacijų duomenys](../youtube.md) (`datasets/gov/lrsk/youtube`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/youtube.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/youtube/Transliacija` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/youtube.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/youtube (https://data.gov.lt/datasets/2614/)
