---
type: Table
title: "Term"
description: "Termino straipsnis (tinkamumo kategorija, sukirčiuotas terminas, apibrėžtis, pastabos, simbolis, straipsnio nr. standarte, pagrindinis žodis)"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/Term"
tags: [gov, lst, term, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L45"
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv#L45"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/terms"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Term

Termino straipsnis (tinkamumo kategorija, sukirčiuotas terminas, apibrėžtis, pastabos, simbolis, straipsnio nr. standarte, pagrindinis žodis)[^manifest]

- **Model:** `datasets/gov/lst/terms/Term`[^manifest]
- **Dataset:** [Standartų terminų bazė](../terms.md) (`datasets/gov/lst/terms`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L45)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/Term` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv#L45 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L45)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/terms (https://data.gov.lt/datasets/996/)
