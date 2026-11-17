---
type: Table
title: "LovosProfilis — Lovų profiliai"
description: "Spinta table datasets/gov/hi/lovos/LovosProfilis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/lovos/LovosProfilis"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/lovos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# LovosProfilis — Lovų profiliai

- **Model:** `datasets/gov/hi/lovos/LovosProfilis`[^manifest]
- **Dataset:** [Stacionaro lovų skaičius ir jų veiklos rodikliai](../lovos.md) (`datasets/gov/hi/lovos`)
- **Manifest CSV:** [datasets/gov/hi/lovos.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/lovos/LovosProfilis`
- **Primary Key (`ref`):** `prof_kod`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prof_kod` | `string` | — | `4` | `open` | — | Lovos profillo kodas | — |
| `grupes_kodas` | `string` | — | `4` | `open` | — | Lovos profilio grupės kodas | — |
| `prof_pavadinimas` | `string` | — | `4` | `open` | — | Lovos profilio pavadinimas | — |
| `grupes_pavadinimas` | `string` | — | `4` | `open` | — | Lovos profilio grupės pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/lovos.csv
