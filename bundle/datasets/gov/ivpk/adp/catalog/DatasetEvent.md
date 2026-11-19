---
type: Table
title: "DatasetEvent"
description: "Spinta table datasets/gov/ivpk/adp/catalog/DatasetEvent (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetEvent"
tags: [gov, ivpk, datasetevent, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L273"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L273"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# DatasetEvent

- **Model:** `datasets/gov/ivpk/adp/catalog/DatasetEvent`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L273](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L273)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetEvent` (`deployed`)[^manifest]
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
| `dataset` | `ref` | [Dataset](Dataset.md) (`level=4 UUID`: `dataset._id`) | `4` | `open` | — | — | — |
| `status` | `string` | `enum: Status` | `4` | `open` | — | — | — |
| `type` | `string` | — | `4` | `open` | — | — | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `status` | `'INVENTORED'` | — | — | Atlikta inventorizacija | — |
| `status` | `'PRIORITIZED'` | — | — | Numatitas prioritetas | — |
| `status` | `'FINANCING'` | — | — | Skirtas finansavimas | — |
| `status` | `'METADATA'` | — | — | Pateikti metaduomenys | — |
| `status` | `'HAS_DATA'` | — | — | Atverti duomenys | — |
| `type` | `'CREATED'` | — | — | Duomenų rinkinys sukurtas | — |
| `type` | `'DATA_ADDED'` | — | — | Pateikti duomenys | — |
| `type` | `'DATA_UPDATED'` | — | — | Atnaujinti duomenys | — |
| `type` | `'EDITED'` | — | — | Atnaujinti metaduomenys | — |
| `type` | `'STATUS_CHANGED'` | — | — | Pasikeitė būsena | — |
| `type` | `'TRANSFERRED'` | — | — | Perkeltas į kitą organizacijai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L273 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L273)
