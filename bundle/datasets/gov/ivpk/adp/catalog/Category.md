---
type: Table
title: "Category — Kategorija"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Category (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Category"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L35"
    last_modified: "2026-11-11T14:39:20Z"
---

# Category — Kategorija

- **Model:** `datasets/gov/ivpk/adp/catalog/Category`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L35)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Category`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | `U` | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | `U` | `5` | `open` | `dct:modified` | Kada pakeista | Paskutinio keitimo data ir laikas. |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `description` | `string` | — | `2` | `open` | `skos:definition` | Aprašymas | — |
| `featured` | `boolean` | — | `4` | `open` | — | Iškeltas | Kategorijos kurios yra iškeltos dažniausiai rodomos pirmiausia. |
| `icon` | `string` | — | `2` | `open` | — | Piktograma | — |
| `parent` | `integer` | — | `2` | `open` | `skos:broader` | Tėvinė kategorija | — |
| `title` | `string` | — | `2` | `open` | `skos:prefLabel` | Pavadinimas | — |
| `edp_title` | `string` | — | `2` | `open` | `skos:altLabel` | Pavadinimas (EDP) | Analogiškos kategorijos pavadinimas Europos atvirų duomenų portale. |
| `title_en` | `string` | — | `2` | `open` | `skos:prefLabel` | Pavadinimas anglų kalba | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
