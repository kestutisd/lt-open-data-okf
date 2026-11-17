---
type: Table
title: "PasvalioLigonine — Pasvalio ligoninėje pacientams atliktų laboratorinių tyrimų duomenys"
description: "Pasvalio ligoninės OpenLIMS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/PasvalioLigonine"
tags: [gov, lab_tyrimai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L65"
    last_modified: "2026-11-11T14:39:20Z"
---

# PasvalioLigonine — Pasvalio ligoninėje pacientams atliktų laboratorinių tyrimų duomenys

Pasvalio ligoninės OpenLIMS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. Duomenys kaupiami nuo 2018 m. ir yra atnaujinami iki šiol. Duomenų rinkinio kaupiami duomenys apima įstaigos pavadinimą, paciento šifruotą identifikatorių, lytį, gimimo metus, tyrimo datą dienos tikslumu, rezultato interpretacijos stulpelį tiek su skaitiniais rezultatais, tiek su semantiniais vertinimais, atskirą skaitinių rezultatų stulpelį, suapvalintą 5 skaitmenų tikslumu, tyrimo metodo pavadinimą, normalių rezultato reikšmių rėžius, suapvalintus 5 skaitmenų tikslumu, rezultato matavimo vienetus bei paciento pagrindinės diagnozės TLK-10-AM kodą ir pavadinimą.

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/PasvalioLigonine`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L65](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L65)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/PasvalioLigonine`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `istaigos_pav` | `string` | — | `4` | `open` | — | Tyrimą atlikusios įstaigos pavadinimas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento šifruotas identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_data` | `date` | `D` | `4` | `open` | — | Tyrimo data dienos tikslumu | — |
| `tyrimo_rezultato_interpretacija` | `string` | — | `1` | `open` | — | Tyrimo rezultatų semantiniai vertinimai ir skaitiniai rezultatai | — |
| `tyrimo_skaitinis_rezultatas` | `number` | — | `4` | `open` | — | Tyrimo skaitinis rezultatas | — |
| `tyrimo_metodo_pavadinimas` | `string` | — | `4` | `open` | — | Tyrimo metodo pavadinimas | — |
| `tyrimo_rezultato_norma_nuo` | `number` | — | `4` | `open` | — | Tyrimo rezultato mažiausia normali reikšmė pagal metodą | — |
| `tyrimo_rezultato_norma_iki` | `number` | — | `4` | `open` | — | Tyrimo rezultato didžiausia normali reikšmė pagal metodą | — |
| `matavimo_vienetas` | `string` | — | `4` | `open` | — | Tyrimo rezultato matavimo vienetas | — |
| `paciento_diagnozes_tlk_10_am_kodas` | `string` | — | `4` | `open` | — | Paciento pagrindinės diagnozės TLK-10-AM kodas | — |
| `paciento_diagnoze` | `string` | — | `4` | `open` | — | Paciento pagrindinės diagnozės pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"V"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"M"` | `M` | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv
