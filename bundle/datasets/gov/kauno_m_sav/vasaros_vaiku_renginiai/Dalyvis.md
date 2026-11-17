---
type: Table
title: "Dalyvis — Dalyvių sąrašas"
description: "Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Dalyvis"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dalyvis — Dalyvių sąrašas

Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas.

- **Model:** `datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Dalyvis`[^manifest]
- **Dataset:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai](../vasaros_vaiku_renginiai.md) (`datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Dalyvis`
- **Primary Key (`ref`):** `vda_primary_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_primary_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `renginio_id` | `ref` | [/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Renginys[renginio_id]](Renginys.md) | `4` | `open` | — | Renginio identifikatorius | — |
| `renginio_pav` | `string` | — | `4` | `open` | — | Užsiėmimo pavadinimas | — |
| `vaiko_ask` | `string` | — | `4` | `open` | — | Užkoduotas vaiko asmens kodas | — |
| `vaik_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Vaiko gimimo metai | — |
| `mokyklos_id` | `string` | — | `4` | `open` | — | Mokykla | — |
| `klase` | `string` | — | `4` | `open` | — | Klasė | — |
| `spec_grupe` | `boolean` | — | `4` | `open` | — | Specialioji grupė | — |
| `registracijos_laikas` | `datetime` | `S` | `4` | `open` | — | Registracijos data ir laikas | — |
| `vaika_registravo_ask` | `string` | — | `4` | `open` | — | Užkoduotas vaiką registravusio asmens kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv
