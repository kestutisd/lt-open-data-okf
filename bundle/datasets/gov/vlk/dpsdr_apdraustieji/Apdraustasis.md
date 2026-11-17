---
type: Table
title: "Apdraustasis — Apdraustųjų skaičius"
description: "Spinta table datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apdraustasis — Apdraustųjų skaičius

- **Model:** `datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis`[^manifest]
- **Dataset:** [datasets/gov/vlk/dpsdr_apdraustieji](../dpsdr_apdraustieji.md) (`datasets/gov/vlk/dpsdr_apdraustieji`)
- **Manifest CSV:** [datasets/gov/vlk/dpsdr_apdraustieji.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `M` | `4` | `open` | — | Laikotarpis | Laikotarpis mėnesio tikslumu |
| `asm_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `pagrindas` | `ref` | [Pagrindas](Pagrindas.md) | `4` | `open` | — | Nuoroda į Pagrindas | Įregistravimo pagrindo unikalus numeris |
| `skaicius` | `number` | `U` | `4` | `open` | — | Apdraustųjų skaičius | Apdraustųjų skaičius (paskutinės mėnesio dienos duomenimis) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asm_lytis` | `"Vyras"` | — | — | — | — |
| `asm_lytis` | `"Moteris"` | — | — | — | — |
| `asm_lytis` | `"Nenurodyta"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv
