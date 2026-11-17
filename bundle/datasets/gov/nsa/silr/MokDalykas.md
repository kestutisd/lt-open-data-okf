---
type: Table
title: "MokDalykas — Mokinių lankomumo duomenų mokomųjų dalykų klasifikatorius"
description: "Spinta table datasets/gov/nsa/silr/MokDalykas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/silr/MokDalykas"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# MokDalykas — Mokinių lankomumo duomenų mokomųjų dalykų klasifikatorius

- **Model:** `datasets/gov/nsa/silr/MokDalykas`[^manifest]
- **Dataset:** [Švietimo įstaigų lankomumo rodikliai](../silr.md) (`datasets/gov/nsa/silr`)
- **Manifest CSV:** [datasets/gov/nsa/silr/silr.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/silr/MokDalykas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `dienynas` | `string` | — | `4` | `open` | — | Mokyklos naudojamo elektroninio dienyno pavadinimas (NAŠC arba Tamo) | — |
| `mokdal_kodas` | `string` | — | `4` | `open` | — | Mokomojo dalyko kodas | — |
| `mokdal_pav` | `string` | — | `4` | `open` | — | Mokomojo dalyko pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv
