---
type: Table
title: "SARSCoVTestas — Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai"
description: "Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie žmonėms atliktus SARS-CoV-2 polimerazinės grandininės reakcijos (PGR) ir antigeno testus."
resource: "https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita/SARSCoVTestas"
tags: [gov, nvspl, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# SARSCoVTestas — Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai

Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie žmonėms atliktus SARS-CoV-2 polimerazinės grandininės reakcijos (PGR) ir antigeno testus. Viena eilutė atitinka vieną asmenį, kuriam buvo atliktas testas. Eilutės informaciją sudaro unikalios eilutės identifikatorius, tiriamojo amžius ir lytis, laboratorijos priskirtas mėginio identifikacinis numeris, mėginio paėmimo data, antigeno ir PGR testų rezultatai, laboratorijų, kurios atliko PGR tyrimą ir sekoskaitą pavadinimai.

- **Model:** `datasets/gov/nvspl/sekoskaita/SARSCoVTestas`[^manifest]
- **Dataset:** [SARS-CoV-2 viruso sekoskaitos duomenys](../sekoskaita.md) (`datasets/gov/nvspl/sekoskaita`)
- **Manifest CSV:** [datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita/SARSCoVTestas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Įrašo identifikacinis numeris | Unikalios eilutės identifikatorius |
| `amzius` | `integer` | — | `4` | `open` | — | Tiriamojo amžius | — |
| `lytis` | `string` | — | `4` | `open` | — | Tiriamojo lytis | — |
| `meg_id` | `string` | — | `4` | `open` | — | Mėginio identifikacinis numeris | — |
| `meginio_data` | `date` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `pgr_rezultatas` | `string` | — | `4` | `open` | — | PGR rezultatas | SARS-CoV-2 polimerazinės grandininės reakcijos (PGR) tyrimo rezultatas (1 - teigiamas, 0 - neigiamas) |
| `antigeno_rezultatas` | `string` | — | `4` | `open` | — | Antigeno tyrimo rezultatas | SARS-CoV-2 antigeno tyrimo rezultatas (1- teigiamas, 0 - neigiamas) |
| `pgr_lab_pav` | `string` | — | `4` | `open` | — | PGR tyrimą atlikusios laboratorijos pavadinimas | — |
| `sekosk_lab_pav` | `string` | — | `4` | `open` | — | Sekoskaitą atlikusios laboratorijos pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `pgr_rezultatas` | `"0.0"` | — | — | Neigiamas | — |
| `pgr_rezultatas` | `"1.0"` | — | — | Teigiamas | — |
| `antigeno_rezultatas` | `"0.0"` | — | — | Neigiamas | — |
| `antigeno_rezultatas` | `"1.0"` | — | — | Teigiamas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv
