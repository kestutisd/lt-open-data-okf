---
type: Table
title: "Skolininkai"
description: "Spinta table datasets/gov/vsdfv/ds/Skolininkai (6 columns)."
tags: [gov, vsdfv, skolininkai, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Skolininkai

- **Model:** `datasets/gov/vsdfv/ds/Skolininkai`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/ds](../ds.md) (`datasets/gov/vsdfv/ds`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/ds.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `draudeju_grupe, draudeju_tipas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | — |
| `draudeju_tipas` | `ref` | [Draudejai](Draudejai.md) (`level=4 UUID`: `draudeju_tipas._id`) | `4` | `open` | — | Draudėjų tipas | — |
| `draudeju_grupe` | `ref` | [Draudejai](Draudejai.md) (`level=4 UUID`: `draudeju_grupe._id`) | `4` | `open` | — | Draudėjų grupė | — |
| `draudeju_sk` | `integer` | — | `4` | `open` | — | Skolingų draudėjų skaičius | Draudėjų, laiku į Valstybinio socialinio draudimo fondo biudžetą (toliau – Fondo biudžetas) nesumokėjusių priskaičiuotų socialinio draudimo įmokų, palūkanų, baudų ir delspinigių, skaičius (ataskaitinio laikotarpio pabaigoje). |
| `skola_eur` | `number` | — | `2` | `open` | — | Draudėjų skola, Eur | Draudėjams priskaičiuotų, tačiau laiku į Fondo biudžetą nesumokėtų socialinio draudimo įmokų, palūkanų, baudų ir delspinigių suma (ataskaitinio laikotarpio pabaigoje). |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `skola_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L16)
