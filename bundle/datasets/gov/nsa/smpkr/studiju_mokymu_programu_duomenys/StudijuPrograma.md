---
type: Table
title: "StudijuPrograma — Studijų ir mokymų programos"
description: "Lentelėje pateiktos studijų ir mokymų programos iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/StudijuPrograma"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# StudijuPrograma — Studijų ir mokymų programos

Lentelėje pateiktos studijų ir mokymų programos iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR). Duomenų apie programas laiko aprėptis - nuo 1996 metų iki šių dienų. Duomenys atnaujinami kas mėnesį.

- **Model:** `datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/StudijuPrograma`[^manifest]
- **Dataset:** [Studijų ir mokymų programų duomenys](../studiju_mokymu_programu_duomenys.md) (`datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`)
- **Manifest CSV:** [datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/StudijuPrograma`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sukurtas duomenų eilutės identifikatorius | — |
| `prg_valst_kodas` | `string` | — | `4` | `open` | — | Programos valstybinis kodas | — |
| `prg_isced_kodas` | `string` | — | `4` | `open` | — | Programos ISCED kodas | — |
| `prg_pavad_lt` | `string` | — | `4` | `open` | — | Programos pavadinimas lietuvių kalba | — |
| `prg_pavad_en` | `string` | — | `4` | `open` | — | Programos pavadinimas anglų kalba | — |
| `prg_lygmuo_lt` | `string` | — | `4` | `open` | — | Programos lygmuo lietuvių kalba | — |
| `prg_lygmuo_en` | `string` | — | `4` | `open` | — | Programos lygmuo anglų kalba | — |
| `stud_tipas_lt` | `string` | — | `4` | `open` | — | Studijų tipas lietuvių kalba | — |
| `stud_tipas_en` | `string` | — | `4` | `open` | — | Studijų tipas anglų kalba | — |
| `stud_pakopa_lt` | `string` | — | `4` | `open` | — | Studijų pakopa lietuvių kalba | — |
| `stud_pakopa_en` | `string` | — | `4` | `open` | — | Studijų pakopa anglų kalba | — |
| `prg_apimtis_kred` | `number` | — | `4` | `open` | — | Programos apimtis kreditais | — |
| `teik_issilav_lt` | `string` | — | `4` | `open` | — | Programos suteikiamas išsilavinimas lietuvių kalba | — |
| `teik_issilav_en` | `string` | — | `4` | `open` | — | Programos suteikiamas anglų kalba | — |
| `stud_sritis_lt` | `string` | — | `4` | `open` | — | Studijų sritis lietuvių kalba | — |
| `stud_sritis_en` | `string` | — | `4` | `open` | — | Studijų sritis anglų kalba | — |
| `stud_posritis_lt` | `string` | — | `4` | `open` | — | Studijų posritis lietuvių kalba | — |
| `stud_posritis_en` | `string` | — | `4` | `open` | — | Studijų posritis anglų kalba | — |
| `prg_ireg_data` | `date` | `D` | `4` | `open` | — | Programos įregistravimo data | — |
| `prg_isreg_data` | `date` | `D` | `4` | `open` | — | Programos išregistravimo data | — |
| `prg_isreg_priezast_lt` | `string` | — | `4` | `open` | — | Išregistravimo priežastis lietuvių kalba | — |
| `prg_reg_inst_lt` | `string` | — | `4` | `open` | — | Programą registruojančios institucijos pavadinimas lietuvių kalba | — |
| `prg_reg_inst_en` | `string` | — | `4` | `open` | — | Programą registruojančios institucijos pavadinimas anglų kalba | — |
| `prg_reg_inst_kodas` | `string` | — | `4` | `open` | — | Programą registruojančios institucijos kodas | — |
| `prg_reg_inst_kodo_tipas` | `string` | — | `4` | `open` | — | Programą registruojančios institucijos kodo tipas | — |
| `prg_reg_inst_tipas` | `string` | — | `4` | `open` | — | Programą registruojančios institucijos tipas | — |
| `prg_reg_inst_adr` | `string` | — | `4` | `open` | — | Programą registruojančios institucijos adresas | — |
| `prg_paskut_kitimas` | `date` | `D` | `4` | `open` | — | Paskutinio programos pakeitimo data | — |
| `duom_paskut_redag` | `date` | `D` | `4` | `open` | — | Paskutinio duomenų redagavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv
