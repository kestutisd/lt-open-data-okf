---
type: Table
title: "ServiceDescription — Išoriniai ir vidiniai paslaugų aprašai"
description: "Paslaugų aprašai."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp/ServiceDescription"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ServiceDescription — Išoriniai ir vidiniai paslaugų aprašai

Paslaugų aprašai. Trumpi, ilgi pavadinimai. Mokama/nemokama paslauga ir pan. Informacija kuri matoma paslaugos apraše.

- **Model:** `datasets/gov/ivpk/viisp/ServiceDescription`[^manifest]
- **Dataset:** [datasets/gov/ivpk/viisp](../viisp.md) (`datasets/gov/ivpk/viisp`)
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp/ServiceDescription`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus paslaugos aprašo ID | — |
| `unique_id` | `string` | — | `4` | `open` | — | Unikalus paslaugos ID. (PID) | — |
| `description_lt` | `string` | — | `4` | `open` | — | Paslaugos aprašas | — |
| `name_lt` | `string` | — | `4` | `open` | — | Paslaugos pavadinimas | — |
| `short_description_lt` | `string` | — | `4` | `open` | — | Trumpas paslaugos aprašas | — |
| `short_name` | `string` | — | `4` | `open` | — | Trumpas pavadinimas | — |
| `is_paid_service` | `boolean` | — | `4` | `open` | — | Ar mokama paslauga | — |
| `contacts_lt` | `string` | — | `4` | `open` | — | Kontaktai | — |
| `price_lt` | `string` | — | `4` | `open` | — | Paslaugos apraše nurodyta kaina | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv
