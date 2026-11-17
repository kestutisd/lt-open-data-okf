---
type: Table
title: "PaslauguProfiliuEtapas"
description: "Spinta table datasets/gov/vaspvt/licencijos/PaslauguProfiliuEtapas (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguProfiliuEtapas"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L200"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaslauguProfiliuEtapas

- **Model:** `datasets/gov/vaspvt/licencijos/PaslauguProfiliuEtapas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L200](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L200)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguProfiliuEtapas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `3` | `open` | — | Paslaugos profilio etapo identifikatorius | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Paslaugos profilio etapo pavadinimas | — |
| `profilio_id` | `string` | — | `2` | `open` | — | Paslaugos profilio identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `profilio_id` | `update(property: "profilis", type: "ref", ref: "PaslauguProfilis")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
