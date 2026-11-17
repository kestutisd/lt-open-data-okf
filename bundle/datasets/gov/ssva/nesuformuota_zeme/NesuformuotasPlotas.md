---
type: Table
title: "NesuformuotasPlotas — Nesuformuoti žemės plotai"
description: "Duomenų rinkinys apima informaciją apie valstybės valdomus, bet dar nesuformuotus žemės plotus."
resource: "https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme/NesuformuotasPlotas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# NesuformuotasPlotas — Nesuformuoti žemės plotai

Duomenų rinkinys apima informaciją apie valstybės valdomus, bet dar nesuformuotus žemės plotus. Kiekvienam sklypui pateikiamas unikalus identifikatorius, jį administruojanti institucija (dažniausiai Nacionalinė žemės tarnyba), buvimo vietos koordinatės (taškinė ir poligoninė geometrija), nesuformuotos žemės perimetras bei plotas. Duomenys taip pat apima savivaldybės ir gyvenvietės kodus, o geografinė informacija pateikta keliuose koordinacinių sistemų formatuose (LKS94, WGS84, GeoJSON, WKT).

- **Model:** `datasets/gov/ssva/nesuformuota_zeme/NesuformuotasPlotas`[^manifest]
- **Dataset:** [Nesuformuoti žemės plotai](../nesuformuota_zeme.md) (`datasets/gov/ssva/nesuformuota_zeme`)
- **Manifest CSV:** [datasets/gov/ssva/nesuformuota_zeme.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme/NesuformuotasPlotas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus nesuformuotos žemės identifikatorius | — |
| `patiketinis` | `string` | — | `4` | `open` | — | Patikėtinio tipas: N - NŽT, S - savivaldybė | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Patikėtinio pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Patiketinio JAR kodas | — |
| `gyv_kodas` | `string` | — | `4` | `open` | — | Gyvenvietės kodas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `perimetras_m` | `number` | — | `4` | `open` | — | Nesuformuoto ploto perimetras metrais | — |
| `plotas_m2` | `number` | — | `4` | `open` | — | Nesuformuotas plotas kvadratiniais metrais | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Nesuformuoto ploto taškinė geometrija WKT (Well-Known Text) formatu | — |
| `geom_wkt` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija WKT (Well-Known Text) formatu (LKS94) | — |
| `geojson_wgs` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija GeoJSON formatu (koordinatės WGS84 sistemoje) | — |
| `geojson_lks` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija GeoJSON formatu (koordinatės LKS94 sistemoje) | — |
| `paskutinio_atnaujinimo_data` | `datetime` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv
