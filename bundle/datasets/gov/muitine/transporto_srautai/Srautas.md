---
type: Table
title: "Srautas — Transporto priemonių judėjimo pro muitinės postus srautas"
description: "Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai/Srautas"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/transporto_srautai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Srautas — Transporto priemonių judėjimo pro muitinės postus srautas

Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus

- **Model:** `datasets/gov/muitine/transporto_srautai/Srautas`[^manifest]
- **Dataset:** [Transporto priemonių judėjimo pro muitinės postus srautas](../transporto_srautai.md) (`datasets/gov/muitine/transporto_srautai`)
- **Manifest CSV:** [datasets/gov/muitine/transporto_srautai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai/Srautas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA sukurtas unikalus identifikatorius | — |
| `ataskaitine_para` | `date` | `D` | `4` | `open` | — | Ataskaitinė para | — |
| `judejimo_kryptis` | `string` | — | `4` | `open` | — | Transporto priemonės ar konteinerio judėjimo kryptis | — |
| `kameros_pavadinimas` | `string` | — | `4` | `open` | — | Kameros pavadinimas | — |
| `kameros_aprasymas` | `string` | — | `4` | `open` | — | Kameros aprašymas | — |
| `kameros_tipas` | `string` | — | `4` | `open` | — | Kameros tipas | — |
| `muitines_kodas` | `string` | — | `4` | `open` | — | Muitinės posto kodas | — |
| `tp_srautas` | `integer` | — | `4` | `open` | — | Transporto priemonių srautas | — |
| `muitines_posto_platumos_koordinate` | `number` | — | `4` | `open` | — | Muitinės posto platumos koordinatė | — |
| `muitines_posto_ilgumos_koordinate` | `number` | — | `4` | `open` | — | Muitinės posto ilgumos koordinatė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `judejimo_kryptis` | — | `"in"` | — | — | — |
| `judejimo_kryptis` | — | `"out"` | — | — | — |
| `kameros_tipas` | — | `"stacionarus"` | — | — | — |
| `kameros_tipas` | — | `"mobilus"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/transporto_srautai.csv
