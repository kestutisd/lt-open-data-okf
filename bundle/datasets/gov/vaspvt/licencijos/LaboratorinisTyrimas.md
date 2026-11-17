---
type: Table
title: "LaboratorinisTyrimas — Laboratoriniai tyrimai"
description: "Spinta table datasets/gov/vaspvt/licencijos/LaboratorinisTyrimas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/LaboratorinisTyrimas"
tags: [gov, vaspvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L109"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaboratorinisTyrimas — Laboratoriniai tyrimai

- **Model:** `datasets/gov/vaspvt/licencijos/LaboratorinisTyrimas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L109](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L109)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/LaboratorinisTyrimas`
- **Primary Key (`ref`):** `labor_tyrimo_id`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `labor_tyrimo_id` | `string` | — | `2` | `open` | — | Laboratorinio tyrimo identifikatorius | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos identikatorius | — |
| `eminys` | `string` | — | `4` | `open` | — | Ėminio identifikatorius | — |
| `analite` | `string` | — | `4` | `open` | — | Analitės identifikatorius | — |
| `tyrimas` | `string` | — | `4` | `open` | — | Tyrimo identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "labor_tyrimo_id")` | `ref` | `4` | `open` | — | — | — |
| `labor_tyrimo_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
