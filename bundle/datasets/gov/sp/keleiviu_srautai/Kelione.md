---
type: Table
title: "Kelione"
description: "Lentelėje pateikiama bendra informacija apie reisą – maršruto grafiko pavadinimas bei pradžia ir pabaiga"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/Kelione"
tags: [gov, sp, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kelione

Lentelėje pateikiama bendra informacija apie reisą – maršruto grafiko pavadinimas bei pradžia ir pabaiga

- **Model:** `datasets/gov/sp/keleiviu_srautai/Kelione`[^manifest]
- **Dataset:** [Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys](../keleiviu_srautai.md) (`datasets/gov/sp/keleiviu_srautai`)
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/Kelione`
- **Primary Key (`ref`):** `reiso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reiso_id` | `string` | — | `4` | `open` | — | Reiso identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Kelionės data | — |
| `keliones_pradzia` | `datetime` | `S` | `4` | `open` | — | Kelionės pradžia | — |
| `keliones_pabaiga` | `datetime` | `S` | `4` | `open` | — | Kelionės pabaiga | — |
| `pamainos_id` | `string` | — | `4` | `open` | — | Pamainos identifikatorius | Pamainos identifikatorius - Nurodo bloką, kuriam priklauso kelionė. Bloką sudaro viena kelionė arba daug nuoseklių kelionių, atliekamų ta pačia transporto priemone, apibrėžtų bendromis aptarnavimo dienomis |
| `pamainos_pav` | `string` | — | `4` | `open` | — | Pamainos pavadinimas | Pavadinimo struktūra: Transporto rūšis (A - autobusas arba T - troleibusas) maršruto numeris - Tvarkaraščio grafiko numeris - Savaitės dienos tipas (1 – darbo diena, 6 – šeštadienis, 7 – sekmadienis) - Tvarkaraščio įsigaliojimo data – YYMMDD formatu |
| `tvarkarascio_id` | `string` | — | `4` | `open` | — | Maršruto tvarkaraščio identifikatorius | — |
| `tvarkarascio_pav` | `string` | — | `4` | `open` | — | Mašruto tvarkaraščio pavadinimas | — |
| `stoteliu_sk` | `integer` | — | `4` | `open` | — | Stotelių skaičius maršrute | — |
| `tp_id` | `string` | — | `4` | `open` | — | Transporto priemonės identifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv
