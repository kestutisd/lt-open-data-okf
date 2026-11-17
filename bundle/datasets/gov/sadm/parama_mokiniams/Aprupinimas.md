---
type: Table
title: "Aprupinimas — Duomenys apie paramą mokiniams"
description: "Spinta table datasets/gov/sadm/parama_mokiniams/Aprupinimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams/Aprupinimas"
tags: [gov, sadm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sadm/parama_mokiniams.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Aprupinimas — Duomenys apie paramą mokiniams

- **Model:** `datasets/gov/sadm/parama_mokiniams/Aprupinimas`[^manifest]
- **Dataset:** [datasets/gov/sadm/parama_mokiniams](../parama_mokiniams.md) (`datasets/gov/sadm/parama_mokiniams`)
- **Manifest CSV:** [datasets/gov/sadm/parama_mokiniams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams/Aprupinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje suteikta parama | — |
| `paslauga` | `string` | — | `3` | `open` | — | Suteiktos socialinės paslaugos tipas | — |
| `parama` | `string` | — | `3` | `open` | — | Suteiktos paramos kategorija | — |
| `menuo` | `date` | `D` | `4` | `open` | — | Suteiktos paslaugos menuo | — |
| `suma` | `number` | — | `2` | `open` | — | Suteiktos paramos suma | Eurais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/parama_mokiniams.csv
