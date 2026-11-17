---
type: Table
title: "KedainiuPSPC — Kėdainių pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys"
description: "Kėdainių pirminės sveikatos priežiūros centro OpenLIMS sistemoje nuo 2021 m. kaupiami ir iki šiol atnaujinami pacientams atliktų laboratorinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/KedainiuPSPC"
tags: [gov, lab_tyrimai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L145"
    last_modified: "2026-11-11T14:39:20Z"
---

# KedainiuPSPC — Kėdainių pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys

Kėdainių pirminės sveikatos priežiūros centro OpenLIMS sistemoje nuo 2021 m. kaupiami ir iki šiol atnaujinami pacientams atliktų laboratorinių tyrimų duomenys. Duomenų rinkinį sudaro: įstaigos pavadinimas, paciento šifruotas identifikatorius, lytis, gimimo metai, tyrimo data dienos tikslumu, rezultato interpretacijos stulpelis, tiek su skaitiniais rezultatais, tiek su semantiniais vertinimais, atskiras, 5 skaitmenų tikslumu suapvalintas skaitinių rezultatų stulpelis, tyrimo metodo pavadinimas, rezultato reikšmių normų rėžiai, suapvalinti 5 skaitmenų tikslumu, rezultato matavimo vienetai bei paciento pagrindinės diagnozės TLK-10-AM kodas ir pavadinimas. Vienas įrašas atitinka vienam pacientui atliktą vieną tyrimą.

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/KedainiuPSPC`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L145](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L145)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/KedainiuPSPC`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `istaigos_pav` | `string` | — | `4` | `open` | — | Tyrimą atlikusios įstaigos pavadinimas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento šifruotas identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_data` | `date` | `D` | `4` | `open` | — | Tyrimo data dienos tikslumu | — |
| `tyrimo_rezultato_interpretacija` | `string` | — | `4` | `open` | — | Tyrimo rezultatų semantiniai vertinimai ir skaitiniai rezultatai | — |
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
| `paciento_lytis` | `"Vyras"` | — | — | Vyras | — |
| `paciento_lytis` | `"Moteris"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv
