---
type: Table
title: "RequestEvent"
description: "Spinta table datasets/gov/ivpk/adp/catalog/RequestEvent (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestEvent"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L376"
    last_modified: "2026-11-11T14:39:20Z"
---

# RequestEvent

- **Model:** `datasets/gov/ivpk/adp/catalog/RequestEvent`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L376](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L376)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestEvent`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `created` | `datetime` | — | `4` | `open` | — | — | — |
| `deleted` | `string` | — | `4` | `open` | — | — | — |
| `deleted_on` | `datetime` | — | `4` | `open` | — | — | — |
| `modified` | `datetime` | — | `4` | `open` | — | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `comment` | `string` | — | `4` | `open` | — | — | — |
| `type` | `string` | — | `4` | `open` | — | — | — |
| `request` | `ref` | [Request](Request.md) | `4` | `open` | — | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'CREATED'` | — | — | — | — |
| `type` | `'ASSIGNED'` | — | — | — | — |
| `type` | `'EDITED'` | — | — | — | — |
| `type` | `'APPROVED'` | — | — | — | — |
| `type` | `'REJECTED'` | — | — | — | — |
| `type` | `'STATUS_CHANGED'` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
