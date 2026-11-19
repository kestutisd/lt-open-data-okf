---
type: Table
title: "LaboratorinisTyrimas — Laboratorinių tyrimų agreguoti skaičiai"
description: "\"Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai/LaboratorinisTyrimas"
tags: [gov, lsd, laboratorinistyrimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4129/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-18T00:00:00Z"
---

# LaboratorinisTyrimas — Laboratorinių tyrimų agreguoti skaičiai

"Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. Laboratorinių tyrimų agreguotas skaičius, koduojamų su LOINC ir be LOINC, pateiktas atskirai."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/lab_tyrimai/LaboratorinisTyrimas`[^manifest]
- **Dataset:** [Laboratorinių tyrimų agreguoti skaičiai](../lab_tyrimai.md) (`datasets/gov/lsd/sveikata/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai/LaboratorinisTyrimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-02-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `tyr_pav_analite` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas ir analitė (Tyrimas: analitė) | — |
| `skaicius_be_loinc` | `integer` | — | `4` | `open` | — | Tyrimų skaičius be LOINC kodo | — |
| `analites_loinc_kodas` | `string` | — | `4` | `open` | — | LOINC kodas | — |
| `skaicius_loinc` | `integer` | — | `4` | `open` | — | Tyrimų skaičius su LOINC kodu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/lab_tyrimai (https://data.gov.lt/datasets/4129/)
