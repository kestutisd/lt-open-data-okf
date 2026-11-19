---
type: Table
title: "ProgramosStudentas — Studentai studijų programose"
description: "Lentelėje pateikiami studentų, bent šiek tiek studijavusių ir baigusių tam tikrą programą konkrečiais metais, skaičiai iš Nacionalinės švietimo agentūros (NŠA) Studentų registro (SR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStudentas"
tags: [gov, nsa, programosstudentas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69"
    title: "atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3918/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ProgramosStudentas — Studentai studijų programose

Lentelėje pateikiami studentų, bent šiek tiek studijavusių ir baigusių tam tikrą programą konkrečiais metais, skaičiai iš Nacionalinės švietimo agentūros (NŠA) Studentų registro (SR). Duomenų laiko aprėptis - nuo 1992 metų. Lentelė atnaujinama kasmet, rudens antroje pusėje. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStudentas`[^manifest]
- **Dataset:** [Studijų ir mokymų programų duomenys](../studiju_mokymu_programu_duomenys.md) (`datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStudentas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sukurtas duomenų eilutės identifikatorius | — |
| `metai` | `date` | `D` | `4` | `open` | — | Metai | — |
| `prg_valst_kodas` | `string` | — | `4` | `open` | — | Studijų programos valstybinis kodas | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Švietimo institucijos identifikacinis (JAR) kodas | — |
| `stud_studijav` | `integer` | — | `4` | `open` | — | Studentų, studijavusių programoje konkrečiais metais, skaičius iš NŠA studentų registro | — |
| `stud_baige` | `integer` | — | `4` | `open` | — | Studentų, baigusių programą konkrečiais metais, skaičius iš NŠA studentų registro | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L69)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys (https://data.gov.lt/datasets/3918/)
