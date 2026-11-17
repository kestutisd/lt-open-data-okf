---
type: Table
title: "StandardDirective"
description: "Standarto ryšys su Europos Sąjungos direktyvomis"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/StandardDirective"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L302"
    last_modified: "2026-11-11T14:39:20Z"
---

# StandardDirective

Standarto ryšys su Europos Sąjungos direktyvomis

- **Model:** `datasets/gov/lst/standards/StandardDirective`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L302](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L302)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/StandardDirective`
- **Primary Key (`ref`):** `directive, standard`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `directive` | `ref` | [Directive](Directive.md) | — | `open` | — | — | — |
| `standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `oficial_journal` | `string` | — | — | `open` | — | — | — |
| `lithuanian_oficial_journal` | `string` | — | — | `open` | — | — | — |
| `lithuanian_oficial_journal_date` | `datetime` | — | — | `open` | — | — | — |
| `harmonised` | `boolean` | — | — | `open` | — | — | — |
| `report_generation_date` | `datetime` | — | — | `open` | — | — | — |
| `applicability_date` | `datetime` | — | — | `open` | — | — | — |
| `oj_publication_date` | `datetime` | — | — | `open` | — | — | — |
| `coexistence_end_date` | `datetime` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
