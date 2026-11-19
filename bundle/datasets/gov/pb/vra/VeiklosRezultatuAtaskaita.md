---
type: Table
title: "VeiklosRezultatuAtaskaita"
description: "Spinta table datasets/gov/pb/vra/VeiklosRezultatuAtaskaita (4 columns)."
tags: [gov, pb, veiklosrezultatuataskaita, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/vra.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/pb/vra.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeiklosRezultatuAtaskaita

- **Model:** `datasets/gov/pb/vra/VeiklosRezultatuAtaskaita`[^manifest]
- **Dataset:** [datasets/gov/pb/vra](../vra.md) (`datasets/gov/pb/vra`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/vra.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/vra.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `straipsniai` | `string` | — | `3` | `open` | — | Straipsniai | — |
| `dabartinis_ataskaitinis_laikotarpis` | `number` | — | `2` | `open` | — | Dabartinis ataskaitinis laikotarpis(pajamos) | — |
| `praejes_ataskaitinis_laikotarpis` | `number` | — | `2` | `open` | — | Praėjęs ataskaitinis laikotarpis(pajamos) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dabartinis_ataskaitinis_laikotarpis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `praejes_ataskaitinis_laikotarpis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/vra.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/vra.csv#L5)
