---
type: Table
title: "ExchangeRate"
description: "Spinta table datasets/gov/muitine/valiutu_kursai/ExchangeRate (4 columns)."
tags: [gov, muitine, exchangerate, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/valiutu_kursai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/muitine/valiutu_kursai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ExchangeRate

- **Model:** `datasets/gov/muitine/valiutu_kursai/ExchangeRate`[^manifest]
- **Dataset:** [datasets/gov/muitine/valiutu_kursai](../valiutu_kursai.md) (`datasets/gov/muitine/valiutu_kursai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/valiutu_kursai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/valiutu_kursai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `currency, valid_from`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `currency` | `ref` | [Currency](../valiutu_sarasas/Currency.md) (`level=4 UUID`: `currency._id`) | `4` | `open` | — | Valiutos kodas | 3 ženklų valiutos kodas |
| `rate_eur` | `number` | — | `4` | `open` | — | Valiutos kursas | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios data | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/valiutu_kursai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/valiutu_kursai.csv#L5)
