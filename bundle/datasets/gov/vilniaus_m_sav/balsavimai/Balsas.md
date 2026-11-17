---
type: Table
title: "Balsas — Vilniaus miesto tarybos narių individualūs balsavimų duomenys"
description: "Spinta table datasets/gov/vilniaus_m_sav/balsavimai/Balsas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Balsas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L36"
    last_modified: "2026-11-11T14:39:20Z"
---

# Balsas — Vilniaus miesto tarybos narių individualūs balsavimų duomenys

- **Model:** `datasets/gov/vilniaus_m_sav/balsavimai/Balsas`[^manifest]
- **Dataset:** [Vilniaus miesto tarybos balsavimai](../balsavimai.md) (`datasets/gov/vilniaus_m_sav/balsavimai`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/balsavimai.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L36)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Balsas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `balsavimo_id` | `string` | — | `4` | `open` | — | Balsavimo identifikacinis numeris | — |
| `balsavimo_laikas` | `datetime` | `S` | `4` | `open` | — | Balsavimo laiko žyma | — |
| `narys` | `string` | — | `4` | `open` | — | Tarybos narys, dalyvavęs balsavime | — |
| `balsas` | `string` | — | `4` | `open` | — | Tarybos nario atiduotas balsavimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv
