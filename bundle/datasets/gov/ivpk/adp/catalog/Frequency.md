---
type: Table
title: "Frequency — Periodiškumas"
description: "Duomenų atnaujinimo periodiškumas"
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Frequency"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L98"
    last_modified: "2026-11-11T14:39:20Z"
---

# Frequency — Periodiškumas

Duomenų atnaujinimo periodiškumas

- **Model:** `datasets/gov/ivpk/adp/catalog/Frequency`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L98](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L98)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Frequency`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `title` | `string` | — | `2` | `open` | `dct:title` | Pavadinimas | — |
| `title_en` | `string` | — | `2` | `open` | `dct:title` | Pavadinimas anglų kalba | — |
| `uri` | `string` | — | `5` | `open` | `dct:accrualPeriodicity` | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
