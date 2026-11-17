---
type: Table
title: "Text"
description: "Su standartu susijusi tekstinė informacija (standarto pavadinimas (antraštė), aprašymas (abstract), taikymo sritis (scope) lietuvių ir anglų kalbomis, pastaba, kuri pateikia papildomą informaciją susijusią standartu)"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Text"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L327"
    last_modified: "2026-11-11T14:39:20Z"
---

# Text

Su standartu susijusi tekstinė informacija (standarto pavadinimas (antraštė), aprašymas (abstract), taikymo sritis (scope) lietuvių ir anglų kalbomis, pastaba, kuri pateikia papildomą informaciją susijusią standartu)

- **Model:** `datasets/gov/lst/standards/Text`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L327](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L327)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Text`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `type` | `ref` | [TextType](TextType.md) | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `text` | `string` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
