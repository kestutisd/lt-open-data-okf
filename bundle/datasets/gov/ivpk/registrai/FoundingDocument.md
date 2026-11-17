---
type: Table
title: "FoundingDocument — Objekto steigimo dokumentas"
description: "Spinta table datasets/gov/ivpk/registrai/FoundingDocument (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/FoundingDocument"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L131"
    last_modified: "2026-11-11T14:39:20Z"
---

# FoundingDocument — Objekto steigimo dokumentas

- **Model:** `datasets/gov/ivpk/registrai/FoundingDocument`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L131](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L131)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/FoundingDocument`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `name` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `number` | `string` | — | `4` | `open` | — | Numeris | — |
| `acceptance_date` | `date` | `D` | `4` | `open` | — | Priėmimo data | — |
| `effective_date` | `string` | — | `2` | `open` | — | Įsigaliojimo data | — |
| `publication_in_press` | `string` | — | `2` | `open` | — | Publikacija spaudoje | — |
| `url` | `string` | — | `4` | `open` | — | Svetainės adresas | — |
| `object` | `integer` | — | `1` | `open` | — | Objektas | — |
| `status` | `ref` | [ProvisionAndSpecificationStatus](ProvisionAndSpecificationStatus.md) | `4` | `open` | — | Nuostatų ir specifikacijų statuso ID | — |
| `type` | `integer` | — | `1` | `open` | — | Dokumento tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
