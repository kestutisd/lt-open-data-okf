---
type: Table
title: "PAHDiagnoze — \"Asmenys, kuriems diagnozuota PAH\""
description: "\"Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a) kaip pagrindinė, lydinti arba skyriaus..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHDiagnoze"
tags: [gov, lsd, pahdiagnoze, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3888/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/pah_diagnozes"
    author: "team:vda"
    last_modified: "2026-05-06T00:00:00Z"
---

# PAHDiagnoze — "Asmenys, kuriems diagnozuota PAH"

"Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a) kaip pagrindinė, lydinti arba skyriaus diagnozė. Pateikiama jų gimimo data (metų tikslumu), kiekvieno PAH diagnozės kodo pirmo įrašymo data, mirties data (mėnesio tikslumu) bei pagrindinė mirties priežastis."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/pah_diagnozes/PAHDiagnoze`[^manifest]
- **Dataset:** ["Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys"](../pah_diagnozes.md) (`datasets/gov/lsd/sveikata/pah_diagnozes`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHDiagnoze` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-05-06`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/pah_diagnozes (https://data.gov.lt/datasets/3888/)
