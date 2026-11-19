---
type: Table
title: "Ligonis — Pacientų sąrašas"
description: "Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai/Ligonis"
tags: [gov, palangos_gintaras, ligonis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2720/"
    title: "data.gov.lt DCAT-AP — datasets/gov/palangos_gintaras/pacientai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Ligonis — Pacientų sąrašas

Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų sąrašas. Duomenys pateikiami už 2016-2023 metus[^manifest]

- **Model:** `datasets/gov/palangos_gintaras/pacientai/Ligonis`[^manifest]
- **Dataset:** [Palangos vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų registracijų sąrašas](../pacientai.md) (`datasets/gov/palangos_gintaras/pacientai`)[^manifest]
- **Manifest CSV:** [datasets/gov/palangos_gintaras/pacientai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai/Ligonis` (`deployed`)[^manifest]
- **Provider:** `palangos_gintaras` — Vaikų reabilitacijos sanatorija "Palangos gintaras" *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikacinis numeris | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `neigalumo_tipas` | `string` | — | `4` | `open` | — | Paciento neįgalumno tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/palangos_gintaras/pacientai (https://data.gov.lt/datasets/2720/)
