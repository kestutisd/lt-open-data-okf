---
type: Table
title: "Irenginys — Marijampolės savivaldybės reklamų įrengimai"
description: "Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Irenginys"
tags: [gov, marijampoles_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Irenginys — Marijampolės savivaldybės reklamų įrengimai

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys. Duomenų rinkinį sudaro: įmonė, reklamos statusas, adresas, koordinatės, tipas, zona.

Viena eilutė atitinka vieną reklamos objektą.

- **Model:** `datasets/gov/marijampoles_sav/reklamos/Irenginys`[^manifest]
- **Dataset:** [Marijampolės savivaldybės reklamų įrengimai ir leidimai](../reklamos.md) (`datasets/gov/marijampoles_sav/reklamos`)
- **Manifest CSV:** [datasets/gov/marijampoles_sav/reklamos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Irenginys`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio identifikatorius | — |
| `imone` | `string` | — | `4` | `open` | — | Įmonė | — |
| `galiojimo_statusas` | `string` | — | `4` | `open` | — | Galiojimo statusas | — |
| `galiojimo_statuso_data` | `date` | `D` | `4` | `open` | — | Galiojimo statuso data | — |
| `reklamos_adresas` | `string` | — | `4` | `open` | — | Reklamos adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Geometrija | — |
| `reklamos_tipas` | `string` | — | `4` | `open` | — | Reklamos tipas | — |
| `reklamos_zona` | `string` | — | `4` | `open` | — | Reklamos zona | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv
