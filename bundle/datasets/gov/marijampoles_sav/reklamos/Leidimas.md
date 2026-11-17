---
type: Table
title: "Leidimas — Marijampolės savivaldybės reklamų leidimai"
description: "Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi lauko reklamų leidimai."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Leidimas"
tags: [gov, marijampoles_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L26"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Marijampolės savivaldybės reklamų leidimai

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi lauko reklamų leidimai. Duomenų rinkinį sudaro: leidimo numeris bei leidimo galiojimo terminai.

Viena eilutė atitinka vieną leidimą.

- **Model:** `datasets/gov/marijampoles_sav/reklamos/Leidimas`[^manifest]
- **Dataset:** [Marijampolės savivaldybės reklamų įrengimai ir leidimai](../reklamos.md) (`datasets/gov/marijampoles_sav/reklamos`)
- **Manifest CSV:** [datasets/gov/marijampoles_sav/reklamos.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L26)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Leidimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio identifikatorius | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv
