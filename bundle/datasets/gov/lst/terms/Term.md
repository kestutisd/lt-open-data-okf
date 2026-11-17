---
type: Table
title: "Term"
description: "Termino straipsnis (tinkamumo kategorija, sukirčiuotas terminas, apibrėžtis, pastabos, simbolis, straipsnio nr. standarte, pagrindinis žodis)"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/Term"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L45"
    last_modified: "2026-11-11T14:39:20Z"
---

# Term

Termino straipsnis (tinkamumo kategorija, sukirčiuotas terminas, apibrėžtis, pastabos, simbolis, straipsnio nr. standarte, pagrindinis žodis)

- **Model:** `datasets/gov/lst/terms/Term`[^manifest]
- **Dataset:** [datasets/gov/lst/terms](../terms.md) (`datasets/gov/lst/terms`)
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L45)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/Term`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `created` | `datetime` | — | — | `open` | — | — | — |
| `updated` | `datetime` | — | — | `open` | — | — | — |
| `status` | `ref` | [Status](Status.md) | — | `open` | — | — | — |
| `term_acc` | `string` | — | — | `open` | — | — | — |
| `abbreviation` | `string` | — | — | `open` | — | — | — |
| `article_no` | `string` | — | — | `open` | — | — | — |
| `symbol` | `string` | — | — | `open` | — | — | — |
| `text` | `string` | — | — | `open` | — | — | — |
| `note` | `string` | — | — | `open` | — | — | — |
| `keyword` | `string` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv
