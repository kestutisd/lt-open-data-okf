---
type: Table
title: "UsecaseDataset"
description: "Spinta table datasets/gov/ivpk/adp/catalog/UsecaseDataset (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/UsecaseDataset"
tags: [gov, ivpk, usecasedataset, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L393"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L393"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# UsecaseDataset

- **Model:** `datasets/gov/ivpk/adp/catalog/UsecaseDataset`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L393](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L393)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/UsecaseDataset` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `usecase` | `ref` | [Usecase](Usecase.md) (`level=4 UUID`: `usecase._id`) | `4` | `open` | — | — | — |
| `dataset` | `ref` | [Dataset](Dataset.md) (`level=4 UUID`: `dataset._id`) | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L393 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L393)
