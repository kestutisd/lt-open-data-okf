---
type: Table
title: "Paslauga — Akredituotų institucijų teikiamos paslaugos, jų grupės ir rūšys"
description: "Spinta table datasets/gov/sadm/akredituotos_institucijos/Paslauga (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos/Paslauga"
tags: [gov, sadm, paslauga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L58"
    title: "atviriduomenys/manifest — datasets/gov/sadm/akredituotos_institucijos.csv#L58"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4118/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/akredituotos_institucijos"
    author: "team:vda"
    last_modified: "2026-10-22T00:00:00Z"
---

# Paslauga — Akredituotų institucijų teikiamos paslaugos, jų grupės ir rūšys

- **Model:** `datasets/gov/sadm/akredituotos_institucijos/Paslauga`[^manifest]
- **Dataset:** [Prašymai teikti akredituotas socialines paslaugas](../akredituotos_institucijos.md) (`datasets/gov/sadm/akredituotos_institucijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/akredituotos_institucijos.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L58)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos/Paslauga` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `paslaugos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-22`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_id` | `string` | — | `4` | `open` | — | Įrašo ID | — |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo ID | — |
| `paslaugu_tipas` | `string` | — | `4` | `open` | — | Paslaugos tipas | — |
| `paslaugu_grupe` | `string` | — | `4` | `open` | — | Paslaugų grupė | — |
| `paslaugu_rusis` | `string` | — | `4` | `open` | — | Paslaugų rūšis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/akredituotos_institucijos.csv#L58 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L58)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/akredituotos_institucijos (https://data.gov.lt/datasets/4118/)
