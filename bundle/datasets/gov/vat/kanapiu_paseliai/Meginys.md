---
type: Table
title: "Meginys"
description: "Informacija apie pluoštinių kanapių pasėlių plotus pagal veisles, paimtus pluoštinių kanapių mėginius ir nustatytus THC kiekius pluoštinių kanapių veislėse"
resource: "https://get.data.gov.lt/datasets/gov/vat/kanapiu_paseliai/Meginys"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r31_pluostines_kanapes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r31_pluostines_kanapes.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Meginys

Informacija apie pluoštinių kanapių pasėlių plotus pagal veisles, paimtus pluoštinių kanapių mėginius ir nustatytus THC kiekius pluoštinių kanapių veislėse

- **Model:** `datasets/gov/vat/kanapiu_paseliai/Meginys`[^manifest]
- **Dataset:** [datasets/gov/vat/kanapiu_paseliai](../kanapiu_paseliai.md) (`datasets/gov/vat/kanapiu_paseliai`)
- **Manifest CSV:** [datasets/gov/vat/r31_pluostines_kanapes.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r31_pluostines_kanapes.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/kanapiu_paseliai/Meginys`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | `Identifikacinis numeris` | — | — |
| `registracija` | `integer` | — | `4` | `open` | `Registracijos metai` | — | — |
| `veisle` | `string` | — | `4` | `open` | `Kanapių veislė` | — | — |
| `plotas` | `number` | `ha` | `4` | `open` | `Bendras plotas` | — | — |
| `lauku_irasai` | `number` | `U` | `4` | `open` | `Laukų įrašų kiekis` | — | — |
| `tyrimai` | `number` | `U` | `4` | `open` | `Atliktų tyrimų skaičius` | — | — |
| `thc_suma` | `integer` | — | `4` | `open` | `Suma Thc` | — | — |
| `virsija_thc` | `number` | `U` | `4` | `open` | `Mėginių skaičius, viršijantis Thc` | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `registracija` | `update(type: "registracija", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r31_pluostines_kanapes.csv
