---
type: Table
title: "MedPersonalas — Medicininio personalo etatai"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami dirbančio medicininio personalo tarnybiniai duomenys: darbuotojo pseudonimizuotas asmens kodas, lytis, gimimo metai, darbuotojui priskirtas skyrius..."
resource: "https://get.data.gov.lt/datasets/gov/med_personalas/MedPersonalas"
tags: [gov, med_personalas, medpersonalas, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MedPersonalas — Medicininio personalo etatai

**Dataset Context:** Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami dirbančio medicininio personalo tarnybiniai duomenys: darbuotojo pseudonimizuotas asmens kodas, lytis, gimimo metai, darbuotojui priskirtas skyrius, pareigos, darbo pradžios ir pabaigos datos. Atkreipiame dėmesį, kad Kauno klinikose darbuotojų duomenys tvarkomi rankiniu būdų, todėl duomenyse gali atsirasti neatitikimų. Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/med_personalas/MedPersonalas`[^manifest]
- **Dataset:** [Lietuvos sveikatos universiteto Kauno klinikų medicininio personalo etatai](../med_personalas.md) (`datasets/gov/med_personalas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/med_personalas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/med_personalas/MedPersonalas` (`deployed`)[^manifest]
- **Provider:** `med_personalas`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ak_validacija` | `"Tinkamas"` | — | — | Asmens kodas atitinka LT asmens kodo sudarymo taisykles | — |
| `ak_validacija` | `"Netinkamas ilgis"` | — | — | Asmens kodas netinkamo ilgio | — |
| `ak_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Asmens kode nurodytas netinkamas paskutinis skaitmuo | — |
| `ak_validacija` | `"Netinkama gimimo data"` | — | — | Asmens kode nurodyta netinkama gimimo data | — |
| `lytis` | `"F"` | — | `open` | Female | — |
| `lytis` | `"M"` | — | `open` | Male | — |
| `ak_lytis` | `"M"` | — | `open` | Moteris | — |
| `ak_lytis` | `"V"` | — | `open` | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L6)
