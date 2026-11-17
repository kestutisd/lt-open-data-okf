---
type: Table
title: "Quantity — Teršalai"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Quantity (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Quantity — Teršalai

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Quantity`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Quantity`
- **Primary Key (`ref`):** `code_quantity`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code_quantity` | `string` | — | `4` | `open` | — | Teršalo idenfikacinis numeris | — |
| `shortname` | `string` | — | `4` | `open` | — | Teršalo pavadinimo santrumpa | — |
| `longname` | `string` | — | `4` | `open` | — | Teršalo pavadinimas | — |
| `attrib` | `string` | — | `4` | `open` | — | Teršalo tipas | — |
| `code_unit` | `ref` | [/datasets/gov/aaa/oro_stociu_matavimai/Units[code_unit]](Units.md) | `4` | `open` | — | Matavimo vieneto identifikacinis numeris | — |
| `id` | `string` | — | `4` | `open` | — | Teršalo idenfikacinis numeris | (sutampa su code_quantity) |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv
