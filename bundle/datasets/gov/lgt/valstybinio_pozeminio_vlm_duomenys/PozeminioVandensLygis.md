---
type: Table
title: "PozeminioVandensLygis — Valstybinio požeminio vandens monitoringo matavimų duomenys"
description: "Spinta table datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/poz_vandens_lygiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PozeminioVandensLygis — Valstybinio požeminio vandens monitoringo matavimų duomenys

- **Model:** `datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis`[^manifest]
- **Dataset:** [Valstybinio požeminio vandens monitoringo lygio matavimų duomenys](../valstybinio_pozeminio_vlm_duomenys.md) (`datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys`)
- **Manifest CSV:** [datasets/gov/lgt/poz_vandens_lygiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `integer` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `postas` | `string` | — | `4` | `open` | — | Stebimojo posto pavadinimas | — |
| `posto_id` | `integer` | — | `4` | `open` | — | Stebimojo posto numeris | — |
| `tasko_id` | `integer` | — | `4` | `open` | — | Taško numeris | — |
| `koord` | `geometry(point,3346)` | `m` | `4` | `open` | — | Koordinatės | — |
| `gr_nr` | `integer` | — | `4` | `open` | — | Gręžinio numeris | — |
| `abs_aukstis` | `number` | `m` | `4` | `open` | — | Taško absoliutinis aukštis | — |
| `data` | `date` | `D` | `4` | `open` | — | Matavimo data | — |
| `lygis_cm` | `integer` | `cm` | `4` | `open` | — | Vandens lygis nuo žemės paviršiaus centimetrais | — |
| `lygis_abs` | `number` | `m` | `4` | `open` | — | požeminio vandens lygis gręžinyje jūros lygio atžvilgiu (altitudė) | — |
| `temperatura` | `number` | `°C` | `4` | `open` | — | Vandens temperatūra | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/poz_vandens_lygiai.csv
