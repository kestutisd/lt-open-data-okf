---
type: Table
title: "Tyrimas — Laboratorinių tyrimų duomenys"
description: "Mykolo Marcinkevičiaus ligoninės sLIS sistema kaupia duomenis apie Mykolo Marcinkevičiaus ligoinėje įvykdytus laboratorinius tyrimus pacientams."
resource: "https://get.data.gov.lt/datasets/gov/mml/slis/Tyrimas"
tags: [gov, mml, tyrimas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mml/slis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/mml/slis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tyrimas — Laboratorinių tyrimų duomenys

Mykolo Marcinkevičiaus ligoninės sLIS sistema kaupia duomenis apie Mykolo Marcinkevičiaus ligoinėje įvykdytus laboratorinius tyrimus pacientams. Duomenys kaupiami nuo 2021 m. ir atnaujinami iki šiol. Duomenų rinkinyje kaupiami duomenys apima paciento identifikatorių, gimimo metus, lytį, tyrimo identifikatorių, pavadinimą bei validacijos datą, tyrimo analičių identifikatorius, pavadinimus, originalų rezultatų stulpelį su dviem papildomais, į kuriuos atitinkamai išskirstyti tyrimų semantiniai vertinimai ir skaitiniai rezultatai, rezultatų normų rėžius ir matavimo vienetus. Tyrimo analitė - tai vienas iš matuojamų sudedamųjų veiksnių atliekamam laboratoriniui tyrimui.[^manifest]

- **Model:** `datasets/gov/mml/slis/Tyrimas`[^manifest]
- **Dataset:** [Laboratorinių tyrimų duomenys](../slis.md) (`datasets/gov/mml/slis`)[^manifest]
- **Manifest CSV:** [datasets/gov/mml/slis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mml/slis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/mml/slis/Tyrimas` (`deployed`)[^manifest]
- **Provider:** `mml` — Mykolo Marcinkevičiaus ligoninė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo data metų tikslumu | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyrimo_id` | `string` | — | `4` | `open` | — | Tyrimo identifikatorius | — |
| `tyrimo_pav` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `tyrimo_val_data` | `datetime` | `S` | `4` | `open` | — | Tyrimo validacijos data ir laikas sekundžių tikslumu | — |
| `tyrimo_analites_id` | `string` | — | `4` | `open` | — | Tyrimo analitės identifikatorius | — |
| `tyrimo_analites_pav` | `string` | — | `4` | `open` | — | Tyrimo analitės pavadinimas | — |
| `tyrimo_analites_rez_orig` | `string` | — | `4` | `open` | — | Tyrimo analitės rezultatų originalus stulpelis | — |
| `tyrimo_analites_tekst_rez_parsed` | `string` | — | `4` | `open` | — | Tyrimo analitės išskirti semantiniai vertinimai | — |
| `tyrimo_analites_skait_rez_parsed` | `number` | — | `4` | `open` | — | Tyrimo analitės išskirti skaitiniai rezultatai | — |
| `tyrimo_analites_norma_nuo` | `number` | — | `4` | `open` | — | Tyrimo analinės rezultato mažiausia normali reikšmė | — |
| `tyrimo_analites_norma_iki` | `number` | — | `4` | `open` | — | Tyrimo analinės rezultato didžiausia normali reikšmė | — |
| `tyrimo_analites_vnt` | `string` | — | `4` | `open` | — | Tyrimo analitės rezultato matavimo vienetas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `lytis` | `"Nežinoma"` | `N` | — | Nežinoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/mml/slis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mml/slis.csv#L6)
