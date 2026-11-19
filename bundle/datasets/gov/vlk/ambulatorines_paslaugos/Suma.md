---
type: Table
title: "Suma — Sumos, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų"
description: "Informacija apie sumas, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų (pagal gydymo įstaigų įvestus į IS „Sveidra“ duomenis)"
resource: "https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_paslaugos/Suma"
tags: [gov, vlk, suma, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_paslaugos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_paslaugos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1533/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/ambulatorines_paslaugos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Suma — Sumos, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų

Informacija apie sumas, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų (pagal gydymo įstaigų įvestus į IS „Sveidra“ duomenis)[^manifest]

- **Model:** `datasets/gov/vlk/ambulatorines_paslaugos/Suma`[^manifest]
- **Dataset:** [Sumos, už kurias gydymo įstaigos suteikė ambulatorinių paslaugų](../ambulatorines_paslaugos.md) (`datasets/gov/vlk/ambulatorines_paslaugos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/ambulatorines_paslaugos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_paslaugos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_paslaugos/Suma` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri teikė paslaugas, ID |
| `pacientu_grupe` | `string` | — | `4` | `open` | — | Pacientų grupė | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `pas_kodas` | `ref` | [Paslauga](../paslaugos/Paslauga.md) (`level=4 UUID` via `Paslauga[kodas]`: `pas_kodas._id`) | `4` | `open` | — | Paslaugos kodas | Paslaugos kodas pagal Klasifikatorių |
| `balai` | `number` | `U` | `4` | `open` | — | Suma balais | — |
| `kontrastas_balais` | `number` | `U` | `4` | `open` | — | Suma balais už kontrastą | — |
| `eurai` | `number` | — | `2` | `open` | — | Suma eurais | — |
| `kontrastas_eurais` | `number` | — | `2` | `open` | — | Suma eurais už kontrastą | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_paslaugos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_paslaugos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/ambulatorines_paslaugos (https://data.gov.lt/datasets/1533/)
