---
type: Table
title: "PaslauguProfilis"
description: "Spinta table datasets/gov/vaspvt/licencijos/PaslauguProfilis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguProfilis"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L157"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaslauguProfilis

- **Model:** `datasets/gov/vaspvt/licencijos/PaslauguProfilis`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L157](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L157)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguProfilis`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Paslaugos profilio identifikatorius | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Paslaugos profilio pavadinimas | — |
| `paslaugos_id` | `string` | — | `2` | `open` | — | Paslaugos identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_id` | `update(property: "paslauga", type: "ref", ref: "IstaigosPaslauga")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
