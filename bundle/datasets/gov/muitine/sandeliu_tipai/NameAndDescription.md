---
type: Table
title: "NameAndDescription"
description: "Spinta table datasets/gov/muitine/sandeliu_tipai/NameAndDescription (4 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/sandeliu_tipai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliu_tipai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# NameAndDescription

- **Model:** `datasets/gov/muitine/sandeliu_tipai/NameAndDescription`[^manifest]
- **Dataset:** [datasets/gov/muitine/sandeliu_tipai](../sandeliu_tipai.md) (`datasets/gov/muitine/sandeliu_tipai`)
- **Manifest CSV:** [datasets/gov/muitine/sandeliu_tipai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliu_tipai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Rinkinio identifikacinis numeris | — |
| `metadata` | `ref` | [Metadata](Metadata.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `language_code` | `string` | — | `3` | `open` | — | Kalbos kodas | 2 simbolių šalies kodas |
| `name` | `string` | — | `3` | `open` | — | Sąrašo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/sandeliu_tipai.csv
