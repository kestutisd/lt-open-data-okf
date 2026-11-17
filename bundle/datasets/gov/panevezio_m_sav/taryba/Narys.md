---
type: Table
title: "Narys — Rinkinyje pateikiamas buvusių ir esamų Panevėžio miesto tarybos narių sąrašas. Duomenys apima laikotarpį nuo 2007m. iki šių dienų."
description: "Spinta table datasets/gov/panevezio_m_sav/taryba/Narys (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/taryba/Narys"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/tarybos_nariai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Narys — Rinkinyje pateikiamas buvusių ir esamų Panevėžio miesto tarybos narių sąrašas. Duomenys apima laikotarpį nuo 2007m. iki šių dienų.

- **Model:** `datasets/gov/panevezio_m_sav/taryba/Narys`[^manifest]
- **Dataset:** [Panevėžio miesto tarybos narių sąrašas](../taryba.md) (`datasets/gov/panevezio_m_sav/taryba`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/taryba/Narys`
- **Primary Key (`ref`):** `delegato_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `delegato_id` | `string` | — | `4` | `open` | — | Tarybos nario identifikacinis numeris | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Tarybos nario vardas ir pavardė | — |
| `pareigos` | `string` | — | `4` | `open` | — | Tarybos nario pareigos | — |
| `ar_aktyvus` | `boolean` | — | `4` | `open` | — | Požymis, ar Tarybos narys eina pareigas einamosios kadencijos metu | — |
| `duomenu_sviezumas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/tarybos_nariai.csv
