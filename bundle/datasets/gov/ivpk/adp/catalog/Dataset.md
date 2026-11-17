---
type: Table
title: "Dataset"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Dataset (32 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Dataset"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L238"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dataset

- **Model:** `datasets/gov/ivpk/adp/catalog/Dataset`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L238](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L238)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Dataset`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | — | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | — | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `catalog` | `ref` | [Catalog](Catalog.md) | `4` | `open` | — | — | — |
| `description` | `string` | — | `2` | `open` | `dct:description` | — | — |
| `internal_id` | `string` | — | `5` | `open` | `dct:identifier` | Rinkinio ID išoriniame kataloge | — |
| `language` | `string` | — | `2` | `open` | `dct:language` | Kalba kuria pateikti duomenys | Dviejų raidžių kalbos kodai, atskirti kableliais. |
| `licence` | `ref` | [Licence](Licence.md) | `2` | `open` | `dct:license` | — | — |
| `creator` | `ref` | [Organization](Organization.md) | `5` | `open` | `dct:creator` | — | Duomenų šaltinio autorius |
| `contributor` | `ref` | [Organization](Organization.md) | `0` | `open` | `dct:contributor` | — | Kiti autoriai prisidėję prie duomenų kūrimo |
| `publisher` | `ref` | [Organization](Organization.md) | `0` | `open` | `dct:publisher` | — | Duomenų platintojas |
| `priority_score` | `integer` | — | `4` | `open` | — | Prioriteto balas | Prioriteto balas, nuo 1 iki 100. |
| `published` | `datetime` | — | `5` | `open` | `dct:issued` | Kada paskelbta | — |
| `slug` | `string` | — | `4` | `open` | — | — | — |
| `spatial_coverage` | `string` | — | `1` | `open` | `dct:spatial` | — | — |
| `spatial_resolution` | `number` | `m` | `0` | `open` | `dcat:spatialResolutionInMeters` | — | — |
| `status` | `string` | `Status` | `4` | `open` | — | — | — |
| `tags` | `string` | — | `2` | `open` | `dcat:keyword` | Žymės | Atskirtos kableliu. |
| `temporal_coverage` | `string` | — | `2` | `open` | `dct:temporal` | — | — |
| `temporal_resolution` | `ref` | [Frequency](Frequency.md) | `0` | `open` | `dcat:temporalResolution` | — | — |
| `title` | `string` | — | `4` | `open` | `dct:title` | — | — |
| `uuid` | `string` | — | `4` | `open` | `dct:identifier` | — | — |
| `catalog2` | `ref` | [Catalog](Catalog.md) | `4` | `open` | — | — | — |
| `access_rights` | `string` | — | `2` | `open` | `dct:rights` | — | — |
| `category` | `ref` | [Category](Category.md) | `4` | `open` | `dcat:theme` | — | — |
| `distribution_conditions` | `string` | — | `1` | `open` | `odrl:hasPolicy` | — | — |
| `description_en` | `string` | — | `5` | `open` | `dct:description` | — | — |
| `last_update` | `datetime` | — | `5` | `open` | `dct:modified` | — | — |
| `title_en` | `string` | — | `5` | `open` | `dct:title` | — | — |
| `structure` | `file` | — | `3` | `open` | — | Struktūra | [Duomenų struktūros aprašas](https://atviriduomenys.readthedocs.io/dsa/index.html). |
| `frequency` | `ref` | [Frequency](Frequency.md) | `5` | `open` | `dct:accrualPeriodicity` | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `status` | `'INVENTORED'` | — | — | Atlikta inventorizacija | — |
| `status` | `'PRIORITIZED'` | — | — | Numatitas prioritetas | — |
| `status` | `'FINANCING'` | — | — | Skirtas finansavimas | — |
| `status` | `'METADATA'` | — | — | Pateikti metaduomenys | — |
| `status` | `'HAS_DATA'` | — | — | Atverti duomenys | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |
| `odrl` | `http://www.w3.org/ns/odrl/2/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
