---
type: Table
title: "Prisirases — Prisirašiusių prie psichikos sveikatos centro asmenų skaičius"
description: "Informacija apie prisirašiusių prie psichikos sveikatos centrų asmenų skaičių (paskutinei mėnesio dienai)"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase_psc/Prisirases"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase_pcs.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_pcs.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prisirases — Prisirašiusių prie psichikos sveikatos centro asmenų skaičius

Informacija apie prisirašiusių prie psichikos sveikatos centrų asmenų skaičių (paskutinei mėnesio dienai)

- **Model:** `datasets/gov/vlk/prisirase_psc/Prisirases`[^manifest]
- **Dataset:** [datasets/gov/vlk/prisirase_psc](../prisirase_psc.md) (`datasets/gov/vlk/prisirase_psc`)
- **Manifest CSV:** [datasets/gov/vlk/prisirase_pcs.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_pcs.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase_psc/Prisirases`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `data` | `date` | `M` | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `istaiga` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga[kodas]](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, prie kurios prisirašę asmenys, ID |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `draustumas` | `integer` | — | `3` | `open` | — | Draustumas | Požymis, parodantis, ar asmenys buvo apdrausti PSD nurodytu laikotarpiu |
| `tlk` | `string` | — | `4` | `open` | — | Teritorinė ligonių kasa | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `asmenys` | `number` | `U` | `4` | `open` | — | Asmenų skaičius | Prisirašiusių prie pirminės psichikos centro asmenų skaičius (paskutinei mėnesio dienai) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | — | — |
| `lytis` | `"Vyras"` | — | — | — | — |
| `tlk` | `"Vilniaus TLK"` | — | — | — | — |
| `tlk` | `"Kauno TLK"` | — | — | — | — |
| `tlk` | `"Klaipėdos TLK"` | — | — | — | — |
| `tlk` | `"Šiaulių TLK"` | — | — | — | — |
| `tlk` | `"Panevėžio TLK"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase_pcs.csv
