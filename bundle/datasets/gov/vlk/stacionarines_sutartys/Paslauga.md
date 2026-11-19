---
type: Table
title: "Paslauga"
description: "Spinta table datasets/gov/vlk/stacionarines_sutartys/Paslauga (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/stacionarines_sutartys/Paslauga"
tags: [gov, vlk, paslauga, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_sutartys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vlk/stacionarines_sutartys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1587/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/stacionarines_sutartys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Paslauga

- **Model:** `datasets/gov/vlk/stacionarines_sutartys/Paslauga`[^manifest]
- **Dataset:** [Numatomų teikti stacionarinių ir dienos chirurgijos asmens sveikatos priežiūros paslaugų...](../stacionarines_sutartys.md) (`datasets/gov/vlk/stacionarines_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/stacionarines_sutartys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_sutartys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/stacionarines_sutartys/Paslauga` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pagrindines_kodas` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID` via `Istaiga[pagrindines_kodas]`: `pagrindines_kodas._id`) | `4` | `open` | — | Įstaigos (pagrindinės) ID | Pagrindinės įstaigos, kuri sudarė sutartį ID |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos dėl kurios sudaryta sutartis pavadinimas | Paslaugos dėl kurios sudaryta sutartis pavadinimas |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | Sutartis galioja nuo |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | Sutartis galioja iki |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/stacionarines_sutartys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_sutartys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/stacionarines_sutartys (https://data.gov.lt/datasets/1587/)
