---
type: Table
title: "VeiklosAdresoPaslauga — Veiklos adresų paslaugos"
description: "Spinta table datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga"
tags: [gov, vaspvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L118"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeiklosAdresoPaslauga — Veiklos adresų paslaugos

- **Model:** `datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L118](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L118)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga`
- **Primary Key (`ref`):** `veiklos_adreso_paslaugos_id`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veiklos_adreso_paslaugos_id` | `string` | — | `2` | `open` | — | Veiklos adreso paslaugos identifikatorius | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos identifikatorius | — |
| `paslaugos_lygis` | `string` | — | `4` | `open` | — | Paslaugos lygio identifikatorius | — |
| `paslaugos_budo_id` | `string` | — | `2` | `open` | — | Paslaugos būdo identifikatorius | — |
| `paslaugos_grupe` | `string` | — | `4` | `open` | — | Paslaugos grupės identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "veiklos_adreso_paslaugos_id")` | `ref` | `4` | `open` | — | — | — |
| `veiklos_adreso_paslaugos_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `paslaugos_budo_id` | `update(property: "paslaugu_lygis")` | `property` | `4` | `open` | — | — | — |
| `paslaugos_budo_id` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
