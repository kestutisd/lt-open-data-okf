---
type: Table
title: "Pertraukimas — Studentų studijų pertraukimai ir nutraukimai"
description: "Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš studentų registro (SR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas/Pertraukimas"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/sr/studiju_pertraukimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pertraukimas — Studentų studijų pertraukimai ir nutraukimai

Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš studentų registro (SR). Persidengiantys pertraukimai (pvz.: studentas pertraukė studijas 2021-09-04 - 2022-01-30 ir tuomet vėl 2022-01-31 - 2022-09-01) yra sutraukti į vieną laikotarpį. Duomenys kaupiami nuo 2010 m.

- **Model:** `datasets/gov/nsa/sr/studiju_pertraukimas/Pertraukimas`[^manifest]
- **Dataset:** [Studentų studijų pertraukimai ir nutraukimai](../studiju_pertraukimas.md) (`datasets/gov/nsa/sr/studiju_pertraukimas`)
- **Manifest CSV:** [datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas/Pertraukimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `studento_stud_id` | `string` | — | `4` | `open` | — | Studento studijų identifikatorius | — |
| `st_id` | `string` | — | `4` | `open` | — | Studento identifikatorius | — |
| `studento_gimmetai` | `date` | `Y` | `4` | `open` | — | Studento gimimo metai | — |
| `studento_lytis` | `string` | — | `4` | `open` | — | Studento lytis | — |
| `etapas` | `string` | — | `4` | `open` | — | Studijų etapas (nutraukimas / pertraukimas) | — |
| `nutr_pert_priezastis` | `string` | — | `4` | `open` | — | Studijų nutraukimo / pertraukimo priežastis | — |
| `etapo_pradz_data` | `date` | `D` | `4` | `open` | — | Studijų nutraukimo / pertraukimo data | — |
| `grizimo_data` | `date` | `D` | `4` | `open` | — | Grįžimo į studijas data | — |
| `std_pakopos_pav` | `string` | — | `4` | `open` | — | Studijų pakopa | — |
| `kursas_i_kuri_grizo` | `string` | — | `4` | `open` | — | Studijų kursas į kurį grįžo studentas | — |
| `prg_stud_sritis_pav` | `string` | — | `4` | `open` | — | Studijų srities pavadinimas | — |
| `ins_pagr_tipas` | `string` | — | `4` | `open` | — | Studijų institucijos tipas | — |
| `std_studiju_pradzia` | `date` | `D` | `4` | `open` | — | Studijų pradžia | — |
| `std_numatoma_stud_pabaiga` | `date` | `D` | `4` | `open` | — | Numatoma studijų pabaiga | — |
| `stud_baigimo_data` | `date` | `D` | `4` | `open` | — | Studijų baigimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nutr_pert_priezastis` | `"update(property: ""nutr_pert_priezastis[]"", type: ""array"", source: ""Nutr_pert_priezastis"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/sr/studiju_pertraukimas.csv
