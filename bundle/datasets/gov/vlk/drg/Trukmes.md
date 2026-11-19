---
type: Table
title: "Trukmes — DRG trukmės"
description: "Giminingų diagnozių grupių gydymo trukmės"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg/Trukmes"
tags: [gov, vlk, trukmes, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L37"
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L37"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1384/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/drg"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Trukmes — DRG trukmės

Giminingų diagnozių grupių gydymo trukmės[^manifest]

- **Model:** `datasets/gov/vlk/drg/Trukmes`[^manifest]
- **Dataset:** [DRG sąrašas](../drg.md) (`datasets/gov/vlk/drg`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L37)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg/Trukmes` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupe` | `ref` | [Grupe](Grupe.md) (`level=4 UUID`: `grupe._id`) | `4` | `open` | — | Nuoroda į DRG grupes | — |
| `minimali` | `integer` | — | `4` | `open` | — | Minimali DRG trukmė | Minimali gydymo trukmė (lovadieniai) |
| `vidutine` | `integer` | — | `4` | `open` | — | Vidutinė DRG trukmė | Vidutinė gydymo trukmė (lovadieniai) |
| `maksimali` | `integer` | — | `4` | `open` | — | Maksimali DRG trukmė | Maksimali gydymo trukmė (lovadieniai) |
| `nuo` | `date` | `D` | `4` | `open` | — | DRG trukmė (nuo) | Normatyvinės gydymo trukmės galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | DRG trukmė (iki) | Normatyvinės gydymo trukmės galiojimo pabaigos data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L37 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L37)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/drg (https://data.gov.lt/datasets/1384/)
