---
type: Table
title: "ServiceDescription — Išoriniai ir vidiniai paslaugų aprašai"
description: "Paslaugų aprašai. Trumpi, ilgi pavadinimai."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp/ServiceDescription"
tags: [gov, ivpk, servicedescription, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ServiceDescription — Išoriniai ir vidiniai paslaugų aprašai

Paslaugų aprašai. Trumpi, ilgi pavadinimai. Mokama/nemokama paslauga ir pan. Informacija kuri matoma paslaugos apraše.[^manifest]

- **Model:** `datasets/gov/ivpk/viisp/ServiceDescription`[^manifest]
- **Dataset:** [datasets/gov/ivpk/viisp](../viisp.md) (`datasets/gov/ivpk/viisp`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp/ServiceDescription` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L4)
