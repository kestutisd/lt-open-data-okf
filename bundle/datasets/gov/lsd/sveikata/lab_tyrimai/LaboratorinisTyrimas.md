---
type: Table
title: "LaboratorinisTyrimas — Laboratorinių tyrimų agreguoti skaičiai"
description: "Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai/LaboratorinisTyrimas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaboratorinisTyrimas — Laboratorinių tyrimų agreguoti skaičiai

Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. Laboratorinių tyrimų agreguotas skaičius, koduojamų su LOINC ir be LOINC, pateiktas atskirai.

- **Model:** `datasets/gov/lsd/sveikata/lab_tyrimai/LaboratorinisTyrimas`[^manifest]
- **Dataset:** [Laboratorinių tyrimų agreguoti skaičiai](../lab_tyrimai.md) (`datasets/gov/lsd/sveikata/lab_tyrimai`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai/LaboratorinisTyrimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `tyr_pav_analite` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas ir analitė (Tyrimas: analitė) | — |
| `skaicius_be_loinc` | `integer` | — | `4` | `open` | — | Tyrimų skaičius be LOINC kodo | — |
| `analites_loinc_kodas` | `string` | — | `4` | `open` | — | LOINC kodas | — |
| `skaicius_loinc` | `integer` | — | `4` | `open` | — | Tyrimų skaičius su LOINC kodu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv
