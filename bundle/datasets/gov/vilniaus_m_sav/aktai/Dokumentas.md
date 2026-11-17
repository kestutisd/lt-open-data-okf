---
type: Table
title: "Dokumentas — Vilniaus miesto savivaldybės teisės aktai"
description: "Spinta table datasets/gov/vilniaus_m_sav/aktai/Dokumentas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Dokumentas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — Vilniaus miesto savivaldybės teisės aktai

- **Model:** `datasets/gov/vilniaus_m_sav/aktai/Dokumentas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės teisės aktų registras](../aktai.md) (`datasets/gov/vilniaus_m_sav/aktai`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/aktai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Dokumentas`
- **Primary Key (`ref`):** `dokumento_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento identifikacinis numeris | — |
| `paskelbimas` | `date` | `D` | `4` | `open` | — | Dokumento pasirašymo data | — |
| `potvarkio_nr` | `string` | — | `4` | `open` | — | Dokumento registracijos numeris | — |
| `rusis` | `string` | — | `4` | `open` | — | Dokumento rūšis | — |
| `url` | `string` | — | `4` | `open` | — | Suformuota nuoroda į dokumentą | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Dokumento pavadinimas | — |
| `padalinys` | `string` | — | `4` | `open` | — | Savivaldybės padalinys, parengęs dokumentą | — |
| `statusas` | `string` | — | `4` | `open` | — | Dokumento statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv
