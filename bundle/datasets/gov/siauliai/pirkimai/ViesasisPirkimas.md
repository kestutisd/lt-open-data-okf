---
type: Table
title: "ViesasisPirkimas — Viešieji pirkimai"
description: "Spinta table datasets/gov/siauliai/pirkimai/ViesasisPirkimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/siauliai/pirkimai/ViesasisPirkimas"
tags: [gov, siauliai, viesasispirkimas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliai/pirkimai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/siauliai/pirkimai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ViesasisPirkimas — Viešieji pirkimai

- **Model:** `datasets/gov/siauliai/pirkimai/ViesasisPirkimas`[^manifest]
- **Dataset:** [datasets/gov/siauliai/pirkimai](../pirkimai.md) (`datasets/gov/siauliai/pirkimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliai/pirkimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliai/pirkimai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliai/pirkimai/ViesasisPirkimas` (`deployed`)[^manifest]
- **Provider:** `siauliai` — Šiaulių miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | ID | — |
| `ketvirtis` | `string` | — | `2` | `open` | — | Ketvirtis | — |
| `kontrakto_rusis` | `string` | — | `3` | `open` | — | Kontrakto rūšis | — |
| `metai` | `string` | — | `2` | `open` | — | Metai | — |
| `pirkimo_pavadinimas` | `string` | — | `4` | `open` | — | Pirkimo pavadinimas | — |
| `sutart_sask_nr` | `string` | — | `4` | `open` | — | Sutarties sąskaitos numeris | — |
| `sutarties_data` | `date` | `D` | `4` | `open` | — | Sutarties data | — |
| `sutarties_verte` | `number` | — | `4` | `open` | — | Sutarties vertė | — |
| `sutarties_verte_bepvm` | `number` | — | `4` | `open` | — | Sutarties vertė be pvm | — |
| `tiekejo_pavadinimas` | `string` | — | `2` | `open` | — | Tiekėjo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliai/pirkimai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliai/pirkimai.csv#L4)
