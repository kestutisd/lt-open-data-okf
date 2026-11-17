---
type: Table
title: "Operacija — Centralizuotai perkamų endoprotezų panaudojimas"
description: "Informacija apie PSDF biudžeto lėšomis atliktų centralizuotai perkamų sąnarių endoprotezavimo operacijų skaičių"
resource: "https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Operacija"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Operacija — Centralizuotai perkamų endoprotezų panaudojimas

Informacija apie PSDF biudžeto lėšomis atliktų centralizuotai perkamų sąnarių endoprotezavimo operacijų skaičių

- **Model:** `datasets/gov/vlk/cp_endoprotezai/Operacija`[^manifest]
- **Dataset:** [datasets/gov/vlk/cp_endoprotezai](../cp_endoprotezai.md) (`datasets/gov/vlk/cp_endoprotezai`)
- **Manifest CSV:** [datasets/gov/vlk/cp_endoprotezai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Operacija`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istg_id` | `ref` | [Istaiga](Istaiga.md) | `4` | `open` | — | Nuoroda į Istaiga | Gydymo įstaigos unikalus numeris |
| `lokalizacijos_id` | `ref` | [Lokalizacija](Lokalizacija.md) | `4` | `open` | — | Nuoroda į Lokalizacija | Endoprotezo lokalizacijos unikalus numeris |
| `prasymo_id` | `ref` | [Prasymas](Prasymas.md) | `4` | `open` | — | Nuoroda į Prasymas | Prašymo unikalus numeris |
| `data` | `date` | `M` | `4` | `open` | — | Operacijos data | Operacijos atlikimo data mėnesio tikslumu |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv
