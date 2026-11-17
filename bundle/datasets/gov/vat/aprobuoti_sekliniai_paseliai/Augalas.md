---
type: Table
title: "Augalas — Pateikiama informacija apie žemės ūkio augalų (išskyrus bulves) aprobuotus sėklinius pasėlius (augalų rūšių grupę, augalo rūšis, veislę, aprobuotą plotą ha, pripažintą kategoriją..."
description: "Spinta table datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r27_aprob_sekl_pasel.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Augalas — Pateikiama informacija apie žemės ūkio augalų (išskyrus bulves) aprobuotus sėklinius pasėlius (augalų rūšių grupę, augalo rūšis, veislę, aprobuotą plotą ha, pripažintą kategoriją...

- **Model:** `datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas`[^manifest]
- **Dataset:** [datasets/gov/vat/aprobuoti_sekliniai_paseliai](../aprobuoti_sekliniai_paseliai.md) (`datasets/gov/vat/aprobuoti_sekliniai_paseliai`)
- **Manifest CSV:** [datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Aprobavimo eilės numeris | — |
| `rusis` | `string` | — | `2` | `open` | — | Augalo rūšis | — |
| `veisle` | `string` | — | `2` | `open` | — | Augalo veislė | — |
| `kategorija` | `string` | — | `4` | `open` | — | Kategorijos kodas | — |
| `aprobuotas_plotas` | `number` | `ha` | `4` | `open` | — | Aprobuotas plotas | — |
| `isbrokuotas_plotas` | `number` | `ha` | `4` | `open` | — | Išbrokuotas plotas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veisle` | `update(base: "/datasets/gov/vat/saugomos_veisles/Veisles", type: "ref", ref: "/datasets/gov/vat/saugomos_veisles/Veisles")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r27_aprob_sekl_pasel.csv
