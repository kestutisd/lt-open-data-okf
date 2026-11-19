---
type: Table
title: "Paskirtis — Pastatų paskirtys"
description: "Pagal STR 2.01.09:2005 ir STR 2.01.02:2016"
resource: "https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai/Paskirtis"
tags: [gov, ssva, paskirtis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40"
    title: "atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2366/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pen_sertifikatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paskirtis — Pastatų paskirtys

Pagal STR 2.01.09:2005 ir STR 2.01.02:2016[^manifest]

- **Model:** `datasets/gov/ssva/pen_sertifikatai/Paskirtis`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikatus](../pen_sertifikatai.md) (`datasets/gov/ssva/pen_sertifikatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai/Paskirtis` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Pastatų paskirties ID | — |
| `paskirtis` | `string` | — | `4` | `open` | — | Pastatų paskirties sutrumpinimas | — |
| `grupe` | `string` | — | `4` | `open` | — | Pastatų grupė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L40)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pen_sertifikatai (https://data.gov.lt/datasets/2366/)
