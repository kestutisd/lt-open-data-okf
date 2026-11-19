---
type: Table
title: "DatasetVisit — Duomenų rinkinio peržiūros"
description: "Šiuo metu duomenų rinkinio peržiūros fiksuojamos visiems puslapio atidarymo atvejams, greičiauisiai didžiąją dalį peržiūrų sugeneruoja paieškos botai, todėl šie skaičiai gali būti nepatikimi."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetVisit"
tags: [gov, ivpk, datasetvisit, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L367"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L367"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# DatasetVisit — Duomenų rinkinio peržiūros

Šiuo metu duomenų rinkinio peržiūros fiksuojamos visiems puslapio atidarymo atvejams, greičiauisiai didžiąją dalį peržiūrų sugeneruoja paieškos botai, todėl šie skaičiai gali būti nepatikimi.[^manifest]

- **Model:** `datasets/gov/ivpk/adp/catalog/DatasetVisit`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L367](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L367)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetVisit` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `created` | `datetime` | — | `4` | `open` | — | — | — |
| `modified` | `datetime` | — | `4` | `open` | — | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `last_visited` | `datetime` | — | `4` | `open` | — | — | — |
| `visit_count` | `integer` | — | `4` | `open` | — | Peržiūrų skaičius | — |
| `dataset` | `ref` | [Dataset](Dataset.md) (`level=4 UUID`: `dataset._id`) | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L367 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L367)
