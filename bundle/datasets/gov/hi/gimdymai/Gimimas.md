---
type: Table
title: "Gimimas — Duomenys apie gimdymus Lietuvoje."
description: "Spinta table datasets/gov/hi/gimdymai/Gimimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/gimdymai/Gimimas"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/gimdymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gimimas — Duomenys apie gimdymus Lietuvoje.

- **Model:** `datasets/gov/hi/gimdymai/Gimimas`[^manifest]
- **Dataset:** [Duomenys apie gimdymus Lietuvoje.](../gimdymai.md) (`datasets/gov/hi/gimdymai`)
- **Manifest CSV:** [datasets/gov/hi/gimdymai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gimdymai/Gimimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `gimdymo_data` | `datetime` | `L` | `4` | `open` | — | Gimdymo laiko žyma | — |
| `rajonas` | `string` | — | `4` | `open` | — | Nėščiosios (Motinos) gyvenamosios vietos rajonas | — |
| `gimdymo_vieta` | `string` | — | `4` | `open` | — | Gimdymo vieta | — |
| `viso_vaisiu` | `integer` | `U` | `4` | `open` | — | Vaisių skaičius gimdyme iš viso | — |
| `mot_rhd` | `string` | — | `4` | `open` | — | Nėščiosios (motinos) RhD antigenas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gimdymo_vieta` | `"Stacionare"` | — | — | — | — |
| `gimdymo_vieta` | `"Namuose"` | — | — | — | — |
| `gimdymo_vieta` | `"GMP"` | — | — | — | — |
| `gimdymo_vieta` | `"Kitur"` | — | — | — | — |
| `mot_rhd` | `"+"` | — | — | — | Teigiamas |
| `mot_rhd` | `"-"` | — | — | — | Neigiamas |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gimdymai.csv
