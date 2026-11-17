---
type: Table
title: "EltsaNoiseLevel — Triukšmas pagrindiniuose geležinkelio keliuose ne aglomeracijos zonose"
description: "Spinta table datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_triuksmas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# EltsaNoiseLevel — Triukšmas pagrindiniuose geležinkelio keliuose ne aglomeracijos zonose

- **Model:** `datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel`[^manifest]
- **Dataset:** [Triukšmas pagrindiniuose geležinkelio keliuose ne aglomeracijos zonose](../gelezinkeliu_triuksmas.md) (`datasets/gov/ltsa/gelezinkeliu_triuksmas`)
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel`
- **Primary Key (`ref`):** `gid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ctryid` | `string` | — | `4` | `open` | — | Valstybės kodas | — |
| `db_high` | `integer` | `dB` | `4` | `open` | — | Triukšmo viršutinė reikšmė | — |
| `db_low` | `integer` | `dB` | `4` | `open` | — | Triukšmo žemutinė reikšmė | — |
| `geom` | `geometry(multipolygonzm, 3346)` | — | `3` | `open` | — | Teritorija | — |
| `gid` | `integer` | — | `4` | `open` | — | ID | — |
| `group` | `string` | — | `3` | `open` | — | Grupė | — |
| `period` | `string` | — | `3` | `open` | — | Paros laikas | — |
| `year` | `integer` | — | `2` | `open` | — | Metai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_triuksmas.csv
