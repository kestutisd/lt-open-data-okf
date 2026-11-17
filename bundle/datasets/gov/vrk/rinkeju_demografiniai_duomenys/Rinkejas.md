---
type: Table
title: "Rinkejas — Rinkėjai"
description: "Balso teisę turinčių rinkėjų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Rinkejas"
tags: [gov, vrk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rinkejas — Rinkėjai

Balso teisę turinčių rinkėjų lentelė. Vienas įrašas atitinka vieną rinkėją. Lentelė sudaryta iš rinkėjo pseudonimizuoto asmens kodo, lyties ir gimimo metų. Apie 12% rinkėjų gimimo metų įrašų yra modifikuoti pridedant atsitiktines vertes – triukšmą, siekiant užtikrinti konfidencialumą.

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/Rinkejas`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Rinkejas`
- **Primary Key (`ref`):** `rinkejo_asm_k`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rinkejo_asm_k` | `string` | — | `4` | `open` | — | Rinkėjo pseudonimizuotas asmens kodas | — |
| `rinkejo_lytis` | `string` | — | `4` | `open` | — | Rinkėjo lytis | — |
| `rinkejo_gim_m` | `date` | `Y` | `4` | `open` | — | Rinkėjo gimimo metai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinkejo_lytis` | `"V"` | — | — | Vyras | — |
| `rinkejo_lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv
