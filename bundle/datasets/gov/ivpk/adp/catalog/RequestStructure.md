---
type: Table
title: "RequestStructure — Pageidaujamos duomenų struktūros laukas"
description: "Teikiant prašymus gauti duomenis yra galimybė pateikti kokių konkrečių duomenų laukų reikia arba trūksta duomenų rinkinyje."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestStructure"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L201"
    last_modified: "2026-11-11T14:39:20Z"
---

# RequestStructure — Pageidaujamos duomenų struktūros laukas

Teikiant prašymus gauti duomenis yra galimybė pateikti kokių konkrečių duomenų laukų reikia arba trūksta duomenų rinkinyje. Šioje lentelėje saugomi prašomi atverti duomenų laukai.

- **Model:** `datasets/gov/ivpk/adp/catalog/RequestStructure`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L201](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L201)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestStructure`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `data_notes` | `string` | — | `2` | `open` | `dct:description` | Pastabos | Duomenų struktūros apraše `comment` eilutė. |
| `data_title` | `string` | — | `2` | `open` | — | Duomenų lauko antraštė | Duomenų struktūros apraše `title`. |
| `data_type` | `string` | — | `1` | `open` | — | Duomenų lauko tipas | Duomenų struktūros apraše `type`. |
| `dictionary_title` | `string` | — | `1` | `open` | — | Duomenų kodinis pavadinimas | Duomenų struktūros apraše `model/property` arba `uri`. |
| `request` | `ref` | [Request](Request.md) | `4` | `open` | — | Poreikis duomenų rinkiniui | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dictionary_title` | — | `type` | — | `open` | — | — | Nėra susiejim su struktūros aprašu, laisvas tekstas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv
