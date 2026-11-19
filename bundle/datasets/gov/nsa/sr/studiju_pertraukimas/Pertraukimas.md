---
type: Table
title: "Pertraukimas — Studentų studijų pertraukimai ir nutraukimai"
description: "Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš studentų registro (SR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas/Pertraukimas"
tags: [gov, nsa, pertraukimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2616/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/sr/studiju_pertraukimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pertraukimas — Studentų studijų pertraukimai ir nutraukimai

Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš studentų registro (SR). Persidengiantys pertraukimai (pvz.: studentas pertraukė studijas 2021-09-04 - 2022-01-30 ir tuomet vėl 2022-01-31 - 2022-09-01) yra sutraukti į vieną laikotarpį. Duomenys kaupiami nuo 2010 m.[^manifest]

- **Model:** `datasets/gov/nsa/sr/studiju_pertraukimas/Pertraukimas`[^manifest]
- **Dataset:** [Studentų studijų pertraukimai ir nutraukimai](../studiju_pertraukimas.md) (`datasets/gov/nsa/sr/studiju_pertraukimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas/Pertraukimas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/sr/studiju_pertraukimas (https://data.gov.lt/datasets/2616/)
