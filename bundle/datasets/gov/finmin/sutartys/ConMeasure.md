---
type: Table
title: "ConMeasure — Sutarties priemonės"
description: "Spinta table datasets/gov/finmin/sutartys/ConMeasure (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConMeasure"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L114"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConMeasure — Sutarties priemonės

- **Model:** `datasets/gov/finmin/sutartys/ConMeasure`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L114](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L114)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConMeasure`
- **Primary Key (`ref`):** `con_measure_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_measure_id` | `string` | — | `4` | `open` | — | Sutarties priemonės identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `priority_area_group` | `string` | — | `2` | `open` | — | Prioritetinių sričių grupė | — |
| `priority_area_code` | `string` | — | `2` | `open` | — | Prioritetinė sritis | — |
| `esf_code` | `string` | — | `2` | `open` | — | ESF antrinė tema | — |
| `thematic_goal_code` | `string` | — | `2` | `open` | — | Tematinis tikslas | — |
| `eco_activity_code` | `string` | — | `2` | `open` | — | Ekonominė veikla | — |
| `program_measure_code` | `string` | — | `3` | `open` | — | Programos priemonės kodas | — |
| `func_cl_code` | `string` | — | `3` | `open` | — | Funkcinės klasifikacijos kodas | — |
| `eco_cl_code` | `string` | — | `3` | `open` | — | Ekonominės klasifikacijos kodas | — |
| `eu_fin_code` | `string` | — | `3` | `open` | — | Finansavimo šaltinio kodas. ES | — |
| `gf_fin_code` | `string` | — | `3` | `open` | — | Finansavimo šaltinio kodas. BF | — |
| `fixed_norm` | `boolean` | — | `4` | `open` | — | Taikoma fiksuotoji projekto išlaidų norma | — |
| `fin_form1` | `string` | — | `2` | `open` | — | Finansavimo forma Nr. 1 | — |
| `fin_form2` | `string` | — | `2` | `open` | — | Finansavimo forma Nr. 2 | — |
| `fin_form3` | `string` | — | `2` | `open` | — | Finansavimo forma Nr. 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
