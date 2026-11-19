---
type: Table
title: "Broadcasting"
description: "Spinta table datasets/gov/rrt/broadcasting/Broadcasting (15 columns)."
tags: [gov, rrt, broadcasting, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/broadcasting.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rrt/broadcasting.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Broadcasting

- **Model:** `datasets/gov/rrt/broadcasting/Broadcasting`[^manifest]
- **Dataset:** [datasets/gov/rrt/broadcasting](../broadcasting.md) (`datasets/gov/rrt/broadcasting`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/broadcasting.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/broadcasting.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `frequency_mhz` | `integer` | — | `4` | `open` | — | Centrinis siųstuvo dažnis | — |
| `bandwidth_mhz` | `number` | — | `4` | `open` | — | Kanalo plotis | — |
| `channel` | `integer` | — | `3` | `open` | — | Kanalo numeris | — |
| `antenna_height` | `integer` | `m` | `4` | `open` | — | Antenos aukštis virš žemės lygio | — |
| `licence_no` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `longitude` | `number` | — | `3` | `open` | — | Ilguma | — |
| `latitude` | `number` | — | `3` | `open` | — | Platuma | — |
| `coordinates_wgs` | `geometry(point)` | — | — | — | — | — | — |
| `erp_max_dbw` | `number` | — | `4` | `open` | — | Maksimali spinduliavimo galia ERP | — |
| `valid_from` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `valid_to` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `system_type` | `string` | — | `4` | `open` | — | Transliavimo sistemos tipas | — |
| `lic_type` | `string` | — | `3` | `open` | — | Leidimo tipas | — |
| `owner_name` | `string` | — | `3` | `open` | — | Leidimo turėtojo pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `system_type` | `"DAB"` | — | — | DAB | Skaitmeninio radijo siųstuvas |
| `system_type` | `"DVB"` | — | — | DVB | Skaitmeninės televizijos siųstuvas |
| `system_type` | `"RADIO"` | — | — | RADIO | Analoginio radijo siųstuvas |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/broadcasting.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/broadcasting.csv#L4)
