---
type: Table
title: "Istaiga — Įstaigos"
description: "Spinta table datasets/gov/hi/lovos/Istaiga (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/lovos/Istaiga"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/lovos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Istaiga — Įstaigos

- **Model:** `datasets/gov/hi/lovos/Istaiga`[^manifest]
- **Dataset:** [Stacionaro lovų skaičius ir jų veiklos rodikliai](../lovos.md) (`datasets/gov/hi/lovos`)
- **Manifest CSV:** [datasets/gov/hi/lovos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/lovos/Istaiga`
- **Primary Key (`ref`):** `istg_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istg_id` | `string` | — | `4` | `open` | — | Įstaigos ID | — |
| `ist_kodas` | `ref` | [/datasets/gov/vaspvt/licencijos/Istaiga[ja_kodas]](../../vaspvt/licencijos/Istaiga.md) | `3` | `open` | — | Įstaigos JAR kodas | — |
| `ist_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/lovos.csv
