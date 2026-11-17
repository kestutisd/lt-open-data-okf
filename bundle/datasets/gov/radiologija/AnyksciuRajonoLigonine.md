---
type: Table
title: "AnyksciuRajonoLigonine — Anykščių rajono ligoninės pacientams atlikti radiologiniai tyrimai"
description: "Anykščių rajono ligoninės naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/AnyksciuRajonoLigonine"
tags: [gov, radiologija, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L54"
    last_modified: "2026-11-11T14:39:20Z"
---

# AnyksciuRajonoLigonine — Anykščių rajono ligoninės pacientams atlikti radiologiniai tyrimai

Anykščių rajono ligoninės naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys. Kaupiamų duomenų aprėptis laike – nuo 2013 m., atnaujinant duomenis kasdien. Duomenų rinkinį sudaro: paciento pseudonimizuotas asmens kodas, tyrimo studijos identifikatorius ir data, paciento gimimo metai, lytis, tyrimo serijos identifikatorius, aprašymas ir modalumas, tirtos kūno dalies duomenys, medicininio atvaizdo identifikatorius, apšvita arksekundėmis ir fotometrinė interpretacija. Vienas įrašas atitinka vieną medicininį atvaizdą (visų medicininių atvaizdų identifikatoriai unikalūs).

- **Model:** `datasets/gov/radiologija/AnyksciuRajonoLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L54](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L54)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/AnyksciuRajonoLigonine`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento asmens kodas | — |
| `tyrimo_studijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyrimo_serijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tirta_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `4` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo unikalus identifikatorius | — |
| `apsvita` | `number` | `″` | `4` | `open` | — | Apšvita arksekundėmis | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"moteris"` | `M` | — | Moteris | — |
| `paciento_lytis` | `"kita"` | `K` | — | Kita | — |
| `tyrimo_serijos_modalumas` | `"Kompiuterinė tomografija"` | `CT` | — | Kompiuterinė tomografija | — |
| `tyrimo_serijos_modalumas` | `"Skaitmeninė radiografija"` | `DX` | — | Skaitmeninė radiografija | — |
| `tyrimo_serijos_modalumas` | `"Kompiuterinė radiografija"` | `CR` | — | Kompiuterinė radiografija | — |
| `tyrimo_serijos_modalumas` | `"SR dokumentas"` | `SR` | — | SR dokumentas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv
