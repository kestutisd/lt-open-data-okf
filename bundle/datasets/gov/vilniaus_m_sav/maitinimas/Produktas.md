---
type: Table
title: "Produktas — Sunaudoti maisto produktai Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose"
description: "Skelbiama informacija apie maisto gamybai sunaudotus maisto produktus."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/maitinimas/Produktas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/maitinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/maitinimas.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Produktas — Sunaudoti maisto produktai Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose

Skelbiama informacija apie maisto gamybai sunaudotus maisto produktus. Šiuos duomenis įstaigos skelbia nereguliariu dažniu, todėl viena eilutė identifikuoja situaciją apie sunaudotus maisto produktus nuo paskutinės pateiktos ataskaitos. Nurodoma ataskaitą teikusi švietimo įstaiga, deklaruotas produktas ir sunaudotas kiekis maisto gamyboje.

- **Model:** `datasets/gov/vilniaus_m_sav/maitinimas/Produktas`[^manifest]
- **Dataset:** [Maitinimo duomenys Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose](../maitinimas.md) (`datasets/gov/vilniaus_m_sav/maitinimas`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/maitinimas.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/maitinimas.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/maitinimas/Produktas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `ataskaitine_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data, kuriai deklaruoti duomenys | — |
| `istaiga` | `string` | — | `4` | `open` | — | Ugdymo įstaigos pavadinimas | — |
| `produktas` | `string` | — | `4` | `open` | — | Deklaruoto produkto pavadinimas | — |
| `kiekis` | `number` | — | `4` | `open` | — | Sunaudoto produkto kiekis | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Produkto kiekio matavimo vienetai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `matavimo_vnt` | `"kg"` | — | — | Kilogramai | — |
| `matavimo_vnt` | `"vnt"` | — | — | Vienetai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/maitinimas.csv
