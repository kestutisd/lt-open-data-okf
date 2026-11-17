---
type: Table
title: "Valgis — Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigų maitinimo ataskaitos"
description: "Pateikiami duomenys apie suteiktas maitinimo paslaugas švietimo įstaigoje pagal maitinimo kategoriją ataskaitine data."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/maitinimas/Valgis"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/maitinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/maitinimas.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valgis — Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigų maitinimo ataskaitos

Pateikiami duomenys apie suteiktas maitinimo paslaugas švietimo įstaigoje pagal maitinimo kategoriją ataskaitine data. Nurodoma ataskaitinė diena, ugdymo įstaiga, maitinimo tipas ir maitinimą gavusių asmenų skaičius.

- **Model:** `datasets/gov/vilniaus_m_sav/maitinimas/Valgis`[^manifest]
- **Dataset:** [Maitinimo duomenys Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose](../maitinimas.md) (`datasets/gov/vilniaus_m_sav/maitinimas`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/maitinimas.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/maitinimas.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/maitinimas/Valgis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `ataskaitine_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data, kuriai deklaruoti duomenys | — |
| `istaiga` | `string` | — | `4` | `open` | — | Ugdymo įstaigos pavadinimas | — |
| `maitinimo_kategorija` | `string` | — | `4` | `open` | — | Maitinimo kategorija | — |
| `viso_asmenu` | `integer` | `U` | `4` | `open` | — | Maitinimą gavusių asmenų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/maitinimas.csv
