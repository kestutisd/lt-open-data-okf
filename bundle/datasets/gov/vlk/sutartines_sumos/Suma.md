---
type: Table
title: "Suma — Asmens sveikatos priežiūros įstaigų pasirašytos sutartinės sumos dėl asmens sveikatos priežiūros paslaugų"
description: "Informacija apie asmens sveikatos priežiūros įstaigų ir teritorinių ligonių kasų pasirašytas sutartines sumas dėl asmens sveikatos priežiūros paslaugų teikimo ir jų apmokėjimo Privalomojo sveikatos draudimo fondo biudžeto lėšomis"
resource: "https://get.data.gov.lt/datasets/gov/vlk/sutartines_sumos/Suma"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/sutartines_sumos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/sutartines_sumos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suma — Asmens sveikatos priežiūros įstaigų pasirašytos sutartinės sumos dėl asmens sveikatos priežiūros paslaugų

Informacija apie asmens sveikatos priežiūros įstaigų ir teritorinių ligonių kasų pasirašytas sutartines sumas dėl asmens sveikatos priežiūros paslaugų teikimo ir jų apmokėjimo Privalomojo sveikatos draudimo fondo biudžeto lėšomis

- **Model:** `datasets/gov/vlk/sutartines_sumos/Suma`[^manifest]
- **Dataset:** [datasets/gov/vlk/sutartines_sumos](../sutartines_sumos.md) (`datasets/gov/vlk/sutartines_sumos`)
- **Manifest CSV:** [datasets/gov/vlk/sutartines_sumos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/sutartines_sumos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/sutartines_sumos/Suma`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `istg_jar` | `integer` | — | `2` | `open` | — | Įstaigos JA kodas | — |
| `istg_id` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | — |
| `sut_suma` | `number` | — | `2` | `open` | — | ASPĮ numatyta sutartinė suma | ASPĮ numatyta sutartinė suma Privalomojo sveikatos draudimo fondo biudžeto lėšomis apmokamoms paslaugoms, įskaitant preliminarias sutartines sumas, (01, 03, 05 išlaidų straipsniai) |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `istg_jar` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `sut_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/sutartines_sumos.csv
