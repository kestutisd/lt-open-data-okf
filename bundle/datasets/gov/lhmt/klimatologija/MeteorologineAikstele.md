---
type: Table
title: "MeteorologineAikstele"
description: "Spinta table datasets/gov/lhmt/klimatologija/MeteorologineAikstele (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/klimatologija/MeteorologineAikstele"
tags: [gov, lhmt, meteorologineaikstele, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/klimatologija.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lhmt/klimatologija.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1906/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lhmt/klimatologija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MeteorologineAikstele

- **Model:** `datasets/gov/lhmt/klimatologija/MeteorologineAikstele`[^manifest]
- **Dataset:** [Informacija apie meteorologijos stotis](../klimatologija.md) (`datasets/gov/lhmt/klimatologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/klimatologija.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/klimatologija.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/klimatologija/MeteorologineAikstele` (`deployed`)[^manifest]
- **Provider:** `lhmt` — Lietuvos hidrometeorologijos tarnyba (LHMT) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-sa/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `meteorologines_aikst_adr` | `string` | — | `3` | `open` | — | Meteorologinės aikštelės adresas | — |
| `mat_stotis` | `string` | — | `3` | `open` | — | Matavimo stoties pavadinimas | — |
| `aukst_virs_jur_lygio` | `number` | — | `3` | `open` | — | Vandens aukštis virš jūros lygio | — |
| `koord` | `geometry(point,4326)` | `m` | `4` | `open` | — | Meteorologinės aikštelės koordinatės (WGS) | — |
| `isteigta` | `integer` | — | `3` | `open` | — | Matavimo stoties įsteigimo metai | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/klimatologija.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/klimatologija.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lhmt/klimatologija (https://data.gov.lt/datasets/1906/)
