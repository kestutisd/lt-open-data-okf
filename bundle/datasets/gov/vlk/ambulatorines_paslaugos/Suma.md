---
type: Table
title: "Suma — Sumos, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų"
description: "Informacija apie sumas, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų (pagal gydymo įstaigų įvestus į IS „Sveidra“ duomenis)"
resource: "https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_paslaugos/Suma"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_paslaugos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suma — Sumos, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų

Informacija apie sumas, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų (pagal gydymo įstaigų įvestus į IS „Sveidra“ duomenis)

- **Model:** `datasets/gov/vlk/ambulatorines_paslaugos/Suma`[^manifest]
- **Dataset:** [datasets/gov/vlk/ambulatorines_paslaugos](../ambulatorines_paslaugos.md) (`datasets/gov/vlk/ambulatorines_paslaugos`)
- **Manifest CSV:** [datasets/gov/vlk/ambulatorines_paslaugos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_paslaugos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_paslaugos/Suma`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaiga` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri teikė paslaugas, ID |
| `pacientu_grupe` | `string` | — | `4` | `open` | — | Pacientų grupė | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `pas_kodas` | `ref` | [/datasets/gov/vlk/paslaugos/Paslauga[kodas]](../paslaugos/Paslauga.md) | `4` | `open` | — | Paslaugos kodas | Paslaugos kodas pagal Klasifikatorių |
| `balai` | `number` | `U` | `4` | `open` | — | Suma balais | — |
| `kontrastas_balais` | `number` | `U` | `4` | `open` | — | Suma balais už kontrastą | — |
| `eurai` | `number` | — | `2` | `open` | — | Suma eurais | — |
| `kontrastas_eurais` | `number` | — | `2` | `open` | — | Suma eurais už kontrastą | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pacientu_grupe` | `'LR'` | — | — | — | — |
| `pacientu_grupe` | `'EEE arba CH'` | — | — | — | — |
| `pacientu_grupe` | `'OVS'` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `2` | `open` | — | — | — |
| `eurai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `kontrastas_eurais` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_paslaugos.csv
