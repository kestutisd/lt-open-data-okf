---
type: Table
title: "MykoloMarcinkeviciausLigonine — Mykolo Marcinkevičiaus ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Mykolo Marcinkevičiaus ligoninės sLIS sistema kaupia duomenis apie Mykolo Marcinkevičiaus ligoinėje įvykdytus laboratorinius tyrimus pacientams."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/MykoloMarcinkeviciausLigonine"
tags: [gov, lab_tyrimai, mykolomarcinkeviciausligonine, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L44"
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L44"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2700/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-23T00:00:00Z"
---

# MykoloMarcinkeviciausLigonine — Mykolo Marcinkevičiaus ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai

Mykolo Marcinkevičiaus ligoninės sLIS sistema kaupia duomenis apie Mykolo Marcinkevičiaus ligoinėje įvykdytus laboratorinius tyrimus pacientams. Duomenys kaupiami nuo 2021 m. ir atnaujinami iki šiol. Duomenų rinkinyje kaupiami duomenys apima paciento identifikatorių, gimimo metus, lytį, tyrimo identifikatorių, pavadinimą bei validacijos datą, tyrimo analičių identifikatorius, pavadinimus, originalų rezultatų stulpelį su dviem papildomais, į kuriuos atitinkamai išskirstyti tyrimų semantiniai vertinimai ir skaitiniai rezultatai, rezultatų normų rėžius ir matavimo vienetus. Tyrimo analitė - tai vienas iš matuojamų sudedamųjų veiksnių atliekamam laboratoriniui tyrimui.[^manifest]

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/MykoloMarcinkeviciausLigonine`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L44)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/MykoloMarcinkeviciausLigonine` (`deployed`)[^manifest]
- **Provider:** `lab_tyrimai`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-23`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo data metų tikslumu | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyrimo_id` | `string` | — | `4` | `open` | — | Tyrimo identifikatorius | — |
| `tyrimo_pav` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `tyrimo_val_data` | `date` | `W` | `4` | `open` | — | Tyrimo validacijos data savaitės tikslumu | — |
| `tyrimo_analites_id` | `string` | — | `4` | `open` | — | Tyrimo analitės identifikatorius | — |
| `tyrimo_analites_pav` | `string` | — | `4` | `open` | — | Tyrimo analitės pavadinimas | — |
| `tyrimo_analites_rez_orig` | `string` | — | `1` | `open` | — | Tyrimo analitės rezultatų originalus stulpelis | — |
| `tyrimo_analites_tekst_rez_parsed` | `string` | — | `4` | `open` | — | Tyrimo analitės išskirti semantiniai vertinimai | — |
| `tyrimo_analites_skait_rez_parsed` | `number` | — | `4` | `open` | — | Tyrimo analitės išskirti skaitiniai rezultatai | — |
| `tyrimo_analites_norma_nuo` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato mažiausia normali reikšmė | — |
| `tyrimo_analites_norma_iki` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato didžiausia normali reikšmė | — |
| `tyrimo_analites_vnt` | `string` | — | `4` | `open` | — | Tyrimo analitės rezultato matavimo vienetas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `lytis` | `"Nežinoma"` | `N` | — | Nežinoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L44 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L44)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai (https://data.gov.lt/datasets/2700/)
