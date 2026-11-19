---
type: Table
title: "BiudzetoVykdymoAtaskaita"
description: "Spinta table datasets/gov/pb/bva/BiudzetoVykdymoAtaskaita (7 columns)."
tags: [gov, pb, biudzetovykdymoataskaita, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/bva.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/pb/bva.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# BiudzetoVykdymoAtaskaita

- **Model:** `datasets/gov/pb/bva/BiudzetoVykdymoAtaskaita`[^manifest]
- **Dataset:** [datasets/gov/pb/bva](../bva.md) (`datasets/gov/pb/bva`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/bva.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/bva.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `planas_metams` | `integer` | — | `2` | `open` | — | Asignavimų planas metams | — |
| `planas_ataskaitiniam_laikotarpiui` | `integer` | — | `2` | `open` | — | Asignavimų planas ataskaitiniam laikotarpiui | — |
| `gauti_asignavimai` | `number` | — | `2` | `open` | — | Gauti asignavimai | — |
| `panaudoti_asignavimai` | `number` | — | `2` | `open` | — | Panaudoti asignavimai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `planas_metams` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `planas_ataskaitiniam_laikotarpiui` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `gauti_asignavimai` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `panaudoti_asignavimai` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/bva.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/bva.csv#L5)
