---
type: Table
title: "RespublikineSiauliuLigonine — Respublikinės Šiaulių ligoninės pacientams atliktų radiologinių tyrimų duomenys"
description: "Informacinėje sistemoje „MedDream“ kaupiami Respublikinės Šiaulių ligoninės pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/RespublikineSiauliuLigonine"
tags: [gov, radiologija, respublikinesiauliuligonine, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L235"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L235"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# RespublikineSiauliuLigonine — Respublikinės Šiaulių ligoninės pacientams atliktų radiologinių tyrimų duomenys

Informacinėje sistemoje „MedDream“ kaupiami Respublikinės Šiaulių ligoninės pacientams atliktų radiologinių tyrimų duomenys. Duomenų rinkinyje pateikiami ir iki šiol atnaujinami nuo 2011 metų kaupiami duomenys. Vienas įrašas atitinka vieną tyrimo medicininį atvaizdą (visų tyrimo atvaizdų identifikatoriai unikalūs). Duomenų rinkinį sudaro: paciento pseudonimizuotas asmens kodas, tyrimo studijos identifikatorius, data, paciento gimimo metai, lytis, svoris, ūgis, tyrimo serijos identifikatorius, tirta kūno dalis, serijos modalumas, aprašymas, tyrimo atvaizdo identifikatorius, apšvita, spinduliuotės dozė ir fotometrinė interpretacija. Dėl didelio medicininio atvaizdų kiekio įstaigos duomenų bazėje, rinkinys gali būti sudarytas panaudojus tik dalį visų galimų atvaizdų. Duomenų teikėjas – VšĮ Respublikinė Šiaulių ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/radiologija/RespublikineSiauliuLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L235](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L235)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/RespublikineSiauliuLigonine` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento asmens kodas | — |
| `tyrimo_studijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_svoris` | `number` | `kg` | `4` | `open` | — | Paciento svoris | — |
| `paciento_ugis` | `integer` | `cm` | `4` | `open` | — | Paciento ugis | — |
| `tyrimo_serijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tirta_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta paciento kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `2` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo unikalus identifikatorius | — |
| `apsvita` | `number` | `″` | `4` | `open` | — | Apšvita arksekundėmis | — |
| `doze` | `number` | `dGy/cm^2` | `4` | `open` | — | Spinduliuotės dozė decigrėjais kvadratiniame centimetre | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `tyrimo_serijos_modalumas` | `"CT"` | — | — | Kompiuterinė tomografija | — |
| `tyrimo_serijos_modalumas` | `"CR"` | — | — | Kompiuterinė radiografija | — |
| `tyrimo_serijos_modalumas` | `"MR"` | — | — | Magnetinis rezonansas | — |
| `tyrimo_serijos_modalumas` | `"SR"` | — | — | SR dokumentas | — |
| `tyrimo_serijos_modalumas` | `"ECG"` | — | — | Elektro kardiografija | — |
| `tyrimo_serijos_modalumas` | `"PR"` | — | — | Prezentacijos būsena | — |
| `tyrimo_serijos_modalumas` | `"XA"` | — | — | Rentgeno angiografija | — |
| `tyrimo_serijos_modalumas` | `"MG"` | — | — | Mamografija | — |
| `tyrimo_serijos_modalumas` | `"KO"` | — | — | Raktinių objektų selekcija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L235 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L235)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
