---
type: Table
title: "RoadStop — Aikštelės"
description: "Spinta table datasets/gov/lakd/kelioelementai/RoadStop (10 columns)."
tags: [gov, lakd, roadstop, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/kelioelementai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lakd/kelioelementai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# RoadStop — Aikštelės

- **Model:** `datasets/gov/lakd/kelioelementai/RoadStop`[^manifest]
- **Dataset:** [datasets/gov/lakd/kelioelementai](../kelioelementai.md) (`datasets/gov/lakd/kelioelementai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/kelioelementai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/kelioelementai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `geometry` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `ref` | [StateRoad](../keliai/StateRoad.md) (`level=4 UUID`: `kelionr._id`) | `4` | `open` | — | Kelio numeris | — |
| `vietakm` | `number` | `km` | `4` | `open` | — | Kelio vieta | — |
| `kelio_puse` | `integer` | — | `4` | `open` | — | — | — |
| `vaz_dal` | `integer` | — | `4` | `open` | — | Važiuojamoji dalis | — |
| `tipas` | `integer` | — | `4` | `open` | — | Aikštelės tipas | — |
| `danga` | `string` | — | `4` | `open` | — | Dangos tipas | — |
| `plotas` | `number` | — | — | — | — | Plotas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kelio_puse` | `1` | — | — | Kairėje šalia kelio | — |
| `kelio_puse` | `2` | — | — | Dešinėje šalia kelio | — |
| `kelio_puse` | `25` | — | — | Kairėje | — |
| `kelio_puse` | `26` | — | — | Dešinėje | — |
| `vaz_dal` | `0` | — | — | Viena važiuojamoji dalis | — |
| `vaz_dal` | `1` | — | — | Pirma važiuojamoji dalis | — |
| `vaz_dal` | `2` | — | — | antra važiuojamoji dalis | — |
| `tipas` | `1` | — | — | Poilsio aikštelė | — |
| `tipas` | `2` | — | — | Sustojimo aikštelė | — |
| `tipas` | `3` | — | — | Degalinė | — |
| `danga` | `"asf"` | — | — | Asfaltbetonio danga | — |
| `danga` | `"žv"` | — | — | Žvyro, skaldos ar pan. danga be rišiklių | — |
| `danga` | `"nn"` | — | — | Nenustatyta reikšmė. Reikšmė turi būti, tačiau nėra žinoma (negalima nustatyti), neįrašyta arba prarasta | Reikšmė turi būti, tačiau nėra žinoma (negalima nustatyti), neįrašyta arba prarasta |
| `danga` | `"c"` | — | — | Plokščių (plytelių) danga | — |
| `danga` | `"tr"` | — | — | Betono trinkelių arba akmens trinkelių danga | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/kelioelementai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/kelioelementai.csv#L4)
