---
type: Table
title: "Paslauga"
description: "Spinta table datasets/gov/vlk/stacionarines_sutartys/Paslauga (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/stacionarines_sutartys/Paslauga"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/stacionarines_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_sutartys.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga

- **Model:** `datasets/gov/vlk/stacionarines_sutartys/Paslauga`[^manifest]
- **Dataset:** [datasets/gov/vlk/stacionarines_sutartys](../stacionarines_sutartys.md) (`datasets/gov/vlk/stacionarines_sutartys`)
- **Manifest CSV:** [datasets/gov/vlk/stacionarines_sutartys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/stacionarines_sutartys.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/stacionarines_sutartys/Paslauga`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pagrindines_kodas` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga[pagrindines_kodas]](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos (pagrindinės) ID | Pagrindinės įstaigos, kuri sudarė sutartį ID |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos dėl kurios sudaryta sutartis pavadinimas | Paslaugos dėl kurios sudaryta sutartis pavadinimas |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | Sutartis galioja nuo |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | Sutartis galioja iki |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/stacionarines_sutartys.csv
