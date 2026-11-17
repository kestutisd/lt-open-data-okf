---
type: Table
title: "IstaigosVeiklosAdresas — Sveikatos priežiūros įstaigų veiklos adresai"
description: "Spinta table datasets/gov/vaspvt/licencijos/IstaigosVeiklosAdresas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosVeiklosAdresas"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L76"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstaigosVeiklosAdresas — Sveikatos priežiūros įstaigų veiklos adresai

- **Model:** `datasets/gov/vaspvt/licencijos/IstaigosVeiklosAdresas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L76](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L76)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosVeiklosAdresas`
- **Primary Key (`ref`):** `spi_veiklos_adreso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `spi_veiklos_adreso_id` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos veiklos adreso identifikatorius | — |
| `adreso_id` | `string` | — | `1` | `open` | — | Adreso identifikatorius | — |
| `adresas` | `string` | — | `1` | `open` | — | Adresas | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos identifikatorius | — |
| `filialas` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos filialas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `spi_veiklos_adreso_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `adreso_id` | `update(type: "ref", ref: "/datasets/gov/rc/ar/patalpa/Patalpa")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/patalpa/Patalpa")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
