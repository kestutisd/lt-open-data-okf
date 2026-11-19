---
type: Table
title: "ConMeasure — Sutarties priemonės"
description: "Spinta table datasets/gov/finmin/sutartys/ConMeasure (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConMeasure"
tags: [gov, finmin, conmeasure, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L114"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L114"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ConMeasure — Sutarties priemonės

- **Model:** `datasets/gov/finmin/sutartys/ConMeasure`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L114](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L114)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConMeasure` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `con_measure_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_measure_id` | `string` | — | `4` | `open` | — | Sutarties priemonės identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L114 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L114)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
