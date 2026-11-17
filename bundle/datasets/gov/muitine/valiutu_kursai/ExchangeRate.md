---
type: Table
title: "ExchangeRate"
description: "Spinta table datasets/gov/muitine/valiutu_kursai/ExchangeRate (4 columns)."
tags: [gov, muitine, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/valiutu_kursai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/valiutu_kursai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# ExchangeRate

- **Model:** `datasets/gov/muitine/valiutu_kursai/ExchangeRate`[^manifest]
- **Dataset:** [datasets/gov/muitine/valiutu_kursai](../valiutu_kursai.md) (`datasets/gov/muitine/valiutu_kursai`)
- **Manifest CSV:** [datasets/gov/muitine/valiutu_kursai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/valiutu_kursai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `currency, valid_from`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `currency` | `ref` | [/datasets/gov/muitine/valiutu_sarasas/Currency](../valiutu_sarasas/Currency.md) | `4` | `open` | — | Valiutos kodas | 3 ženklų valiutos kodas |
| `rate_eur` | `number` | — | `4` | `open` | — | Valiutos kursas | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios data | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/valiutu_kursai.csv
