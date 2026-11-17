---
type: Table
title: "RelatedTerm"
description: "Su terminu susieti kiti terminai ir (arba) sinonimai"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/RelatedTerm"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# RelatedTerm

Su terminu susieti kiti terminai ir (arba) sinonimai

- **Model:** `datasets/gov/lst/terms/RelatedTerm`[^manifest]
- **Dataset:** [datasets/gov/lst/terms](../terms.md) (`datasets/gov/lst/terms`)
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/RelatedTerm`
- **Primary Key (`ref`):** `term, related_term`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `related_term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `type` | `ref` | [RelationType](RelationType.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv
