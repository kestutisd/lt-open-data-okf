---
type: Table
title: "Comment — Komentarai"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Comment (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Comment"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L54"
    last_modified: "2026-11-11T14:39:20Z"
---

# Comment — Komentarai

- **Model:** `datasets/gov/ivpk/adp/catalog/Comment`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L54](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L54)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Comment`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | `U` | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | `U` | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `body` | `string` | — | `2` | `open` | — | Komentaro tekstas | — |
| `dataset` | `ref` | [Dataset](Dataset.md) | `4` | `open` | — | Komentuojamas duomenų rinkinys | — |
| `parent` | `integer` | — | `2` | `open` | — | Cituojamas komentaras | — |
| `request` | `ref` | [Request](Request.md) | `4` | `open` | — | Komentuojamas poreikis atverti duomenis | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
