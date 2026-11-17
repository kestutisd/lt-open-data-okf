---
type: Table
title: "Jungimas — Vilniaus miesto savivaldybės teisės aktų tarpusavio sąryšiai"
description: "Spinta table datasets/gov/vilniaus_m_sav/aktai/Jungimas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Jungimas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Jungimas — Vilniaus miesto savivaldybės teisės aktų tarpusavio sąryšiai

- **Model:** `datasets/gov/vilniaus_m_sav/aktai/Jungimas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės teisės aktų registras](../aktai.md) (`datasets/gov/vilniaus_m_sav/aktai`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/aktai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Jungimas`
- **Primary Key (`ref`):** `rysio_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rysio_id` | `string` | — | `4` | `open` | — | Ryšio identifikacinis numeris | — |
| `rysio_pradzia` | `string` | — | `4` | `open` | — | Ryšio pradžios dokumento identifikacinis numeris. | Referuoja į modelio Dokumentas pirminį raktą (dokumento_id) |
| `rysio_pabaiga` | `string` | — | `4` | `open` | — | Ryšio pabaigos dokumento identifikacinis numeris | Referuoja į modelio Dokumentas pirminį raktą (dokumento_id) |
| `rysys` | `string` | — | `4` | `open` | — | Ryšio tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv
