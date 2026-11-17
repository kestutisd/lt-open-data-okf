---
type: Table
title: "ProgramosAkreditacija — Studijų ir mokymų programų akreditacijos"
description: "Lentelėje pateikti studijų ir mokymų programų akreditacijų duomenys iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosAkreditacija"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L37"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProgramosAkreditacija — Studijų ir mokymų programų akreditacijos

Lentelėje pateikti studijų ir mokymų programų akreditacijų duomenys iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR). Šių duomenų laiko aprėptis - nuo 2002 metų iki šių dienų. Duomenys atnaujinami kas mėnesį.

- **Model:** `datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosAkreditacija`[^manifest]
- **Dataset:** [Studijų ir mokymų programų duomenys](../studiju_mokymu_programu_duomenys.md) (`datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`)
- **Manifest CSV:** [datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L37)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosAkreditacija`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sukurtas duomenų eilutės identifikatorius | — |
| `prg_valst_kodas` | `string` | — | `4` | `open` | — | Programos valstybinis kodas | — |
| `prg_isced_kodas` | `string` | — | `4` | `open` | — | Programos ISCED kodas | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Švietimo institucijos identifikacinis (JAR) kodas | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Sprendimas, ar programa akredituota | — |
| `akred_data` | `date` | — | `4` | `open` | — | Programos akreditacijos data | — |
| `akred_terminas` | `date` | `D` | `4` | `open` | — | Programos akreditacijos terminas | — |
| `akred_paskut_redagav` | `date` | `D` | `4` | `open` | — | Programos akreditacijos paskutinio redagavimo data | — |
| `akred_ivert_kriterijus_lt` | `string` | — | `4` | `open` | — | Programos įvertinimo kriterijus lietuvių kalba | — |
| `akred_ivert_kriterijus_en` | `string` | — | `4` | `open` | — | Programos įvertinimo kriterijus anglų kalba | — |
| `akred_ivert_balas` | `string` | — | `4` | `open` | — | Įvertis balais | — |
| `balo_paskut_redagav` | `date` | `D` | `4` | `open` | — | Suteikto įvertinimo balais paskutinio redagavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv
