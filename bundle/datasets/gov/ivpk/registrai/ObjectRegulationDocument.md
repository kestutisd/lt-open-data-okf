---
type: Table
title: "ObjectRegulationDocument — Objektų reglamentavimo dokumentai"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectRegulationDocument (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectRegulationDocument"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L202"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjectRegulationDocument — Objektų reglamentavimo dokumentai

- **Model:** `datasets/gov/ivpk/registrai/ObjectRegulationDocument`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L202](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L202)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectRegulationDocument`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `regulation_type` | `string` | — | `3` | `open` | — | Reglamentavimo tipas | — |
| `name` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `number` | `string` | — | `4` | `open` | — | Numeris | — |
| `acceptance_date` | `date` | `D` | `4` | `open` | — | Priėmimo data | — |
| `effective_date` | `date` | `D` | `4` | `open` | — | Įsteigimo data | — |
| `establishment_date` | `date` | `D` | `4` | `open` | — | Įtvirtinimo data | — |
| `commencement_date` | `date` | `D` | `4` | `open` | — | Pradžios data | — |
| `publication_in_press` | `string` | — | `2` | `open` | — | Publikavimas spaudoje | — |
| `url` | `string` | — | `4` | `open` | — | Svetainės adresas | — |
| `object` | `integer` | — | `1` | `open` | — | Objektas | — |
| `status` | `ref` | [ProvisionAndSpecificationStatus](ProvisionAndSpecificationStatus.md) | `4` | `open` | — | Nuostatų ir specifikacijos statusas | — |
| `type` | `integer` | — | `1` | `open` | — | Dokumento tipas | — |
| `data_providers` | `string` | — | `2` | `open` | — | Duomenų teikėjai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
