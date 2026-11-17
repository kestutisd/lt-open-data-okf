---
type: Table
title: "AugaluFenologija — LHMT duomenys apie Lietuvoje žydinčių augalų fenologinius tarpsnius"
description: "Spinta table datasets/gov/lhmt/fenologija/AugaluFenologija (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/fenologija/AugaluFenologija"
tags: [gov, lhmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# AugaluFenologija — LHMT duomenys apie Lietuvoje žydinčių augalų fenologinius tarpsnius

- **Model:** `datasets/gov/lhmt/fenologija/AugaluFenologija`[^manifest]
- **Dataset:** [Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje](../fenologija.md) (`datasets/gov/lhmt/fenologija`)
- **Manifest CSV:** [datasets/gov/lhmt/augalu_fenologija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/fenologija/AugaluFenologija`
- **Primary Key (`ref`):** `vda_pk`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_pk` | `string` | — | `4` | `open` | — | VDA PK | Valstybės duomenų agentūros unikalus identifikacinis įrašo numeris (pirminis raktas). |
| `augalas_id` | `string` | — | `4` | `open` | — | Augalo ID | Augalo identifikacinis numeris LHMT informacinėje sistemoje. |
| `augalas` | `string` | — | `4` | `open` | — | Augalo pavadinimas | — |
| `faze_id` | `string` | — | `4` | `open` | — | Fazės ID | Kartu su fazės stadijos identifikaciniu kodu naudojami konkrečiai fazei įvardinti. |
| `fazes_stad_id` | `string` | — | `4` | `open` | — | Fazės stadijos ID | Kartu su fazės identifikaciniu kodu naudojami konkrečiai fazei įvardinti. |
| `faze` | `string` | — | `4` | `open` | — | Fenologinio tarpsnio fazė | Augalo fenologinio tarpsnio fazė. |
| `stebeta` | `date` | `1D` | `4` | `open` | — | Stebėjimo data | Data, kada buvo augalo fenologinė tarpsnio fazė pastebėta |
| `stotis` | `string` | — | `4` | `open` | — | Stebėjimo stotis | Stoties, kurioje atliekamas stebėjimas, pavadinimas. AMS - automatinė meteorologijos stotis, MS - meteorologijos stotis. |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | WGS-84 koordinatės taškas | Stoties, kurioje atliekamas stebėjimas, WGS-84 taško koordinatė. |
| `duomenys_ikelti` | `date` | `1D` | `4` | `open` | — | Duomenys įkelti | Kada duomenys buvo užregistruoti LHMT informacinėje sistemoje. |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv
