---
type: Table
title: "Suma — Sumos, už kurias gydymo įstaigos suteikė stacionarinių aktyviojo gydymo ir dienos chirurgijos paslaugų"
description: "Informacija apie sumas, už kurias gydymo įstaigos suteikė stacionarinių aktyviojo gydymo ir dienos chirurgijos paslaugų (pagal gydymo įstaigų įvestus į IS „Sveidra“ duomenis)"
resource: "https://get.data.gov.lt/datasets/gov/vlk/aktyvus_gydymas/Suma"
tags: [gov, vlk, suma, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/aktyvus_gydymas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/aktyvus_gydymas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1534/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/aktyvus_gydymas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Suma — Sumos, už kurias gydymo įstaigos suteikė stacionarinių aktyviojo gydymo ir dienos chirurgijos paslaugų

Informacija apie sumas, už kurias gydymo įstaigos suteikė stacionarinių aktyviojo gydymo ir dienos chirurgijos paslaugų (pagal gydymo įstaigų įvestus į IS „Sveidra“ duomenis)[^manifest]

- **Model:** `datasets/gov/vlk/aktyvus_gydymas/Suma`[^manifest]
- **Dataset:** [Sumos, už kurias gydymo įstaigos suteikė stacionarinių aktyviojo gydymo ir dienos chirurgijos...](../aktyvus_gydymas.md) (`datasets/gov/vlk/aktyvus_gydymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/aktyvus_gydymas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/aktyvus_gydymas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/aktyvus_gydymas/Suma` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri teikė paslaugas, ID |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Finansinio laikotarpio metai |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | Finansinio laikotarpio mėnuo |
| `pacientu_grupe` | `string` | — | `4` | `open` | — | Pacientų grupė | — |
| `drg_kodas` | `string` | — | `4` | `open` | — | DRG kodas | Giminingų diagnozių grupės kodas |
| `balai` | `number` | `U` | `4` | `open` | — | DRG kaina balais | — |
| `eurai` | `number` | — | `2` | `open` | — | DRG kaina eurais | — |
| `dchir` | `string` | — | `4` | `open` | — | Dienos chirurgija | Požymis, nurodantis, ar tai dienos chirurgijos paslauga |
| `dchir_gr` | `integer` | — | `3` | `open` | — | Dienos chirurgijos paslaugų grupė | Požymis, nurodantis dienos chirurgijos paslaugų grupę |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pacientu_grupe` | `'LR'` | — | — | — | — |
| `pacientu_grupe` | `'EEE arba CH'` | — | — | — | — |
| `pacientu_grupe` | `'OVS'` | — | — | — | — |
| `dchir` | `"Ne"` | — | — | — | — |
| `dchir` | `"Taip"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `2` | `open` | — | — | — |
| `menuo` | `update(type: "date", ref: "M")` | `type` | `2` | `open` | — | — | — |
| `eurai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/aktyvus_gydymas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/aktyvus_gydymas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/aktyvus_gydymas (https://data.gov.lt/datasets/1534/)
