---
type: Table
title: "DruskininkuLigonine — Druskininkų ligoninės pacientams atlikti radiologiniai tyrimai"
description: "Druskininkų ligoninės naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/DruskininkuLigonine"
tags: [gov, radiologija, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L78"
    last_modified: "2026-11-11T14:39:20Z"
---

# DruskininkuLigonine — Druskininkų ligoninės pacientams atlikti radiologiniai tyrimai

Druskininkų ligoninės naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys. Kaupiamų duomenų aprėptis laike – nuo 2001 m., atnaujinant duomenis kasdien. Duomenų rinkinį sudaro: paciento pseudonimizuotas asmens kodas, tyrimo studijos data, paciento gimimo metai, lytis, tirtos kūno dalies duomenys, tyrimo serijos modalumas ir aprašymas, medicininio atvaizdo identifikatorius, apšvita arksekundėmis, tyrimo seriją atlikusio techniko pseudonimizuoti vardas ir pavardė, fotometrinė interpretacija, ir tyrimo serijos protokolas. Vienas įrašas atitinka vieną medicininį atvaizdą (visų medicininių atvaizdų identifikatoriai unikalūs).

- **Model:** `datasets/gov/radiologija/DruskininkuLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L78](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L78)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/DruskininkuLigonine`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento asmens kodas | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `kuno_dalis` | `string` | — | `4` | `open` | — | Tirta kūno dalis | — |
| `modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `3` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo unikalus identifikatorius | — |
| `apsvita` | `number` | `″` | `4` | `open` | — | Apšvita arksekundėmis | — |
| `atlikes_technikas` | `string` | — | `4` | `open` | — | Tyrimo seriją atlikusio techniko pseudonimizuoti vardas ir pavardė | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |
| `protokolas` | `string` | — | `3` | `open` | — | Tyrimo serijos protokolas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `modalumas` | `"CT"` | — | — | Kompiuterinė tomografija | — |
| `modalumas` | `"CR"` | — | — | Kompiuterinė radiografija | — |
| `modalumas` | `"DX"` | — | — | Skaitmeninė radiografija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv
