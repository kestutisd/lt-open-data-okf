---
type: Table
title: "RequestEvent"
description: "Spinta table datasets/gov/ivpk/adp/catalog/RequestEvent (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestEvent"
tags: [gov, ivpk, requestevent, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L376"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L376"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# RequestEvent

- **Model:** `datasets/gov/ivpk/adp/catalog/RequestEvent`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L376](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L376)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestEvent` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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
| `request` | `ref` | [Request](Request.md) (`level=4 UUID`: `request._id`) | `4` | `open` | — | — | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'CREATED'` | — | — | — | — |
| `type` | `'ASSIGNED'` | — | — | — | — |
| `type` | `'EDITED'` | — | — | — | — |
| `type` | `'APPROVED'` | — | — | — | — |
| `type` | `'REJECTED'` | — | — | — | — |
| `type` | `'STATUS_CHANGED'` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L376 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L376)
