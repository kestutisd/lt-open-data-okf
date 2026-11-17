---
type: Table
title: "PzeminisVandensVidutinisMenLygis — Valstybinio požeminio vandens monitoringo vidutinių mėnesinių vandens lygių duomenys"
description: "Spinta table datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis"
tags: [gov, lgt, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PzeminisVandensVidutinisMenLygis — Valstybinio požeminio vandens monitoringo vidutinių mėnesinių vandens lygių duomenys

- **Model:** `datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis`[^manifest]
- **Dataset:** [datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys](../vlm_vidutiniu_menesiniu_lygiu_duomenys.md) (`datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys`)
- **Manifest CSV:** [datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `postas` | `string` | — | `4` | `open` | — | Monitoringo posto pavadinimas | — |
| `posto_id` | `integer` | — | `4` | `open` | — | Monitoringo posto ID numeris | — |
| `tasko_id` | `string` | — | `4` | `open` | — | Matavimų taško numeris | — |
| `kooord` | `geometry(point,3346)` | `m` | `4` | `open` | — | Taškas | — |
| `gr_nr` | `integer` | — | `4` | `open` | — | Gręžinio numeris | — |
| `abs_aukstis` | `number` | `m` | `4` | `open` | — | Matavimo taško absoliutinis aukštis (altitudė) | — |
| `menuo` | `date` | `M` | `4` | `open` | — | Mėnuo | — |
| `vid_lygis` | `number` | `cm` | `4` | `open` | — | Vidutinis mėnesio vandens lygis centimetrais nuo žemės paviršiaus | — |
| `abs_lygis_mvn` | `number` | `m` | `4` | `open` | — | požeminio vandens lygis gręžinyje jūros lygio atžvilgiu (altitudė) | — |
| `vid_temperatura` | `number` | `°C` | `4` | `open` | — | Vidutinė mėnesio vandens temperatūra | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv
