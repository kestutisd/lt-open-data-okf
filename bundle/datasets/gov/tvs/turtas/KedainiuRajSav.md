---
type: Table
title: "KedainiuRajSav"
description: "Spinta table datasets/gov/tvs/turtas/KedainiuRajSav (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/tvs/turtas/KedainiuRajSav"
tags: [gov, tvs, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/tvs/turtas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# KedainiuRajSav

- **Model:** `datasets/gov/tvs/turtas/KedainiuRajSav`[^manifest]
- **Dataset:** [Duomenys apie savyvaldybės turtą](../turtas.md) (`datasets/gov/tvs/turtas`)
- **Manifest CSV:** [datasets/gov/tvs/turtas.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tvs/turtas/KedainiuRajSav`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `ntr_reg_kodas` | `string` | — | `4` | `open` | — | NT registro kodas | — |
| `statybos_pabaigos_metai` | `integer` | — | `4` | `open` | — | Objekto statybos pabaigos metai | — |
| `plotas_kv_metrais` | `number` | — | `4` | `open` | — | Objekto plotas kvadratiniais metrais | — |
| `ntr_paskirtis` | `string` | — | `4` | `open` | — | Objekto paskirtis | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Geografinės koordinatės | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Geografinės koordinatės | — |
| `lks_x` | `number` | — | `4` | `open` | — | Stačiakampės plokštuminės LKS-94 koordinatės | — |
| `lks_y` | `number` | — | `4` | `open` | — | Stačiakampės plokštuminės LKS-94 koordinatės | — |
| `geometrija` | `string` | — | `4` | `open` | — | Geografinės koordinatės | — |
| `tipas` | `string` | — | `4` | `open` | — | Objekto adreso informacijos aktualumas | — |
| `patikimumas` | `number` | — | `4` | `open` | — | Geografinių koordinačių patikimumas (procentais) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/tvs/turtas.csv
