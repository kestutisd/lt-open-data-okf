---
type: Table
title: "PozeminioVandensLygis — Valstybinio požeminio vandens monitoringo matavimų duomenys"
description: "Spinta table datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis"
tags: [gov, lgt, pozeminiovandenslygis, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lgt/poz_vandens_lygiai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1338/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PozeminioVandensLygis — Valstybinio požeminio vandens monitoringo matavimų duomenys

- **Model:** `datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis`[^manifest]
- **Dataset:** [Valstybinio požeminio vandens monitoringo lygio matavimų duomenys](../valstybinio_pozeminio_vlm_duomenys.md) (`datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/poz_vandens_lygiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/poz_vandens_lygiai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys (https://data.gov.lt/datasets/1338/)
