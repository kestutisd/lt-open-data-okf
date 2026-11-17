---
type: Table
title: "TermDomain"
description: "Taikymo sritis (standartizacija ir metrologija)"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/TermDomain"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L35"
    last_modified: "2026-11-11T14:39:20Z"
---

# TermDomain

Taikymo sritis (standartizacija ir metrologija)

- **Model:** `datasets/gov/lst/terms/TermDomain`[^manifest]
- **Dataset:** [datasets/gov/lst/terms](../terms.md) (`datasets/gov/lst/terms`)
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L35)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/TermDomain`
- **Primary Key (`ref`):** `term, domain`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `domain` | `ref` | [Domain](Domain.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv
