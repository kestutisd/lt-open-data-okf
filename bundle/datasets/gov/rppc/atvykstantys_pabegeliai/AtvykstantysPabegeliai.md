---
type: Table
title: "AtvykstantysPabegeliai — Į Pabėgėlių priėmimo centrą atvykstantys asmenys."
description: "Į Pabėgėlių priėmimo centrą atvykstančių asmenų išsami informacija."
resource: "https://get.data.gov.lt/datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai"
tags: [gov, rppc, atvykstantyspabegeliai, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2566/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rppc/atvykstantys_pabegeliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AtvykstantysPabegeliai — Į Pabėgėlių priėmimo centrą atvykstantys asmenys.

**Dataset Context:** Į Pabėgėlių priėmimo centrą atvykstančių asmenų išsami informacija.[^manifest]

- **Model:** `datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai`[^manifest]
- **Dataset:** [Į Pabėgėlių priėmimo centrą atvykstantys asmenys.](../atvykstantys_pabegeliai.md) (`datasets/gov/rppc/atvykstantys_pabegeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rppc/atvykstantys_pabegeliai/AtvykstantysPabegeliai` (`deployed`)[^manifest]
- **Provider:** `rppc` — Pabėgėlių priėmimo centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `profesinis_laipsnis` | `"bakalauras"` | — | — | Bakalauras | — |
| `profesinis_laipsnis` | `"magistras"` | — | — | Magistras | — |
| `profesinis_laipsnis` | `"nėra"` | — | — | nėra | — |
| `profesinis_laipsnis` | `"daktaras"` | — | — | Daktaras | — |
| `profesinis_laipsnis` | `"habilituotas daktaras"` | — | — | Habilituotas daktaras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rppc/atvykstantys_pabegeliai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rppc/atvykstantys_pabegeliai (https://data.gov.lt/datasets/2566/)
