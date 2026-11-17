---
type: Table
title: "AtvykstantysPabegeliai — Į Pabėgėlių priėmimo centrą atvykstantys asmenys."
description: "Spinta table datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai"
tags: [gov, rppc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rppc/atvykstantys_pabegeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AtvykstantysPabegeliai — Į Pabėgėlių priėmimo centrą atvykstantys asmenys.

- **Model:** `datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai`[^manifest]
- **Dataset:** [Į Pabėgėlių priėmimo centrą atvykstantys asmenys.](../atvykstantys_pabegeliai.md) (`datasets/gov/rppc/atvykstantys_pabegeliai`)
- **Manifest CSV:** [datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Pabėgėlis, asmuo atvykęs į pabėgėlių priėmimo centrą. Asmuo gali pakartotinai atvykti(asmuo gali kartotis) | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai sistemoje | — |
| `lytis` | `string` | — | `4` | `open` | — | Pabėgėlio lytis sistemoje | — |
| `programos_tipas` | `string` | — | `4` | `open` | — | PPC programos tipas (institucijos vidinis klasifikatorius) | — |
| `pilietybe` | `string` | — | `4` | `open` | — | Pabėgėlio nurodyta pilietybė. Jei asmenų su pilietybe yra mažiau nei 2, tokiems priskiriama "Kita" | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Išsilavinimas, kurį nurodė asmuo | — |
| `profesija` | `string` | — | `4` | `open` | — | Profesija, kurią nurodė asmuo | — |
| `profesinis_laipsnis` | `string` | — | `4` | `open` | — | Profesinis laipsnis, kurį nurodė asmuo | — |
| `ppc_atvykimo_data` | `date` | `D` | `4` | `open` | — | Atvykimo į PPC data | — |
| `ppc_isvykimo_data` | `date` | `D` | `4` | `open` | — | Išvykimo iš PPC data(išvyko į integraciją, mirė, išvyko į užsienį)) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `profesinis_laipsnis` | `"bakalauras"` | — | — | Bakalauras | — |
| `profesinis_laipsnis` | `"magistras"` | — | — | Magistras | — |
| `profesinis_laipsnis` | `"nėra"` | — | — | nėra | — |
| `profesinis_laipsnis` | `"daktaras"` | — | — | Daktaras | — |
| `profesinis_laipsnis` | `"habilituotas daktaras"` | — | — | Habilituotas daktaras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rppc/atvykstantys_pabegeliai.csv
