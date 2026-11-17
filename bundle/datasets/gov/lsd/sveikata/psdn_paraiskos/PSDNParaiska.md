---
type: Table
title: "PSDNParaiska — Pakartotinio sveikatos duomenų naudojimo paraiškos"
description: "Spinta table datasets/gov/lsd/sveikata/psdn_paraiskos/PSDNParaiska (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/psdn_paraiskos/PSDNParaiska"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/psdn_paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PSDNParaiska — Pakartotinio sveikatos duomenų naudojimo paraiškos

- **Model:** `datasets/gov/lsd/sveikata/psdn_paraiskos/PSDNParaiska`[^manifest]
- **Dataset:** [PSDN paraiškos](../psdn_paraiskos.md) (`datasets/gov/lsd/sveikata/psdn_paraiskos`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/psdn_paraiskos/PSDNParaiska`
- **Primary Key (`ref`):** `vda_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | VDA suteiktas unikalus paraiškos numeris | — |
| `subjektai` | `string` | — | `4` | `open` | — | Paraiškoje nagrinėjami subjektai | — |
| `duomenys` | `string` | — | `4` | `open` | — | Paraiškai pateiktų duomenų kategorijos | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės JAR kodas | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `paskutine_pildymo_data` | `date` | — | `4` | `open` | — | Paskutinė paraiškos pildymo data | — |
| `leidimo_data` | `date` | — | `4` | `open` | — | Paraiškai išduoto leidimo data | — |
| `duomenys_pateikti` | `date` | — | `4` | `open` | — | Pareiškėjams pateiktų duomenų data | — |
| `tikslas` | `string` | — | `4` | `open` | — | Paraiškos tikslas | — |
| `trukme` | `date` | — | `4` | `open` | — | Paraiškėjams suteiktos prieigos prie duomenų trukmė | — |
| `galiojimas` | `string` | — | `4` | `open` | — | Paraiškos galiojimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tikslas` | `"Moksliniai tyrimai ir eksperimentinė plėtra"` | — | — | Moksliniai tyrimai ir eksperimentinė plėtra | — |
| `tikslas` | `"Žinių vadyba sveikatos srityje"` | — | — | Žinių vadyba sveikatos srityje | — |
| `tikslas` | `"Inovacijos"` | — | — | Inovacijos | — |
| `tikslas` | `"Statistikos tvarkymas"` | — | — | Statistikos tvarkymas | — |
| `galiojimas` | `"Galioja"` | — | `open` | Leidimas galioja | — |
| `galiojimas` | `"Baigė galioti"` | — | — | Leidimas baigė galioti | — |
| `galiojimas` | `"Sustabdytas"` | — | — | Duomenų teikimas sustabdytas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/psdn_paraiskos.csv
