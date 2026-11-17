---
type: Table
title: "Irenginys — Lošimo bendrovių įregistruoti įrenginiai"
description: "Lošimo bendrovių įregistruotų įrenginių ir jų istorijos sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/lpt/registruoti_irenginiai/Irenginys"
tags: [gov, lpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lpt/registruoti_irenginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registruoti_irenginiai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Irenginys — Lošimo bendrovių įregistruoti įrenginiai

Lošimo bendrovių įregistruotų įrenginių ir jų istorijos sąrašas

- **Model:** `datasets/gov/lpt/registruoti_irenginiai/Irenginys`[^manifest]
- **Dataset:** [Lošimo bendrovių įregistruoti įrenginiai](../registruoti_irenginiai.md) (`datasets/gov/lpt/registruoti_irenginiai`)
- **Manifest CSV:** [datasets/gov/lpt/registruoti_irenginiai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registruoti_irenginiai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/registruoti_irenginiai/Irenginys`
- **Primary Key (`ref`):** `irenginio_registracijos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginio_registracijos_id` | `string` | — | `4` | `open` | — | Įrenginio registracijos unikalus identifikatorius | — |
| `leidimo_id` | `string` | — | `4` | `open` | — | Leidimo unikalus identifikatorius | — |
| `leidimo_dokumento_id` | `string` | — | `4` | `open` | — | Leidimo dokumento unikalus identifikatorius | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio identifikatorius | — |
| `irenginio_registracijos_numeris` | `string` | — | `4` | `open` | — | Registracijos numeris | — |
| `irenginio_pavadinimas` | `string` | — | `4` | `open` | — | Įrenginio pavadinimas, pateiktas lošimų bendrovės | — |
| `irenginio_tipo_id` | `string` | — | `4` | `open` | — | Įrenginio tipo unikalus identifikatorius | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Registracija galioja nuo | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Registracija galioja iki | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginio_pavadinimas` | `update(property: "irenginio_pavadinimas@en", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/registruoti_irenginiai.csv
