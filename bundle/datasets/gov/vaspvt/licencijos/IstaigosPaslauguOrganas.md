---
type: Table
title: "IstaigosPaslauguOrganas — Sveikatos priežiūros įstaigų paslaugų organai"
description: "Spinta table datasets/gov/vaspvt/licencijos/IstaigosPaslauguOrganas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslauguOrganas"
tags: [gov, vaspvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L99"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstaigosPaslauguOrganas — Sveikatos priežiūros įstaigų paslaugų organai

- **Model:** `datasets/gov/vaspvt/licencijos/IstaigosPaslauguOrganas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L99](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L99)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslauguOrganas`
- **Primary Key (`ref`):** `id`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslauga | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "id")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
