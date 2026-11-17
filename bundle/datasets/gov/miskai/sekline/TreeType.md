---
type: Table
title: "TreeType — Medžio tipas"
description: "Spinta table datasets/gov/miskai/sekline/TreeType (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline/TreeType"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L26"
    last_modified: "2026-11-11T14:39:20Z"
---

# TreeType — Medžio tipas

- **Model:** `datasets/gov/miskai/sekline/TreeType`[^manifest]
- **Dataset:** [datasets/gov/miskai/sekline](../sekline.md) (`datasets/gov/miskai/sekline`)
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L26)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline/TreeType`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `3` | `open` | — | Medžio tipo kodas | — |
| `name` | `string` | — | `3` | `open` | — | Medžio tipo pavadinimas | — |
| `group` | `ref` | [TreeTypeGroup](TreeTypeGroup.md) | `4` | `open` | — | Medžio grupė | — |
| `latin_name` | `string` | — | `3` | `open` | — | Medžio tipo lotyniškas pavadinimas | — |
| `authorlot` | `string` | — | `3` | `open` | — | Autorius (lot.) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv
