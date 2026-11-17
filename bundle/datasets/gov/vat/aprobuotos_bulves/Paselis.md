---
type: Table
title: "Paselis — Pateikiama informacija apie sėkinių bulvių aprobuotus pasėlius (veislę, aprobuotą plotą, ha, pripažintą kategoriją, išbrokuotą plotą, ha, iš viso aprobuotą plotą (su išbrokuotais), ha)"
description: "Spinta table datasets/gov/vat/aprobuotos_bulves/Paselis (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/aprobuotos_bulves/Paselis"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r29_bulv_aprob.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r29_bulv_aprob.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paselis — Pateikiama informacija apie sėkinių bulvių aprobuotus pasėlius (veislę, aprobuotą plotą, ha, pripažintą kategoriją, išbrokuotą plotą, ha, iš viso aprobuotą plotą (su išbrokuotais), ha)

- **Model:** `datasets/gov/vat/aprobuotos_bulves/Paselis`[^manifest]
- **Dataset:** [datasets/gov/vat/aprobuotos_bulves](../aprobuotos_bulves.md) (`datasets/gov/vat/aprobuotos_bulves`)
- **Manifest CSV:** [datasets/gov/vat/r29_bulv_aprob.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r29_bulv_aprob.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/aprobuotos_bulves/Paselis`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Aprobavimo eilės numeris | — |
| `veisle` | `string` | — | `2` | `open` | — | Augalo veislė | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorijos kodas | — |
| `aprobuotas_plotas` | `number` | `ha` | `4` | `open` | — | Aprobuotas plotas, ha | — |
| `isbrokuotas_plotas` | `number` | `ha` | `4` | `open` | — | Išbrokuotas plotas, ha | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veisle` | `update(base: "/datasets/gov/vat/saugomos_veisles/Veisles", type: "ref", ref: "/datasets/gov/vat/saugomos_veisles/Veisles")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r29_bulv_aprob.csv
