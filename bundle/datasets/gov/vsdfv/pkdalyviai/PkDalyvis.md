---
type: Table
title: "PkDalyvis"
description: "Spinta table datasets/gov/vsdfv/pkdalyviai/PkDalyvis (5 columns)."
tags: [gov, vsdfv, pkdalyvis, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PkDalyvis

- **Model:** `datasets/gov/vsdfv/pkdalyviai/PkDalyvis`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/pkdalyviai](../pkdalyviai.md) (`datasets/gov/vsdfv/pkdalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/pkdalyviai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metai, menuo`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžiaus grupė | — |
| `dalyviu_skaicius` | `integer` | — | `4` | `open` | — | Dalyvių skaičius, vnt. | Iš viso pensijų kaupimo dalyvių skaičius |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"vyrai"` | — | — | Vyrai | — |
| `lytis` | `"moterys"` | — | — | Moterys | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkdalyviai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkdalyviai.csv#L6)
