---
type: Table
title: "Augalas — Pateikiama informacija apie žemės ūkio augalų (išskyrus bulves) aprobuotus sėklinius pasėlius (augalų rūšių grupę, augalo rūšis, veislę, aprobuotą plotą ha, pripažintą kategoriją, išbrokuotą plotą ha, iš viso aprobuotą plotą..."
description: "Spinta table datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas"
tags: [gov, vat, augalas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1883/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/aprobuoti_sekliniai_paseliai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Augalas — Pateikiama informacija apie žemės ūkio augalų (išskyrus bulves) aprobuotus sėklinius pasėlius (augalų rūšių grupę, augalo...

- **Model:** `datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas`[^manifest]
- **Dataset:** [Ataskaita apie žemės ūkio augalų (išskyrus bulves) aprobuotus sėklinius pasėlius](../aprobuoti_sekliniai_paseliai.md) (`datasets/gov/vat/aprobuoti_sekliniai_paseliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/aprobuoti_sekliniai_paseliai/Augalas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r27_aprob_sekl_pasel.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/aprobuoti_sekliniai_paseliai (https://data.gov.lt/datasets/1883/)
