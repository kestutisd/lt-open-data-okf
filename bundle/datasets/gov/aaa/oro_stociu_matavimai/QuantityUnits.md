---
type: Table
title: "QuantityUnits — Tarpinė lenta"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# QuantityUnits — Tarpinė lenta

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/QuantityUnits`
- **Primary Key (`ref`):** `code_combi`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code_combi` | `string` | — | `4` | `open` | — | Unikalus teršalo arba meteorologinio rodiklio ir jo matavimo vieneto numeris | — |
| `code_quantity` | `ref` | [/datasets/gov/aaa/oro_stociu_matavimai/Quantity[code_quantity]](Quantity.md) | `4` | `open` | — | Unikalus teršalo arba meteorologinio rodiklio numeris | — |
| `code_unit` | `ref` | [/datasets/gov/aaa/oro_stociu_matavimai/Units[code_unit]](Units.md) | `4` | `open` | — | Unikalus matavimo vieneto numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv
