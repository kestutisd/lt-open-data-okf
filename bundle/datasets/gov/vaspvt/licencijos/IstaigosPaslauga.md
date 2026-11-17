---
type: Table
title: "IstaigosPaslauga — Sveikatos priežiūros įstaigų paslaugos"
description: "Spinta table datasets/gov/vaspvt/licencijos/IstaigosPaslauga (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslauga"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L86"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstaigosPaslauga — Sveikatos priežiūros įstaigų paslaugos

- **Model:** `datasets/gov/vaspvt/licencijos/IstaigosPaslauga`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L86](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L86)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslauga`
- **Primary Key (`ref`):** `istaigos_paslaugos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaigos_paslaugos_id` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos paslaugos identifikatorius | — |
| `nustatymas` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos paslaugos nustatymo identifikatorius | — |
| `licenzija` | `string` | — | `4` | `open` | — | Licencija | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaiga | — |
| `filialo_id` | `string` | — | `2` | `open` | — | Filialo identifikatorius | — |
| `veiklos_adresas` | `string` | — | `4` | `open` | — | Veiklos adreso identifikatorius | — |
| `patikslinta` | `boolean` | — | `3` | `open` | — | Patikslinimo būsena | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaigos_paslaugos_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `filialo_id` | `update(property: "filialas")` | `property` | `4` | `open` | — | — | — |
| `filialo_id` | `update(type: "ref", ref: "Istaiga")` | `type` | `4` | `open` | — | — | — |
| `patikslinta` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
