---
type: Table
title: "PAHDiagnoze — Asmenys, kuriems diagnozuota PAH"
description: "Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a) kaip..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHDiagnoze"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# PAHDiagnoze — Asmenys, kuriems diagnozuota PAH

Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a) kaip pagrindinė, lydinti arba skyriaus diagnozė. Pateikiama jų gimimo data (metų tikslumu), kiekvieno PAH diagnozės kodo pirmo įrašymo data, mirties data (mėnesio tikslumu) bei pagrindinė mirties priežastis.

- **Model:** `datasets/gov/lsd/sveikata/pah_diagnozes/PAHDiagnoze`[^manifest]
- **Dataset:** [Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys](../pah_diagnozes.md) (`datasets/gov/lsd/sveikata/pah_diagnozes`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHDiagnoze`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gimimo_data` | `date` | `Y` | `4` | `open` | — | Gimimo data (metų tikslumu) | — |
| `i27_0_pirma_diag` | `date` | `D` | `4` | `open` | — | Pirmos I27.0 diagnozės data | — |
| `i27_2_pirma_diag` | `date` | `D` | `4` | `open` | — | Pirmos I27.2 diagnozės data | — |
| `i27_8_pirma_diag` | `date` | `D` | `4` | `open` | — | Pirmos I27.8 diagnozės data | — |
| `mirties_data` | `date` | `M` | `4` | `open` | — | Mirties data (mėnesio tikslumu) | — |
| `pagr_mirties_priez` | `string` | — | `4` | `open` | — | Pagrindinė mirties priežastis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv
