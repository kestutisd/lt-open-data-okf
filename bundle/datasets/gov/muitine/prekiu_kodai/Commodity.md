---
type: Table
title: "Commodity"
description: "Spinta table datasets/gov/muitine/prekiu_kodai/Commodity (11 columns)."
tags: [gov, muitine, commodity, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekiu_kodai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/prekiu_kodai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Commodity

- **Model:** `datasets/gov/muitine/prekiu_kodai/Commodity`[^manifest]
- **Dataset:** [datasets/gov/muitine/prekiu_kodai](../prekiu_kodai.md) (`datasets/gov/muitine/prekiu_kodai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/prekiu_kodai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekiu_kodai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `code`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `4` | `open` | — | Prekės kodas | 10 simbolių kodas |
| `indents` | `number` | — | `3` | `open` | — | Įtrauka | — |
| `commodity` | `ref` | [Commodity](Commodity.md) (`level=1` scalar) | `1` | `open` | — | Platesnė prekių grupė | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/prekiu_kodai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekiu_kodai.csv#L6)
