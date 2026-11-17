---
type: Table
title: "AmateurCallsigns"
description: "Spinta table datasets/gov/rrt/amateurs/AmateurCallsigns (7 columns)."
tags: [gov, rrt, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/amateurs.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/amateurs.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# AmateurCallsigns

- **Model:** `datasets/gov/rrt/amateurs/AmateurCallsigns`[^manifest]
- **Dataset:** [datasets/gov/rrt/amateurs](../amateurs.md) (`datasets/gov/rrt/amateurs`)
- **Manifest CSV:** [datasets/gov/rrt/amateurs.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/amateurs.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `code` | `string` | — | `3` | `open` | — | Leidimo pavadinimas | — |
| `licence_no` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `call_sign` | `string` | — | `3` | `open` | — | Šaukinys | — |
| `cert_class` | `string` | — | `4` | `open` | — | CERT klasė | — |
| `type` | `string` | — | `4` | `open` | — | Leidimo tipas (klubui arba asmeniui) | — |
| `expire_date` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `cert_class` | `"A"` | — | — | A | — |
| `cert_class` | `"B"` | — | — | B | — |
| `cert_class` | `null` | — | — | — | — |
| `type` | `"Klubinis"` | — | — | Klubinis | — |
| `type` | `"Individualus"` | — | — | Individualus | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/amateurs.csv
