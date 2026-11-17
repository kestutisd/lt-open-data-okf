---
type: Table
title: "TycinisBankrotas — Duomenys apie tyčinius bankrotus"
description: "Spinta table datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas"
tags: [gov, avnt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/avnt/tyciniai_bankrotai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TycinisBankrotas — Duomenys apie tyčinius bankrotus

- **Model:** `datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas`[^manifest]
- **Dataset:** [Duomenys apie tyčinius bankrotus](../tyciniai_bankrotai.md) (`datasets/gov/avnt/tyciniai_bankrotai`)
- **Manifest CSV:** [datasets/gov/avnt/tyciniai_bankrotai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `imones_kodas` | `string` | — | `2` | `open` | — | Įmonės kodas | — |
| `imones_pavadinimas` | `string` | — | `2` | `open` | — | Įmonės pavadinimas | — |
| `bankroto_pradzia` | `date` | `D` | `4` | `open` | — | Bankroto proceso pradžios data | — |
| `apygardos_teismas` | `string` | — | `2` | `open` | — | Apygardos teismo pavadinimas | — |
| `likvidavimo_data` | `date` | `D` | `4` | `open` | — | Likvidavimo data | — |
| `tycinis_bankrotas` | `date` | `D` | `4` | `open` | — | Pripažinti bankrotą tyčiniu data | Data, kuomet teismo sprendimu bankrotas pripažintas tyčiniu |
| `sprendimas_del_pabaigos` | `date` | `D` | `4` | `open` | — | Sprendimo dėl įmonės veiklos pabaigos data | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Įmonės išregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/tyciniai_bankrotai.csv
