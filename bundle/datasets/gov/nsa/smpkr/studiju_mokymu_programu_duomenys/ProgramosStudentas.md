---
type: Table
title: "ProgramosStudentas — Studentai studijų programose"
description: "Lentelėje pateikiami studentų, bent šiek tiek studijavusių ir baigusių tam tikrą programą konkrečiais metais, skaičiai iš Nacionalinės švietimo agentūros (NŠA) Studentų registro (SR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStudentas"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProgramosStudentas — Studentai studijų programose

Lentelėje pateikiami studentų, bent šiek tiek studijavusių ir baigusių tam tikrą programą konkrečiais metais, skaičiai iš Nacionalinės švietimo agentūros (NŠA) Studentų registro (SR). Duomenų laiko aprėptis - nuo 1992 metų. Lentelė atnaujinama kasmet, rudens antroje pusėje.

- **Model:** `datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStudentas`[^manifest]
- **Dataset:** [Studijų ir mokymų programų duomenys](../studiju_mokymu_programu_duomenys.md) (`datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`)
- **Manifest CSV:** [datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStudentas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sukurtas duomenų eilutės identifikatorius | — |
| `metai` | `date` | `D` | `4` | `open` | — | Metai | — |
| `prg_valst_kodas` | `string` | — | `4` | `open` | — | Studijų programos valstybinis kodas | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Švietimo institucijos identifikacinis (JAR) kodas | — |
| `stud_studijav` | `integer` | — | `4` | `open` | — | Studentų, studijavusių programoje konkrečiais metais, skaičius iš NŠA studentų registro | — |
| `stud_baige` | `integer` | — | `4` | `open` | — | Studentų, baigusių programą konkrečiais metais, skaičius iš NŠA studentų registro | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv
