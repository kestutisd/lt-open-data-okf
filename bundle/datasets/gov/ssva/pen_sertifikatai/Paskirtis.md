---
type: Table
title: "Paskirtis — Pastatų paskirtys"
description: "Pagal STR 2.01.09:2005 ir STR 2.01.02:2016"
resource: "https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai/Paskirtis"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paskirtis — Pastatų paskirtys

Pagal STR 2.01.09:2005 ir STR 2.01.02:2016

- **Model:** `datasets/gov/ssva/pen_sertifikatai/Paskirtis`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikatus](../pen_sertifikatai.md) (`datasets/gov/ssva/pen_sertifikatai`)
- **Manifest CSV:** [datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai/Paskirtis`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Pastatų paskirties ID | — |
| `paskirtis` | `string` | — | `4` | `open` | — | Pastatų paskirties sutrumpinimas | — |
| `grupe` | `string` | — | `4` | `open` | — | Pastatų grupė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paskirtis` | `"GV"` | — | — | Gyvenamosios paskirties vieno ir dviejų butų pastatai (namai) | — |
| `paskirtis` | `"KG"` | — | — | Kiti gyvenamieji pastatai (namai) | — |
| `paskirtis` | `"AD"` | — | — | Administracinės paskirties pastatai | — |
| `paskirtis` | `"MK"` | — | — | Mokslo paskirties pastatai | — |
| `paskirtis` | `"GD"` | — | — | Gydymo paskirties pastatai | — |
| `paskirtis` | `"MT"` | — | — | Maitinimo paskirties pastatai | — |
| `paskirtis` | `"PR"` | — | — | Prekybos paskirties pastatai | — |
| `paskirtis` | `"SP"` | — | — | Sporto paskirties pastatai, išskyrus baseinus | — |
| `paskirtis` | `"BS"` | — | — | Baseinai | — |
| `paskirtis` | `"KT"` | — | — | Kultūros paskirties pastatai | — |
| `paskirtis` | `"GM"` | — | — | Garažų, gamybos ir pramonės paskirties pastatai | — |
| `paskirtis` | `"SN"` | — | — | Sandėliavimo paskirties pastatai | — |
| `paskirtis` | `"VB"` | — | — | Viešbučių paskirties pastatai | — |
| `paskirtis` | `"PS"` | — | — | Paslaugų paskirties pastatai | — |
| `paskirtis` | `"TR"` | — | — | Transporto paskirties pastatai | — |
| `paskirtis` | `"PL"` | — | — | Poilsio paskirties pastatai | — |
| `paskirtis` | `"SC"` | — | — | Specialiosios paskirties pastatai | — |
| `grupe` | `"VIES"` | — | — | Viešoji | — |
| `grupe` | `"PRAM"` | — | — | Pramoninė | — |
| `grupe` | `"GYV"` | — | — | Gyvenamoji | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv
