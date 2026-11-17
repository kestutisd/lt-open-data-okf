---
type: Table
title: "Sumos — Sumokėtos sumos už medicinos priemonių (prietaisų) nuomą"
description: "Spinta table datasets/gov/vlk/nmp_sumos/Sumos (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/nmp_sumos/Sumos"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/nmp_sumos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/nmp_sumos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sumos — Sumokėtos sumos už medicinos priemonių (prietaisų) nuomą

- **Model:** `datasets/gov/vlk/nmp_sumos/Sumos`[^manifest]
- **Dataset:** [datasets/gov/vlk/nmp_sumos](../nmp_sumos.md) (`datasets/gov/vlk/nmp_sumos`)
- **Manifest CSV:** [datasets/gov/vlk/nmp_sumos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/nmp_sumos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/nmp_sumos/Sumos`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `straipsnis` | `string` | — | `3` | `open` | — | PSDF biudžeto straipsnis | — |
| `kreditorius` | `string` | — | `3` | `open` | — | Įstaigos pavadinimas | — |
| `data_ad` | `date` | — | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `suma` | `number` | — | `2` | `open` | — | Suma eurais | Kompensuojama suma eurais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/nmp_sumos.csv
