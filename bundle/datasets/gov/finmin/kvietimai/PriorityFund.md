---
type: Table
title: "PriorityFund — Prioriteto fondas"
description: "Spinta table datasets/gov/finmin/kvietimai/PriorityFund (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/PriorityFund"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L75"
    last_modified: "2026-11-11T14:39:20Z"
---

# PriorityFund — Prioriteto fondas

- **Model:** `datasets/gov/finmin/kvietimai/PriorityFund`[^manifest]
- **Dataset:** [datasets/gov/finmin/kvietimai](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L75](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L75)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/PriorityFund`
- **Primary Key (`ref`):** `priority_fund_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priority_fund_id` | `string` | — | `4` | `open` | — | Prioriteto ir fondo kombinacijos identifikatorius | — |
| `priority` | `ref` | [Priority](Priority.md) | `4` | `open` | — | Prioriteto identifikatorius | — |
| `fund_id` | `string` | — | `4` | `open` | — | Fondo identifikatorius | — |
| `name` | `string` | — | `4` | `open` | — | Fondo pavadinimas | — |
| `acronym` | `string` | — | `3` | `open` | — | Fondo akronimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv
