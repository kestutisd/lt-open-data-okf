---
type: Table
title: "TarsosZidinys — Potencialūs taršos židiniai"
description: "Spinta table datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys"
tags: [gov, lgt, tarsoszidinys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1330/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/potencialus_tarsos_zidiniai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TarsosZidinys — Potencialūs taršos židiniai

- **Model:** `datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys`[^manifest]
- **Dataset:** [Potencialūs taršos židiniai](../potencialus_tarsos_zidiniai.md) (`datasets/gov/lgt/potencialus_tarsos_zidiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/potencialus_tarsos_zidiniai/TarsosZidinys` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objecto_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objecto_nr` | `integer` | — | `4` | `open` | — | Objekto numeris | — |
| `ptz_adresas` | `string` | — | `1` | `open` | — | Adresas | — |
| `ptz_anketos_nr` | `string` | — | `4` | `open` | — | Anketos numeris | — |
| `ptz_anketos_data` | `date` | `D` | `4` | `open` | — | Vertinimo data | — |
| `ptz_objekto_bukle` | `string` | — | `3` | `open` | — | Objekto būklė | — |
| `ptz_objekto_tipas` | `string` | — | `3` | `open` | — | Objekto tipas | — |
| `ptz_pavojingumas_aplinkai` | `string` | — | `3` | `open` | — | Pavojingumo aplinkai įvertinimas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Koordinatės | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/potencialus_tarsos_zidiniai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/potencialus_tarsos_zidiniai (https://data.gov.lt/datasets/1330/)
