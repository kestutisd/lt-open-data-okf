---
type: Table
title: "PaslauguNustatymas"
description: "Spinta table datasets/gov/vaspvt/licencijos/PaslauguNustatymas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguNustatymas"
tags: [gov, vaspvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L143"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaslauguNustatymas

- **Model:** `datasets/gov/vaspvt/licencijos/PaslauguNustatymas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L143](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L143)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguNustatymas`
- **Primary Key (`ref`):** `paslaugos_nustatymo_id`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_nustatymo_id` | `string` | — | `2` | `open` | — | Paslaugos nustatymo identifikatorius | — |
| `paslaugos_budas` | `string` | — | `2` | `open` | — | Paslaugos būdo identifikatorius | — |
| `paslaugos_id` | `string` | — | `2` | `open` | — | Paslaugos identifikatorius | — |
| `paslaugos_grupes_id` | `string` | — | `2` | `open` | — | Paslaugos grupės identifikatorius | — |
| `paslaugos_lygio_id` | `string` | — | `2` | `open` | — | Paslaugos lygio identifikatorius | — |
| `paslaugos_tipo_id` | `string` | — | `2` | `open` | — | Paslaugos tipo identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_nustatymo_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `paslaugos_budas` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `paslaugos_id` | `update(property: "paslauga", type: "ref", ref: "IstaigosPaslauga")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_grupes_id` | `update(property: "paslaugu_grupe", type: "ref", ref: "PaslauguGrupe")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_lygio_id` | `update(property: "paslaugu_lygis", type: "ref", ref: "PaslauguLygis")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_tipo_id` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
