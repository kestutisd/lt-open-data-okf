---
type: Table
title: "ExternalSite — Išorinis atvirų duomenų katalogas"
description: "Spinta table datasets/gov/ivpk/adp/catalog/ExternalSite (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/ExternalSite"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L66"
    last_modified: "2026-11-11T14:39:20Z"
---

# ExternalSite — Išorinis atvirų duomenų katalogas

- **Model:** `datasets/gov/ivpk/adp/catalog/ExternalSite`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L66](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L66)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/ExternalSite`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | `U` | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | `U` | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `image` | `string` | — | `2` | `open` | — | Paveiksliukas | — |
| `title` | `string` | — | `2` | `open` | `dct:title` | Katalogo pavadinimas | — |
| `type` | `string` | — | — | `open` | — | — | — |
| `url` | `string` | — | — | `open` | — | Nuoroda į katalogą | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `'EU_COMISSION_PORTAL'` | — | — | Europos komisija | — |
| `type` | `'EU_LAND'` | — | — | Europos šalys | — |
| `type` | `'OTHER_LAND'` | — | — | Kitos šalys | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
