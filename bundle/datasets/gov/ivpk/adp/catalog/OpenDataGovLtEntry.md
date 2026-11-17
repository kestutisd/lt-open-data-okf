---
type: Table
title: "OpenDataGovLtEntry — Informacijos rinkmenų sąrašas"
description: "Duomenys perkelti iš senojo opendata.gov.lt atvirų duomenų katalogo."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/OpenDataGovLtEntry"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L130"
    last_modified: "2026-11-11T14:39:20Z"
---

# OpenDataGovLtEntry — Informacijos rinkmenų sąrašas

Duomenys perkelti iš senojo opendata.gov.lt atvirų duomenų katalogo.

- **Model:** `datasets/gov/ivpk/adp/catalog/OpenDataGovLtEntry`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L130](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L130)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/OpenDataGovLtEntry`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `alt_title` | `string` | — | `2` | `open` | — | — | — |
| `code` | `string` | — | `5` | `open` | `dct:identifier` | Duomenų rinkinio unikalus identifikatorius | Unikalus identifikatorius opendata.gov.lt svetainės duomenų bazėje. |
| `data_extent` | `string` | — | `2` | `open` | — | — | — |
| `data_trustworthiness` | `string` | — | `2` | `open` | — | — | — |
| `dataset_begins` | `string` | — | `2` | `open` | — | — | — |
| `dataset_conditions` | `string` | — | — | `open` | — | — | — |
| `dataset_ends` | `string` | — | — | `open` | — | — | — |
| `dataset_type` | `string` | — | `3` | `open` | — | — | — |
| `date_meta_published` | `string` | — | `2` | `open` | — | — | — |
| `description` | `string` | — | — | `open` | — | — | — |
| `format` | `string` | — | `4` | `open` | — | — | — |
| `keywords` | `string` | — | `2` | `open` | — | Raktiniai žodžiai | — |
| `publisher` | `string` | — | `2` | `open` | — | Organizacija | Organizacija teikianti atvirus duomenis. |
| `refresh_period` | `string` | — | `2` | `open` | — | Atnaujinimo periodiškumas | — |
| `title` | `string` | — | `2` | `open` | — | Duomenų rinkinio pavadinimas | — |
| `topic` | `string` | — | `2` | `open` | — | Kategorija | — |
| `url` | `string` | — | `1` | `open` | `dcat:downloadURL` | Nuoroda | Nuoroda į svetainę iš kurios galima atsisiųsti duomenis arba tiesioginė nuoroda į duomenų failą. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `url` | — | — | — | `open` | — | — | Kartais nurodytas `dcat:accessURL`, kartais `dcat:downloadURL`. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
