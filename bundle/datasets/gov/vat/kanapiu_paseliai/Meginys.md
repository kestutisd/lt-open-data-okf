---
type: Table
title: "Meginys"
description: "Informacija apie pluoštinių kanapių pasėlių plotus pagal veisles, paimtus pluoštinių kanapių mėginius ir nustatytus THC kiekius pluoštinių kanapių veislėse"
resource: "https://get.data.gov.lt/datasets/gov/vat/kanapiu_paseliai/Meginys"
tags: [gov, vat, meginys, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r31_pluostines_kanapes.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r31_pluostines_kanapes.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1887/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/kanapiu_paseliai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Meginys

Informacija apie pluoštinių kanapių pasėlių plotus pagal veisles, paimtus pluoštinių kanapių mėginius ir nustatytus THC kiekius pluoštinių kanapių veislėse[^manifest]

- **Model:** `datasets/gov/vat/kanapiu_paseliai/Meginys`[^manifest]
- **Dataset:** [Informacija apie pluoštinių kanapių pasėlių plotus pagal veisles, paimtus pluoštinių kanapių...](../kanapiu_paseliai.md) (`datasets/gov/vat/kanapiu_paseliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r31_pluostines_kanapes.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r31_pluostines_kanapes.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/kanapiu_paseliai/Meginys` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `registracija` | `update(type: "registracija", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r31_pluostines_kanapes.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r31_pluostines_kanapes.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/kanapiu_paseliai (https://data.gov.lt/datasets/1887/)
