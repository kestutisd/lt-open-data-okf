---
type: Table
title: "Licence — Licencija"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Licence (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Licence"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L109"
    last_modified: "2026-11-11T14:39:20Z"
---

# Licence — Licencija

- **Model:** `datasets/gov/ivpk/adp/catalog/Licence`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L109](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L109)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Licence`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `description` | `string` | — | `2` | `open` | `dct:description` | — | — |
| `identifier` | `string` | — | `5` | `open` | `dct:identifier` | Trumpas licencijos pavadinimas | — |
| `title` | `string` | — | `2` | `open` | `dct:title` | — | — |
| `url` | `string` | — | `5` | `open` | `dct:license` | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
