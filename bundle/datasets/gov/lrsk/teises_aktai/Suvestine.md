---
type: Table
title: "Suvestine — Teisės aktų suvestinių duomenys"
description: "Pateikiami duomenys apie teisės aktų suvestines."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Suvestine"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L67"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suvestine — Teisės aktų suvestinių duomenys

Pateikiami duomenys apie teisės aktų suvestines.

- **Model:** `datasets/gov/lrsk/teises_aktai/Suvestine`[^manifest]
- **Dataset:** [Teisės aktų registro duomenys](../teises_aktai.md) (`datasets/gov/lrsk/teises_aktai`)
- **Manifest CSV:** [datasets/gov/lrsk/teises_aktai.csv#L67](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L67)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Suvestine`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento unikalus identifikatorius | — |
| `suvestines_id` | `string` | — | `4` | `open` | — | Suvestinės redakcijos pagal pakeitimą identifikatorius | — |
| `nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į dokumento suvestinę | — |
| `tekstas_lt` | `string` | — | `2` | `open` | — | Dokumento suvestinės tekstas | — |
| `galioja_nuo` | `datetime` | `S` | `4` | `open` | — | Suvestinės redakcijos įsigaliojimo data | — |
| `galioja_iki` | `datetime` | `S` | `4` | `open` | — | Suvestinės redakcijos galiojimo terminas | — |
| `suv_duom_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tekstas_lt` | `update(property: "tekstas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv
