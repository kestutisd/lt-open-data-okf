---
type: Table
title: "NameAndDescription"
description: "Spinta table datasets/gov/muitine/sandeliai/NameAndDescription (4 columns)."
tags: [gov, muitine, nameanddescription, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/muitine/sandeliai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# NameAndDescription

- **Model:** `datasets/gov/muitine/sandeliai/NameAndDescription`[^manifest]
- **Dataset:** [datasets/gov/muitine/sandeliai](../sandeliai.md) (`datasets/gov/muitine/sandeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/sandeliai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Rinkinio identifikacinis numeris | — |
| `metadata` | `ref` | [Metadata](Metadata.md) (`level=4 UUID`: `metadata._id`) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `language_code` | `string` | — | `3` | `open` | — | Kalbos kodas | 2 simbolių šalies kodas |
| `name` | `string` | — | `3` | `open` | — | Sąrašo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/sandeliai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliai.csv#L10)
