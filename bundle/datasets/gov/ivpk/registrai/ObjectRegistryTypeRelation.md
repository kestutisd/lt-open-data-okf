---
type: Table
title: "ObjectRegistryTypeRelation — Objektų registrų tipai ir ryšiai"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectRegistryTypeRelation (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectRegistryTypeRelation"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L196"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjectRegistryTypeRelation — Objektų registrų tipai ir ryšiai

- **Model:** `datasets/gov/ivpk/registrai/ObjectRegistryTypeRelation`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L196](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L196)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectRegistryTypeRelation`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `object` | `integer` | — | `1` | `open` | — | Objektas | — |
| `registry_type` | `integer` | — | `1` | `open` | — | Registro tipas | — |
| `updated_at` | `datetime` | `S` | `4` | `open` | — | Atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
