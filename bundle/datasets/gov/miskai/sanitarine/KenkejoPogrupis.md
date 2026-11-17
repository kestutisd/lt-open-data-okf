---
type: Table
title: "KenkejoPogrupis"
description: "Spinta table datasets/gov/miskai/sanitarine/KenkejoPogrupis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoPogrupis"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# KenkejoPogrupis

- **Model:** `datasets/gov/miskai/sanitarine/KenkejoPogrupis`[^manifest]
- **Dataset:** [datasets/gov/miskai/sanitarine](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoPogrupis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupe` | `ref` | [KenkejoGrupe](KenkejoGrupe.md) | `4` | `open` | — | Susijusi kenkėjo grupė | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Kenkėjo pogrupio pavadinimas | — |
| `kodas` | `string` | — | `3` | `open` | — | Kenkėjo pogrupio kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv
