---
type: Table
title: "Request"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Request (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Request"
tags: [gov, ivpk, request, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L288"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L288"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Request

- **Model:** `datasets/gov/ivpk/adp/catalog/Request`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L288](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L288)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Request` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `created` | `datetime` | — | `4` | `open` | — | — | — |
| `modified` | `datetime` | — | `4` | `open` | — | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `comment` | `string` | — | `4` | `open` | — | — | — |
| `dataset` | `ref` | [Dataset](Dataset.md) (`level=4 UUID`: `dataset._id`) | `4` | `open` | — | — | — |
| `description` | `string` | — | `4` | `open` | — | — | — |
| `format` | `string` | — | `2` | `open` | — | — | Kableliu atskirtas formatų sąrašas. |
| `is_existing` | `boolean` | — | `4` | `open` | — | — | — |
| `organization` | `ref` | [Organization](Organization.md) (`level=4 UUID`: `organization._id`) | `4` | `open` | — | — | Organizacija, kuriai nukreiptas poreikis. |
| `periodicity` | `string` | — | `3` | `open` | — | — | Pageidaujamas duomnų atnaujinimo dažnumas. |
| `planned_opening_date` | `date` | — | `4` | `open` | — | — | Data, kada planuojama atverti duomenis. |
| `purpose` | `string` | — | `2` | `open` | — | — | Kableliu atskirtas sąrašas panaudojimo atvejų. |
| `slug` | `string` | — | `4` | `open` | — | — | — |
| `status` | `string` | — | `4` | `open` | — | — | — |
| `title` | `string` | — | `4` | `open` | — | — | — |
| `uuid` | `string` | — | `4` | `open` | — | — | — |
| `changes` | `string` | — | `3` | `open` | — | Keitimas | Pageidaujamas keitimas, kableliu atskirtas sąrašas. |
| `structure` | `file` | — | `3` | `open` | — | Struktūra | Pageidaujama duomenų struktūra ([duomenų struktūros aprašas](https://atviriduomenys.readthedocs.io/dsa/index.html)). |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `is_existing` | `false` | — | — | — | Poreikis naujam duomenų rinkiniui. |
| `is_existing` | `true` | — | — | — | Poreikis esamam duomenų rinkiniui. |
| `status` | `'CREATED'` | — | — | Sukurta | Poreikis sukurtas, tačiau spendimas dėl atvėrimo nepateiktas. |
| `status` | `'APPROVED'` | — | — | Patvirtinta | Poreikis patvirtintas, prašomi duomenys bus atverti. |
| `status` | `'ALREADY_OPENED'` | — | — | Atverta | Prašomi duomenys jau atverti. |
| `status` | `'REJECTED'` | — | — | Atmestas | Poreikis nebus tenkinmas, nes duomenų negalima atverti dėl nurodytų priežasčių. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L288 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L288)
