---
type: Table
title: "LRLawStatement"
description: "Nacionalinių teisės aktų, kuriais į nacionalinę teisę perkelta Europos Sąjungos direktyva arba standartas turi nuokrypą arba standartas turi išskirtinę nuorodą, duomenys (pavadinimas, numeris, priėmimo data, įsigaliojimo data..."
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/LRLawStatement"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L165"
    last_modified: "2026-11-11T14:39:20Z"
---

# LRLawStatement

Nacionalinių teisės aktų, kuriais į nacionalinę teisę perkelta Europos Sąjungos direktyva arba standartas turi nuokrypą arba standartas turi išskirtinę nuorodą, duomenys (pavadinimas, numeris, priėmimo data, įsigaliojimo data, panaikinimo data, Valstybės žinių numeris, Valstybės žinių data)

- **Model:** `datasets/gov/lst/standards/LRLawStatement`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L165](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L165)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/LRLawStatement`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | — | — | `open` | — | — | — |
| `type` | `ref` | [LRLawStatementType](LRLawStatementType.md) | — | `open` | — | — | — |
| `number` | `string` | — | — | `open` | — | — | — |
| `valid_from` | `datetime` | — | — | `open` | — | — | — |
| `link` | `string` | — | — | `open` | — | — | — |
| `state_news_nr` | `string` | — | — | `open` | — | — | — |
| `state_news_date` | `datetime` | — | — | `open` | — | — | — |
| `remarks` | `string` | — | — | `open` | — | — | — |
| `implementation_date` | `datetime` | — | — | `open` | — | — | — |
| `withdrawal_date` | `datetime` | — | — | `open` | — | — | — |
| `register_nr` | `string` | — | — | `open` | — | — | — |
| `register_date` | `datetime` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
