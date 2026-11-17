---
type: Table
title: "PreparatasStadija — Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinių preparatų stadijos pokyčius laike"
description: "Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir stadijos pokyčius."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai/PreparatasStadija"
tags: [gov, vvkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L57"
    last_modified: "2026-11-11T14:39:20Z"
---

# PreparatasStadija — Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinių preparatų stadijos pokyčius laike

Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir stadijos pokyčius. Vieną eilutę sudaro unikalus vaistinio preparato identifikacinis numeris, vaistinio preparato trumpas pavadinimas, stadija, oficiali stadijos atsiradimo data, kada stadija buvo įvesta/atnaujinta VVKT informacinėje sistemoje.

- **Model:** `datasets/gov/vvkt/vaistiniai_preparatai/PreparatasStadija`[^manifest]
- **Dataset:** [Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys](../vaistiniai_preparatai.md) (`datasets/gov/vvkt/vaistiniai_preparatai`)
- **Manifest CSV:** [datasets/gov/vvkt/vaistiniai_preparatai.csv#L57](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L57)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai/PreparatasStadija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | VDA ID | Valstybės Duomenų Agentūros įrašo identifikatorius. |
| `vid` | `string` | — | `4` | `open` | — | Vaisto ID | Unikalus vaistinio preparato identifikatorius, automatiškai generuojamas sistemos. |
| `preparato_pav` | `string` | — | `2` | `open` | — | Vaistinio preparato pavadinimas | Vaistinio preparato sugalvotas pavadinimas, vietoje formalaus ilgo pavadinimo. |
| `stadija` | `string` | — | `4` | `open` | — | Stadija | Dabartinė vaistinio preparato stadija. |
| `stad_data` | `date` | `1D` | `4` | `open` | — | Oficiali stadijos data | Vaistinio preparato oficiali stadijos pakeitimo data. |
| `stadija_sukurta` | `datetime` | `1L` | `4` | `open` | — | Stadija sukurta | Laiko žyma kada įrašas buvo sukurtas VVKT informacinėje sistemoje. |
| `stadija_atnaujinta` | `datetime` | `1L` | `4` | `open` | — | Stadija atnaujinta | Laiko žyma kada įrašas buvo atnaujintas VVKT informacinėje sistemoje. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `stadija` | `"Registruotas"` | — | — | Registruotas | — |
| `stadija` | `"Išregistruotas"` | — | — | Išregistruotas | — |
| `stadija` | `"Perregistruotas"` | — | — | Perregistruotas | — |
| `stadija` | `"Sustabdytas"` | — | — | Sustabdytas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv
