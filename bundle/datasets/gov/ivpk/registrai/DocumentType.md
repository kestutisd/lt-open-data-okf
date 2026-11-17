---
type: Table
title: "DocumentType — Dokumento tipas"
description: "Spinta table datasets/gov/ivpk/registrai/DocumentType (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/DocumentType"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L25"
    last_modified: "2026-11-11T14:39:20Z"
---

# DocumentType — Dokumento tipas

- **Model:** `datasets/gov/ivpk/registrai/DocumentType`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L25](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L25)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/DocumentType`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `name` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `ordering` | `integer` | — | `4` | `open` | — | — | — |
| `is_establishment_law_act` | `boolean` | — | `4` | `open` | — | Yra įtvirtintas teisės aktų | — |
| `is_closing_document` | `boolean` | — | `4` | `open` | — | Yra baigamasis dokumentas | — |
| `is_refusal_to_create` | `boolean` | — | `4` | `open` | — | Atsisakymas kurti | — |
| `is_object_regulations` | `boolean` | — | `4` | `open` | — | Yra objekto reglamentai | — |
| `is_project_specification` | `boolean` | — | `4` | `open` | — | Yra projekto specifikacija | — |
| `is_acceptance_to_use` | `boolean` | — | `4` | `open` | — | Yra patvirtintas naudojimui | — |
| `updated_at` | `datetime` | `S` | `4` | `open` | — | Atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
