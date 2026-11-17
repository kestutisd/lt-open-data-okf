---
type: Table
title: "Trukmes — DRG trukmės"
description: "Giminingų diagnozių grupių gydymo trukmės"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg/Trukmes"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L37"
    last_modified: "2026-11-11T14:39:20Z"
---

# Trukmes — DRG trukmės

Giminingų diagnozių grupių gydymo trukmės

- **Model:** `datasets/gov/vlk/drg/Trukmes`[^manifest]
- **Dataset:** [datasets/gov/vlk/drg](../drg.md) (`datasets/gov/vlk/drg`)
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L37)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg/Trukmes`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupe` | `ref` | [Grupe](Grupe.md) | `4` | `open` | — | Nuoroda į DRG grupes | — |
| `minimali` | `integer` | — | `4` | `open` | — | Minimali DRG trukmė | Minimali gydymo trukmė (lovadieniai) |
| `vidutine` | `integer` | — | `4` | `open` | — | Vidutinė DRG trukmė | Vidutinė gydymo trukmė (lovadieniai) |
| `maksimali` | `integer` | — | `4` | `open` | — | Maksimali DRG trukmė | Maksimali gydymo trukmė (lovadieniai) |
| `nuo` | `date` | `D` | `4` | `open` | — | DRG trukmė (nuo) | Normatyvinės gydymo trukmės galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | DRG trukmė (iki) | Normatyvinės gydymo trukmės galiojimo pabaigos data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv
