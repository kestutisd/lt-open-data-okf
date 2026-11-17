---
type: Table
title: "Skolininkai"
description: "Spinta table datasets/gov/vsdfv/ds/Skolininkai (6 columns)."
tags: [gov, vsdfv, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L16"
    last_modified: "2026-11-11T14:39:20Z"
---

# Skolininkai

- **Model:** `datasets/gov/vsdfv/ds/Skolininkai`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/ds](../ds.md) (`datasets/gov/vsdfv/ds`)
- **Manifest CSV:** [datasets/gov/vsdfv/ds.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L16)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `draudeju_grupe, draudeju_tipas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | — |
| `draudeju_tipas` | `ref` | [Draudejai](Draudejai.md) | `4` | `open` | — | Draudėjų tipas | — |
| `draudeju_grupe` | `ref` | [Draudejai](Draudejai.md) | `4` | `open` | — | Draudėjų grupė | — |
| `draudeju_sk` | `integer` | — | `4` | `open` | — | Skolingų draudėjų skaičius | Draudėjų, laiku į Valstybinio socialinio draudimo fondo biudžetą (toliau – Fondo biudžetas) nesumokėjusių priskaičiuotų socialinio draudimo įmokų, palūkanų, baudų ir delspinigių, skaičius (ataskaitinio laikotarpio pabaigoje). |
| `skola_eur` | `number` | — | `2` | `open` | — | Draudėjų skola, Eur | Draudėjams priskaičiuotų, tačiau laiku į Fondo biudžetą nesumokėtų socialinio draudimo įmokų, palūkanų, baudų ir delspinigių suma (ataskaitinio laikotarpio pabaigoje). |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `skola_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv
