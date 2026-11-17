---
type: Table
title: "PaySchedule — Projekto mokėjimo prašymo teikimo grafikas"
description: "Spinta table datasets/gov/finmin/sutartys/PaySchedule (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PaySchedule"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L338"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaySchedule — Projekto mokėjimo prašymo teikimo grafikas

- **Model:** `datasets/gov/finmin/sutartys/PaySchedule`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L338](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L338)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PaySchedule`
- **Primary Key (`ref`):** `pay_schedule_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_schedule_id` | `string` | — | `4` | `open` | — | Mokėjimo grafiko identifikatorius | — |
| `project` | `ref` | [Payment[project_hash]](Payment.md) | `3` | `open` | — | Šifruotas projekto identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `received` | `datetime` | `L` | `4` | `open` | — | Mokėjimo prašymo grafiko gavimo data | — |
| `revised` | `date` | `D` | `4` | `open` | — | Mokėjimo prašymo grafiko patikslinimo data | — |
| `act_impl_extension` | `boolean` | — | `4` | `open` | — | ĮI prašoma pratęsti veiklų įgyvendinimą | — |
| `extend_till` | `date` | `D` | `4` | `open` | — | Data, iki kurios prašoma pratęsti veiklų įgyvendinimą | — |
| `executor_no` | `string` | — | `4` | `open` | — | Vykdytojo nurodytas mokėjimo prašymo grafiko numeris | — |
| `executor_created` | `date` | `D` | `4` | `open` | — | Vykdytojo nurodyta mokėjimo prašymo grafiko data | — |
| `sfmis_no` | `string` | — | `4` | `open` | — | SFMIS mokėjimo prašymo grafiko numeris | — |
| `type` | `string` | — | `3` | `open` | — | Mokėjimo prašymo grafiko tipas | — |
| `state` | `string` | — | `3` | `open` | — | Mokėjimo prašymo grafiko būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | Mokėjimo prašymo grafiko būsenos data | — |
| `state_decided` | `date` | `D` | `4` | `open` | — | Mokėjimo prašymo grafiko būsenos sprendimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
