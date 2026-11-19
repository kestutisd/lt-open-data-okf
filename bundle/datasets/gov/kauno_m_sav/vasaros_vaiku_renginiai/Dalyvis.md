---
type: Table
title: "Dalyvis — Dalyvių sąrašas"
description: "Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Dalyvis"
tags: [gov, kauno_m_sav, dalyvis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2737/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dalyvis — Dalyvių sąrašas

Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Dalyvis`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės vaikų vasaros renginių duomenys](../vasaros_vaiku_renginiai.md) (`datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Dalyvis` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_primary_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_primary_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `renginio_id` | `ref` | [Renginys](Renginys.md) (`level=4 UUID` via `Renginys[renginio_id]`: `renginio_id._id`) | `4` | `open` | — | Renginio identifikatorius | — |
| `renginio_pav` | `string` | — | `4` | `open` | — | Užsiėmimo pavadinimas | — |
| `vaiko_ask` | `string` | — | `4` | `open` | — | Užkoduotas vaiko asmens kodas | — |
| `vaik_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Vaiko gimimo metai | — |
| `mokyklos_id` | `string` | — | `4` | `open` | — | Mokykla | — |
| `klase` | `string` | — | `4` | `open` | — | Klasė | — |
| `spec_grupe` | `boolean` | — | `4` | `open` | — | Specialioji grupė | — |
| `registracijos_laikas` | `datetime` | `S` | `4` | `open` | — | Registracijos data ir laikas | — |
| `vaika_registravo_ask` | `string` | — | `4` | `open` | — | Užkoduotas vaiką registravusio asmens kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai (https://data.gov.lt/datasets/2737/)
