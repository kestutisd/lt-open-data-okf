---
type: Table
title: "KrutiesVezioZymenys — Asmenys, kuriems atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m."
description: "Spinta table datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# KrutiesVezioZymenys — Asmenys, kuriems atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m.

- **Model:** `datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys`[^manifest]
- **Dataset:** [Asmenys, kuriems atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m.](../kruties_vezio_zymenys.md) (`datasets/gov/lsd/sveikata/kruties_vezio_zymenys`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `tyrimo_atlikimo_metai` | `integer` | — | `3` | `open` | — | Krūties vėžio prognostinių žymenų tyrimo atlikimo metai | — |
| `rizika` | `string` | — | `4` | `open` | — | Krūties vėžio atsinaujinimo rizika | — |
| `kruties_vezio_potipis` | `string` | — | `4` | `open` | — | Krūties vėžio potipis | — |
| `genetiko_konsultacija` | `boolean` | — | `4` | `open` | — | Genetiko konsultacijos paslaugos (kodai: 1557,1627,1749,3397,3398,3399,4496,4497,4682) suteikimo faktas prieš atliktą krūties vėžio prognostinių žymenų tyrimą | — |
| `dalyvavimas_kvpp` | `boolean` | — | `4` | `open` | — | Dalyvavimo KVPP (krūties vėžio prevencinėje programoje) faktas prieš atliktą krūties vėžio prognostinių žymenų tyrimą | — |
| `gydymas_l01` | `boolean` | — | `4` | `open` | — | Gydymo faktas L01 ATC subgrupės vaistais po atlikto krūties vėžio prognostinių žymenų tyrimo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rizika` | `"Maža"` | — | — | — | — |
| `rizika` | `"Vidutinė"` | — | — | — | — |
| `rizika` | `"Didelė"` | — | — | — | — |
| `kruties_vezio_potipis` | `"Luminalinis A"` | — | — | — | — |
| `kruties_vezio_potipis` | `"Luminalinis B"` | — | — | — | — |
| `kruties_vezio_potipis` | `"HER2 praturtintas"` | — | — | — | — |
| `kruties_vezio_potipis` | `"Bazalinis"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv
