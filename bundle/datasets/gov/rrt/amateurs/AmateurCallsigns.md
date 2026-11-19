---
type: Table
title: "AmateurCallsigns"
description: "Spinta table datasets/gov/rrt/amateurs/AmateurCallsigns (7 columns)."
tags: [gov, rrt, amateurcallsigns, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/amateurs.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rrt/amateurs.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AmateurCallsigns

- **Model:** `datasets/gov/rrt/amateurs/AmateurCallsigns`[^manifest]
- **Dataset:** [datasets/gov/rrt/amateurs](../amateurs.md) (`datasets/gov/rrt/amateurs`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/amateurs.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/amateurs.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `cert_class` | `"A"` | — | — | A | — |
| `cert_class` | `"B"` | — | — | B | — |
| `cert_class` | `null` | — | — | — | — |
| `type` | `"Klubinis"` | — | — | Klubinis | — |
| `type` | `"Individualus"` | — | — | Individualus | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/amateurs.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/amateurs.csv#L4)
