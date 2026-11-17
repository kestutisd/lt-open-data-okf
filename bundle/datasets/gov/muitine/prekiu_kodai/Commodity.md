---
type: Table
title: "Commodity"
description: "Spinta table datasets/gov/muitine/prekiu_kodai/Commodity (11 columns)."
tags: [gov, muitine, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/prekiu_kodai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekiu_kodai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Commodity

- **Model:** `datasets/gov/muitine/prekiu_kodai/Commodity`[^manifest]
- **Dataset:** [datasets/gov/muitine/prekiu_kodai](../prekiu_kodai.md) (`datasets/gov/muitine/prekiu_kodai`)
- **Manifest CSV:** [datasets/gov/muitine/prekiu_kodai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekiu_kodai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `code`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `4` | `open` | — | Prekės kodas | 10 simbolių kodas |
| `indents` | `number` | — | `3` | `open` | — | Įtrauka | — |
| `commodity` | `ref` | [Commodity](Commodity.md) | `1` | `open` | — | Platesnė prekių grupė | — |
| `suffix` | `string` | — | `4` | `open` | — | Sufiksas | 2 simbolių kodas |
| `import` | `boolean` | — | `4` | `open` | — | Taikymo importo procedūroms požymis | — |
| `export` | `boolean` | — | `4` | `open` | — | Taikymo eksporto procedūroms požymis | — |
| `excise` | `boolean` | — | `4` | `open` | — | Akcizinės prekės požymis | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžia | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaiga | — |
| `description_lt` | `string` | — | `2` | `open` | — | Aprašymas (LT) | — |
| `description_en` | `string` | — | `2` | `open` | — | Aprašymas (EN) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `description_lt` | `update(property: "description@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `description_en` | `update(property: "description@en", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/prekiu_kodai.csv
