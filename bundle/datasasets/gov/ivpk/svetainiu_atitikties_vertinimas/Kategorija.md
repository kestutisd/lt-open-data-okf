---
type: Table
title: "Kategorija"
description: "Spinta table datasasets/gov/ivpk/svetainiu_atitikties_vertinimas/Kategorija (2 columns)."
tags: [datasasets, ivpk, kategorija, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kategorija

- **Model:** `datasasets/gov/ivpk/svetainiu_atitikties_vertinimas/Kategorija` *(`[sic]` upstream manifest namespace)*[^manifest]
- **Dataset:** [datasasets/gov/ivpk/svetainiu_atitikties_vertinimas](../svetainiu_atitikties_vertinimas.md) (`datasasets/gov/ivpk/svetainiu_atitikties_vertinimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `1` | `open` | — | Kategorijos pavadinimas | — |
| `kategorija` | `ref` | [Kategorija](Kategorija.md) (`level=1` scalar) | `1` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv#L17)
