---
type: Table
title: "AsmenuNeigalumas — Asmenų neįgalumo lygis"
description: "Spinta table datasets/gov/ndnt/neigalumo_lygis/AsmenuNeigalumas (9 columns)."
tags: [gov, ndnt, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ndnt/neigalumo_lygis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/neigalumo_lygis.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# AsmenuNeigalumas — Asmenų neįgalumo lygis

- **Model:** `datasets/gov/ndnt/neigalumo_lygis/AsmenuNeigalumas`[^manifest]
- **Dataset:** [Asmenų neįgalumo lygio duomenys](../neigalumo_lygis.md) (`datasets/gov/ndnt/neigalumo_lygis`)
- **Manifest CSV:** [datasets/gov/ndnt/neigalumo_lygis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/neigalumo_lygis.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `gimimo_metai, tlk10am`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nl_lygis` | `string` | — | `4` | `open` | — | Neįgalumo lygis | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `3` | `open` | — | Savivaldybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gimimo_metai` | `date` | `D` | `4` | `open` | — | Gimimo metai | — |
| `galiojimo_data_nuo` | `date` | `D` | `4` | `open` | — | Galiojimo data nuo | — |
| `galiojimo_data_iki` | `date` | `D` | `4` | `open` | — | Galiojimo data iki | — |
| `terminas` | `string` | — | `3` | `open` | — | Terminas | — |
| `tlk10am` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../vlk/tlk10am/Tlk10am.md) | `3` | `open` | — | Ligos kodas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nl_lygis` | `"vidutinis"` | — | — | — | — |
| `nl_lygis` | `"lengvas"` | — | — | — | — |
| `nl_lygis` | `"sunkus"` | — | — | — | — |
| `lytis` | `"v"` | — | — | Vyras | — |
| `lytis` | `"m"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ndnt/neigalumo_lygis.csv
