---
type: Table
title: "VandensMatavimoStotis"
description: "Spinta table datasets/gov/lhmt/hidrologija/VandensMatavimoStotis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/hidrologija/VandensMatavimoStotis"
tags: [gov, lhmt, vandensmatavimostotis, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/hidrologija.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lhmt/hidrologija.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/594/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lhmt/hidrologija"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# VandensMatavimoStotis

- **Model:** `datasets/gov/lhmt/hidrologija/VandensMatavimoStotis`[^manifest]
- **Dataset:** [Informacija apie vandens matavimo stotis](../hidrologija.md) (`datasets/gov/lhmt/hidrologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/hidrologija.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/hidrologija.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/hidrologija/VandensMatavimoStotis` (`deployed`)[^manifest]
- **Provider:** `lhmt` — Lietuvos hidrometeorologijos tarnyba (LHMT) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by-sa/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vms` | `string` | — | `3` | `open` | — | vandens matavimo stotis | — |
| `vand_telk_pvd` | `string` | — | `3` | `open` | — | vandens telkinio pavadinimas | — |
| `ats_nuo_ziociu` | `number` | — | `3` | `open` | — | atstumas nuo žiočių, km | — |
| `koord` | `geometry(point,4326)` | `m` | `4` | `open` | — | vandens matavimo stoties koordinatės (WGS) | — |
| `isteigta` | `integer` | — | `3` | `open` | — | vandens matavimo stoties įsteigimo metai | — |
| `vand_telk_tipas` | `string` | — | `3` | `open` | — | vandens telkinio tipas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/hidrologija.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/hidrologija.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lhmt/hidrologija (https://data.gov.lt/datasets/594/)
