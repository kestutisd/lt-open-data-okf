---
type: Table
title: "Geotopas — Geotopų sąrašas (katalogas)"
description: "Spinta table datasets/gov/lgt/geotopu_sarasas/Geotopas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/geotopu_sarasas/Geotopas"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/geotopai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geotopai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Geotopas — Geotopų sąrašas (katalogas)

- **Model:** `datasets/gov/lgt/geotopu_sarasas/Geotopas`[^manifest]
- **Dataset:** [Geotopų sąrašas (katalogas)](../geotopu_sarasas.md) (`datasets/gov/lgt/geotopu_sarasas`)
- **Manifest CSV:** [datasets/gov/lgt/geotopai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geotopai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/geotopu_sarasas/Geotopas`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geotopai.csv
