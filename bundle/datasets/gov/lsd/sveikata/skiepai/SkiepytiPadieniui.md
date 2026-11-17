---
type: Table
title: "SkiepytiPadieniui — Pasiskiepiję asmenys pagal dieną ir ligą"
description: "Spinta table datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# SkiepytiPadieniui — Pasiskiepiję asmenys pagal dieną ir ligą

- **Model:** `datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui`[^manifest]
- **Dataset:** [Asmenys, paskiepyti įvairių ligų skiepais](../skiepai.md) (`datasets/gov/lsd/sveikata/skiepai`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiPadieniui`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `date` | `date` | `D` | `4` | `open` | — | Diena, kurią skiepyta | — |
| `liga` | `string` | — | `2` | `open` | — | Liga, nuo kurios skiepijama | — |
| `n_asm` | `integer` | — | `4` | `open` | — | Skaičius asmenų, paskiepytų nuo tos ligos tą dieną | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv
