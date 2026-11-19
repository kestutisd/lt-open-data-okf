---
type: Table
title: "Geotopas — Geotopų sąrašas (katalogas)"
description: "Spinta table datasets/gov/lgt/geotopu_sarasas/Geotopas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/geotopu_sarasas/Geotopas"
tags: [gov, lgt, geotopas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geotopai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lgt/geotopai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1326/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/geotopu_sarasas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Geotopas — Geotopų sąrašas (katalogas)

- **Model:** `datasets/gov/lgt/geotopu_sarasas/Geotopas`[^manifest]
- **Dataset:** [Geotopų sąrašas (katalogas)](../geotopu_sarasas.md) (`datasets/gov/lgt/geotopu_sarasas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/geotopai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geotopai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/geotopu_sarasas/Geotopas` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Įrašo eilės numeris | — |
| `tipas` | `string` | — | `3` | `open` | — | Geotopo tipas | — |
| `koord` | `geometry(point,3346)` | `m` | `4` | `open` | — | Taškas | — |
| `vardas` | `string` | — | `4` | `open` | — | Geotopo vardas | — |
| `sinonimai` | `string` | — | `4` | `open` | — | Geotopo vardo sinonimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Geotopo adresas | — |
| `aprasymas` | `string` | — | `2` | `open` | — | Geotopo vietovės aprašymas | — |
| `matmuo_1` | `string` | — | `4` | `open` | — | Matmuo 1 | — |
| `reiksme_1` | `string` | — | `4` | `open` | — | Matmens reikšmė | — |
| `matmuo_2` | `string` | — | `4` | `open` | — | Matmuo 2 | — |
| `reiksme_2` | `string` | — | `4` | `open` | — | Matmens reikšmė | — |
| `matmuo_3` | `string` | — | `4` | `open` | — | Matmuo 3 | — |
| `reiksme_3` | `string` | — | `4` | `open` | — | Matmens reikšmė | — |
| `matmuo_4` | `string` | — | `4` | `open` | — | Matmuo 4 | — |
| `reiksme_4` | `string` | — | `4` | `open` | — | Matmens reikšmė | — |
| `sudetis` | `string` | — | `2` | `open` | — | Sudėtis | — |
| `unikalumas` | `string` | — | `2` | `open` | — | Unikalumas | — |
| `autorius` | `string` | — | `2` | `open` | — | Geotopo aprašo autorius | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geotopai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geotopai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/geotopu_sarasas (https://data.gov.lt/datasets/1326/)
