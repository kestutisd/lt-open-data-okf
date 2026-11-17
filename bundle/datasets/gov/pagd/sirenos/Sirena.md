---
type: Table
title: "Sirena"
description: "Sirenų informacija"
resource: "https://get.data.gov.lt/datasets/gov/pagd/sirenos/Sirena"
tags: [gov, pagd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pagd/sirenos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sirena

Sirenų informacija

- **Model:** `datasets/gov/pagd/sirenos/Sirena`[^manifest]
- **Dataset:** [pagd sirenos](../sirenos.md) (`datasets/gov/pagd/sirenos`)
- **Manifest CSV:** [datasets/gov/pagd/sirenos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/sirenos/Sirena`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | valstybės duomenų agentūros įrašų identifikatorius | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskrities pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | Kordinate lks 94 formatu | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | Kordinate wgs 84 formatu | — |
| `lks_x` | `integer` | — | `4` | `open` | — | Sunormuota LKS x koordinatė (7 skaitmenys) | — |
| `lks_y` | `integer` | — | `4` | `open` | — | Sunormuota LKS y koordinatė (6 skaitmenys) | — |
| `wgs_lon_ilguma` | `number` | — | `4` | `open` | — | WGS koordinatė (ilguma) paskaičiuota iš normuotų LKS koordinačių | — |
| `wgs_lat_platuma` | `number` | — | `4` | `open` | — | WGS koordinatė (platuma) paskaičiuota iš normuotų LKS koordinačių | — |
| `sirenos_sumontavimo_adresas` | `string` | — | `4` | `open` | — | Sirenos sumontavimo adresas | — |
| `garso_spindulys` | `number` | — | `4` | `open` | — | — | — |
| `savininkas` | `string` | — | `4` | `open` | — | — | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | — | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | — | — |
| `gyventoju_skaicius` | `integer` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/sirenos.csv
