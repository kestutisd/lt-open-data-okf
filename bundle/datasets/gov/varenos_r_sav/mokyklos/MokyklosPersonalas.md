---
type: Table
title: "MokyklosPersonalas — Varėnos rajono savivaldybės mokyklų personalas"
description: "Rinkinyje pateikiamas Varėnos rajono savivaldybės mokyklos personalo sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/varenos_r_sav/mokyklos/MokyklosPersonalas"
tags: [gov, varenos_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/varenos_r_sav/mokyklu_personalas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# MokyklosPersonalas — Varėnos rajono savivaldybės mokyklų personalas

Rinkinyje pateikiamas Varėnos rajono savivaldybės mokyklos personalo sąrašas. Pateikiama tokia informacija kaip asmens lytis, užšifruotas asmens kodas, asmens amžius dešimtmečiais, pareigos, darbo laikotarpis ir ugdymo įstaiga.

Viena eilutė atitinka vieno asmens darbo laikotarpį tam tikrose pareigose, tam tikroje įstaigoje.

Duomenys pateikiami asmenų kurie įsidarbino nuo 1959 metų.

- **Model:** `datasets/gov/varenos_r_sav/mokyklos/MokyklosPersonalas`[^manifest]
- **Dataset:** [Varėnos rajono savivaldybės mokyklų informacija](../mokyklos.md) (`datasets/gov/varenos_r_sav/mokyklos`)
- **Manifest CSV:** [datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/varenos_r_sav/mokyklos/MokyklosPersonalas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikacinos numeris | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | Pateikiamas užšifruotas asmens kodas |
| `ak_validacija` | `string` | — | `4` | `open` | — | Asmens kodo validacija | Pateikiama ar asmens kodas tinkamas ar ne (vertinant pagal asmens kodo sudarymo taisykles) |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `gimimo_desimtmetis` | `date` | `Y` | `4` | `open` | — | Gimimo dešimtmetis | Asmenu gimimo dešimtmečio pirma diena |
| `pareigybe` | `string` | — | `4` | `open` | — | Pareigybė | — |
| `dirba_nuo` | `date` | `D` | `4` | `open` | — | Asmuo dirba nuo | — |
| `dirba_iki` | `date` | `D` | `4` | `open` | — | Asmuo dirba iki | — |
| `istaigos_id` | `string` | — | `4` | `open` | — | Įstaigos identifikacijos numeris | — |
| `institucija` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/varenos_r_sav/mokyklu_personalas.csv
