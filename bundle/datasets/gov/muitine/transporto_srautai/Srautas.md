---
type: Table
title: "Srautas — Transporto priemonių judėjimo pro muitinės postus srautas"
description: "Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai/Srautas"
tags: [gov, muitine, srautas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/transporto_srautai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2842/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/transporto_srautai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Srautas — Transporto priemonių judėjimo pro muitinės postus srautas

Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus[^manifest]

- **Model:** `datasets/gov/muitine/transporto_srautai/Srautas`[^manifest]
- **Dataset:** [Transporto priemonių judėjimo pro muitinės postus srautas](../transporto_srautai.md) (`datasets/gov/muitine/transporto_srautai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/transporto_srautai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai/Srautas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `judejimo_kryptis` | — | `"in"` | — | — | — |
| `judejimo_kryptis` | — | `"out"` | — | — | — |
| `kameros_tipas` | — | `"stacionarus"` | — | — | — |
| `kameros_tipas` | — | `"mobilus"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/transporto_srautai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/transporto_srautai (https://data.gov.lt/datasets/2842/)
