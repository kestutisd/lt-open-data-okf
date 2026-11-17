---
type: Table
title: "Kriterijus"
description: "Spinta table datasasets/gov/ivpk/svetainiu_atitikties_vertinimas/Kriterijus (3 columns)."
tags: [gov, ivpk, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kriterijus

- **Model:** `datasasets/gov/ivpk/svetainiu_atitikties_vertinimas/Kriterijus`[^manifest]
- **Dataset:** [datasasets/gov/ivpk/svetainiu_atitikties_vertinimas](../svetainiu_atitikties_vertinimas.md) (`datasasets/gov/ivpk/svetainiu_atitikties_vertinimas`)
- **Manifest CSV:** [datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `1` | `open` | — | Kriterijaus pavadinimas | — |
| `kategorija` | `ref` | [Kategorija](Kategorija.md) | `1` | `open` | — | Kategorija kuriai priklauso kriterijus | — |
| `atitinka` | `boolean` | — | `1` | `open` | — | Atitikmuo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `atitinka` | `false` | `0` | — | Neatitinka | — |
| `atitinka` | `true` | `1` | — | Atitinka | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv
