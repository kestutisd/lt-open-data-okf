---
type: Table
title: "Ligonis — Pacientų sąrašas"
description: "Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai/Ligonis"
tags: [gov, palangos_gintaras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ligonis — Pacientų sąrašas

Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų sąrašas. Duomenys pateikiami už 2016-2023 metus

- **Model:** `datasets/gov/palangos_gintaras/pacientai/Ligonis`[^manifest]
- **Dataset:** [datasets/gov/palangos_gintaras/pacientai](../pacientai.md) (`datasets/gov/palangos_gintaras/pacientai`)
- **Manifest CSV:** [datasets/gov/palangos_gintaras/pacientai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai/Ligonis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikacinis numeris | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `neigalumo_tipas` | `string` | — | `4` | `open` | — | Paciento neįgalumno tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv
