---
type: Table
title: "TeisineForma"
description: "Spinta table datasets/gov/vaspvt/licencijos/TeisineForma (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/TeisineForma"
tags: [gov, vaspvt, deployed, level-1]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L136"
    last_modified: "2026-11-11T14:39:20Z"
---

# TeisineForma

- **Model:** `datasets/gov/vaspvt/licencijos/TeisineForma`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L136](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L136)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/TeisineForma`
- **Primary Key (`ref`):** `teisines_formos_id`
- **Level:** `1`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teisines_formos_id` | `string` | — | `2` | `open` | — | Teisinės formos identifikatorius | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Teisinė forma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/TeisineForma", ref: "pavadinimas@lt")` | `base` | `4` | `open` | — | — | — |
| `teisines_formos_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
