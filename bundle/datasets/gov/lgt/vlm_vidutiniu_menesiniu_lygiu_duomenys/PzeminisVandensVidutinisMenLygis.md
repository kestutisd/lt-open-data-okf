---
type: Table
title: "PzeminisVandensVidutinisMenLygis — Valstybinio požeminio vandens monitoringo vidutinių mėnesinių vandens lygių duomenys"
description: "Spinta table datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis"
tags: [gov, lgt, pzeminisvandensvidutinismenlygis, deployed, level-2, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1339/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PzeminisVandensVidutinisMenLygis — Valstybinio požeminio vandens monitoringo vidutinių mėnesinių vandens lygių duomenys

- **Model:** `datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis`[^manifest]
- **Dataset:** [Valstybinio požeminio vandens monitoringo vidutinių mėnesinių vandens lygių duomenys](../vlm_vidutiniu_menesiniu_lygiu_duomenys.md) (`datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys/PzeminisVandensVidutinisMenLygis` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/vidutiniu_menesiniu_lygiu.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/vlm_vidutiniu_menesiniu_lygiu_duomenys (https://data.gov.lt/datasets/1339/)
