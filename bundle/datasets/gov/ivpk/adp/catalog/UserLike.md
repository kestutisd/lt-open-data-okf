---
type: Table
title: "UserLike — Poreikio „patinka“ paspaudimai"
description: "Spinta table datasets/gov/ivpk/adp/catalog/UserLike (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/UserLike"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L216"
    last_modified: "2026-11-11T14:39:20Z"
---

# UserLike — Poreikio „patinka“ paspaudimai

- **Model:** `datasets/gov/ivpk/adp/catalog/UserLike`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L216](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L216)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/UserLike`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `request` | `ref` | [Request](Request.md) | `4` | `open` | — | Poreikis | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
