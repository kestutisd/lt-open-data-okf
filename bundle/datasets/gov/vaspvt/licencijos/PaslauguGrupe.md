---
type: Table
title: "PaslauguGrupe"
description: "Spinta table datasets/gov/vaspvt/licencijos/PaslauguGrupe (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguGrupe"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L194"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaslauguGrupe

- **Model:** `datasets/gov/vaspvt/licencijos/PaslauguGrupe`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L194](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L194)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguGrupe`
- **Primary Key (`ref`):** `paslaugu_grupes_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugu_grupes_id` | `string` | — | `2` | `open` | — | Paslaugų grupės identifikatorius | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Paslaugų grupės pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugu_grupes_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
