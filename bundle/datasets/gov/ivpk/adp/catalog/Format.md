---
type: Table
title: "Format — Duomenų formatai"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Format (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Format"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L81"
    last_modified: "2026-11-11T14:39:20Z"
---

# Format — Duomenų formatai

- **Model:** `datasets/gov/ivpk/adp/catalog/Format`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L81](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L81)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Format`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `extension` | `string` | — | `5` | `open` | `dct:identifier` | Failo plėtinys | Failo plėtinys didžiosiomis raidėmis. |
| `mimetype` | `string` | — | `2` | `open` | `dcat:mediaType` | Formato media tipas | Standartine MIME/Type forma. |
| `rating` | `integer` | — | `4` | `open` | — | Brandos lygis | Duomenų brandos lygis remiantis 5stardata.info skale. |
| `title` | `string` | — | `2` | `open` | `dct:title` | Formato pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rating` | `1` | — | — | Mašininiu būdu nenuskaitomi | — |
| `rating` | `2` | — | — | Nuosavybiniai formatai | — |
| `rating` | `3` | — | — | Atviri formatai | — |
| `rating` | `4` | — | — | Duomenys su identifikatoriais | — |
| `rating` | `5` | — | — | Standartiniai duomenys | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mimetype` | — | — | — | `open` | — | — | Šiuo metu media tipas pateikiamas laisva forma arba visai nepateikiamas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
