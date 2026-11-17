---
type: Table
title: "ApgyvendinimoEile — Asmenų apgyvendinimo globos namuose eilių duomenys"
description: "Lentelėje pateikti asmenų apgyvendinimo globos namuose 2022 ir 2023 metų eilių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ndnt/eiles/ApgyvendinimoEile"
tags: [gov, ndnt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ndnt/eiles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/eiles.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApgyvendinimoEile — Asmenų apgyvendinimo globos namuose eilių duomenys

Lentelėje pateikti asmenų apgyvendinimo globos namuose 2022 ir 2023 metų eilių duomenys. Duomenų teikėjas – Asmens su negalia teisių apsaugos agentūra prie LR socialinės apsaugos ir darbo ministerijos.

- **Model:** `datasets/gov/ndnt/eiles/ApgyvendinimoEile`[^manifest]
- **Dataset:** [Asmenų apgyvendinimo globos namuose eilių duomenys](../eiles.md) (`datasets/gov/ndnt/eiles`)
- **Manifest CSV:** [datasets/gov/ndnt/eiles.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/eiles.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ndnt/eiles/ApgyvendinimoEile`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `eiles_nr` | `integer` | — | `4` | `open` | — | Eilės numeris asmens apgyvendinimui globos namuose | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Asmens vardas ir pavardė | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `sprendimo_data` | `date` | `D` | `4` | `open` | — | Sprendimo dėl asmens apgyvendinimo globos namuose priėmimo data | — |
| `sprendimo_nr` | `string` | — | `4` | `open` | — | Sprendimo dėl asmens apgyvendinimo globos namuose numeris | — |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Sprendimo registravimo data | — |
| `registravimo_nr` | `string` | — | `4` | `open` | — | Sprendimo registravimo numeris | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės, kuri siunčia asmenį į globos namus, pavadinimas | — |
| `siuntimo_men` | `date` | `M` | `4` | `open` | — | Siuntimo į globos namus metai ir mėnesis | — |
| `siuntimo_nr` | `number` | — | `4` | `open` | — | Siuntimo į globos namus numeris | — |
| `apgyvendinimo_men` | `date` | `M` | `4` | `open` | — | Asmens apgyvendinimo globos namuose metai ir mėnesis | — |
| `apgyvendinimo_institucija` | `string` | — | `4` | `open` | — | Globos namų pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ndnt/eiles.csv
