---
type: Table
title: "DatasetDistribution"
description: "Spinta table datasets/gov/ivpk/adp/catalog/DatasetDistribution (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetDistribution"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L329"
    last_modified: "2026-11-11T14:39:20Z"
---

# DatasetDistribution

- **Model:** `datasets/gov/ivpk/adp/catalog/DatasetDistribution`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L329](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L329)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetDistribution`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | — | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | — | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `description` | `string` | — | `5` | `open` | `dct:description` | — | — |
| `distribution_version` | `integer` | — | `4` | `open` | — | — | — |
| `filename` | `string` | — | `4` | `open` | — | — | — |
| `identifier` | `string` | — | `5` | `open` | `dct:identifier` | — | — |
| `issued` | `date` | — | `5` | `open` | `dct:issued` | — | — |
| `mime_type` | `string` | — | `5` | `open` | `dcat:mediaType` | — | — |
| `municipality` | `string` | — | `3` | `open` | `dct:spatial` | — | — |
| `period_end` | `string` | — | `5` | `open` | `dcat:startDate` | — | — |
| `period_start` | `string` | — | `5` | `open` | `dcat:endDate` | — | — |
| `region` | `string` | — | `3` | `open` | `dct:spatial` | — | — |
| `size` | `integer` | `B` | `5` | `open` | `dcat:byteSize` | — | — |
| `title` | `string` | — | `5` | `open` | `dct:title` | — | — |
| `type` | `string` | — | `4` | `open` | — | — | — |
| `download_url` | `string` | — | `5` | `open` | `dcat:downloadURL` | — | Nuoroda į duomenų failą, naudojamas kai `type="URL"`. |
| `access_url` | `string` | — | `0` | `open` | `dcat:accessURL` | — | — |
| `dataset` | `ref` | [Dataset](Dataset.md) | `5` | `open` | `< dcat:distribution` | — | — |
| `comment` | `string` | — | — | `open` | — | — | — |
| `format` | `ref` | [Format](Format.md) | — | `open` | `dct:format` | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'FILE'` | — | — | Failas | Duomenys publikojami atvirų duomenų kataloge. |
| `type` | `'URL'` | — | — | Nuoroda | Duomenų publikuojame išorėje. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
