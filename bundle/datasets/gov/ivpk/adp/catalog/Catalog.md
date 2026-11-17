---
type: Table
title: "Catalog — Atvirų duomenų katalogas"
description: "Atvirų duomenų katalogas, kuris yra sinchronizuojamas su Lietuvos atvirų duomenų katalogu."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Catalog"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L223"
    last_modified: "2026-11-11T14:39:20Z"
---

# Catalog — Atvirų duomenų katalogas

Atvirų duomenų katalogas, kuris yra sinchronizuojamas su Lietuvos atvirų duomenų katalogu.

- **Model:** `datasets/gov/ivpk/adp/catalog/Catalog`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L223](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L223)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Catalog`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | — | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | — | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `description` | `string` | — | `2` | `open` | `dct:description` | — | — |
| `identifier` | `string` | — | `4` | `open` | `dct:identifier` | — | — |
| `slug` | `string` | — | `4` | `open` | `dct:identifier` | — | — |
| `title` | `string` | — | `2` | `open` | `dct:title` | — | — |
| `licence` | `ref` | [Licence](Licence.md) | `4` | `open` | `dct:license` | — | — |
| `title_en` | `string` | — | `2` | `open` | `dct:title` | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
