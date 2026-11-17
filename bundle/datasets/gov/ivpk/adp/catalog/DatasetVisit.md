---
type: Table
title: "DatasetVisit — Duomenų rinkinio peržiūros"
description: "Šiuo metu duomenų rinkinio peržiūros fiksuojamos visiems puslapio atidarymo atvejams, greičiauisiai didžiąją dalį peržiūrų sugeneruoja paieškos botai, todėl šie skaičiai gali būti nepatikimi."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetVisit"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L367"
    last_modified: "2026-11-11T14:39:20Z"
---

# DatasetVisit — Duomenų rinkinio peržiūros

Šiuo metu duomenų rinkinio peržiūros fiksuojamos visiems puslapio atidarymo atvejams, greičiauisiai didžiąją dalį peržiūrų sugeneruoja paieškos botai, todėl šie skaičiai gali būti nepatikimi.

- **Model:** `datasets/gov/ivpk/adp/catalog/DatasetVisit`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L367](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L367)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetVisit`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `created` | `datetime` | — | `4` | `open` | — | — | — |
| `modified` | `datetime` | — | `4` | `open` | — | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `last_visited` | `datetime` | — | `4` | `open` | — | — | — |
| `visit_count` | `integer` | — | `4` | `open` | — | Peržiūrų skaičius | — |
| `dataset` | `ref` | [Dataset](Dataset.md) | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
