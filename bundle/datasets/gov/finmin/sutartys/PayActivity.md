---
type: Table
title: "PayActivity — Projekto mokėjimo prašymo dalies Nr. 1 veiklos"
description: "Spinta table datasets/gov/finmin/sutartys/PayActivity (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayActivity"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L238"
    last_modified: "2026-11-11T14:39:20Z"
---

# PayActivity — Projekto mokėjimo prašymo dalies Nr. 1 veiklos

- **Model:** `datasets/gov/finmin/sutartys/PayActivity`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L238](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L238)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayActivity`
- **Primary Key (`ref`):** `pay_activity_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_activity_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies veiklos identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | MPD1 veiklos numeris | — |
| `from` | `date` | `M` | `4` | `open` | — | Faktinio veiklos vykdymo laikotarpio pradžia (metai ir mėnuo) | — |
| `till` | `date` | `M` | `4` | `open` | — | Faktinio veiklos vykdymo laikotarpio pabaiga (metai ir mėnuo) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
