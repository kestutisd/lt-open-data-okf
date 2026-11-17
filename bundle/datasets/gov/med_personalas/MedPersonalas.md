---
type: Table
title: "MedPersonalas — Medicininio personalo etatai"
description: "Spinta table datasets/gov/med_personalas/MedPersonalas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/med_personalas/MedPersonalas"
tags: [gov, med_personalas, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MedPersonalas — Medicininio personalo etatai

- **Model:** `datasets/gov/med_personalas/MedPersonalas`[^manifest]
- **Dataset:** [Lietuvos sveikatos universiteto Kauno klinikų medicininio personalo etatai](../med_personalas.md) (`datasets/gov/med_personalas`)
- **Manifest CSV:** [datasets/gov/lsmu/med_personalas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/med_personalas/MedPersonalas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `aspi_skyrius` | `string` | — | `4` | `open` | — | Ambulatorines asmens sveikatos priežiūros skyriaus kodas | — |
| `aspi_skyriaus_id` | `string` | — | `4` | `open` | — | Ambulatorines asmens sveikatos priežiūros skyriaus id | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Darbuotojo pseudomizuotas asmens kodas | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Paciento asmens kodo trūkumai | — |
| `lytis` | `string` | — | `4` | `open` | — | Darbuotojo lytis (Angliškos reikšmės) | — |
| `ak_lytis` | `string` | — | `4` | `open` | — | Darbuotojo lytis nurodyta asmens kode | — |
| `gim_metai` | `date` | `Y` | `4` | `open` | — | Mediko gimimo metai | — |
| `ak_gim_metai` | `date` | `Y` | `4` | `open` | — | Mediko gimimo metai nurodyti asmens kode | — |
| `pareigybe` | `string` | — | `4` | `open` | — | Mediko pareigos | — |
| `dirba_nuo` | `date` | `D` | `4` | `open` | — | Darbo santykių pradžios data | — |
| `dirba_iki` | `date` | `D` | `4` | `open` | — | Darbo santykių pabaigos data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ak_validacija` | `"Tinkamas"` | — | — | Asmens kodas atitinka LT asmens kodo sudarymo taisykles | — |
| `ak_validacija` | `"Netinkamas ilgis"` | — | — | Asmens kodas netinkamo ilgio | — |
| `ak_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Asmens kode nurodytas netinkamas paskutinis skaitmuo | — |
| `ak_validacija` | `"Netinkama gimimo data"` | — | — | Asmens kode nurodyta netinkama gimimo data | — |
| `lytis` | `"F"` | — | `open` | Female | — |
| `lytis` | `"M"` | — | `open` | Male | — |
| `ak_lytis` | `"M"` | — | `open` | Moteris | — |
| `ak_lytis` | `"V"` | — | `open` | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv
