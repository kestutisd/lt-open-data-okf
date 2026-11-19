---
type: Table
title: "Sprendimas — Sprendimai dėl Lietuvos Respublikos pilietybės suteikimo"
description: "Duomenys apie asmenis, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat vaikus, kuriems buvo konstatuotas Lietuvos Respublikos pilietybės turėjimo faktas..."
resource: "https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe/Sprendimas"
tags: [gov, migracija, sprendimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1943/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/lt_pilietybe"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sprendimas — Sprendimai dėl Lietuvos Respublikos pilietybės suteikimo

**Dataset Context:** Duomenys apie asmenis, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat vaikus, kuriems buvo konstatuotas Lietuvos Respublikos pilietybės turėjimo faktas, kurie Lietuvos Respublikos pilietybę įgijo juos įvaikinus arba pasikeitus tėvų pilietybei, neatsižvelgiant į jų gyvenamąją vietą.[^manifest]

- **Model:** `datasets/gov/migracija/lt_pilietybe/Sprendimas`[^manifest]
- **Dataset:** [Duomenys apie LT pilietybės suteikimą](../lt_pilietybe.md) (`datasets/gov/migracija/lt_pilietybe`)[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/lt_pilietybe.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe/Sprendimas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sprendimo_registracija` | `date` | `D` | `4` | `open` | — | Sprendimo registracijos data | — |
| `sprendimas` | `string` | — | `3` | `open` | — | Migracijos departamento sprendimas dėl Lietuvos Respublikos pilietybės | — |
| `sprendimo_pagrindas` | `string` | — | `3` | `open` | — | Sprendimo pagrindas | — |
| `poreiksme` | `string` | — | `2` | `open` | — | Sprendimo poreikšmė | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Sprendimą gavusio asmens pilietybė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Sprendimą gavusio asmens amžiaus grupė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `poreiksme` | `"update(property: ""poreiksme[]"", type: ""array"", source: ""Poreiksme"")"` | `property` | `4` | — | — | — | — |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L15)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/lt_pilietybe (https://data.gov.lt/datasets/1943/)
