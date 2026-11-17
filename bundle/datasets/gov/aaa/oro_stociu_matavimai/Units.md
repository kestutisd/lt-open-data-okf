---
type: Table
title: "Units — Matavimo vienetai"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Units (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Units"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Units — Matavimo vienetai

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Units`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Units`
- **Primary Key (`ref`):** `code_unit`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code_unit` | `string` | — | `4` | `open` | — | Matavimo vieneto identifikacinis numeris | — |
| `unitname` | `string` | — | `4` | `open` | — | Matavimo vieneto pavadinimas | — |
| `id` | `string` | — | `4` | `open` | — | Matavimo vieneto identifikacinis numeris | (sutampa su code_unit) |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv
