---
type: Table
title: "VilniausRajSiuksliavezioMarsrutas — Vilniaus rajono savivaldybės šiukšliavežių maršrutai"
description: "Vilniaus rajono savivaldybės informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/marsrutai/VilniausRajSiuksliavezioMarsrutas"
tags: [gov, asmlis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L45"
    last_modified: "2026-11-11T14:39:20Z"
---

# VilniausRajSiuksliavezioMarsrutas — Vilniaus rajono savivaldybės šiukšliavežių maršrutai

Vilniaus rajono savivaldybės informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys:šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis.

- **Model:** `datasets/gov/asmlis/marsrutai/VilniausRajSiuksliavezioMarsrutas`[^manifest]
- **Dataset:** [Šiukšliavežių maršrutai](../marsrutai.md) (`datasets/gov/asmlis/marsrutai`)
- **Manifest CSV:** [datasets/gov/asmlis/marsrutai.csv#L45](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L45)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/marsrutai/VilniausRajSiuksliavezioMarsrutas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `marsrutas` | `string` | — | `4` | `open` | — | Maršrutas | — |
| `automobilio_nr` | `string` | — | `4` | `open` | — | Automobilio numeris (šifruotas) | — |
| `marke` | `string` | — | `4` | `open` | — | Automobilio markė | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Data | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `tikslumas` | `number` | — | `4` | `open` | — | TIklsumas | — |
| `koodinates_saltinis` | `string` | — | `4` | `open` | — | Koordinatės šaltinis (gps - navigaciją, foreign - išoriniai, kiti šaltiniai) | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Geometrija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv
