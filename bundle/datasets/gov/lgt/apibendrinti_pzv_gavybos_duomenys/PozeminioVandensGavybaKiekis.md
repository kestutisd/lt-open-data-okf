---
type: Table
title: "PozeminioVandensGavybaKiekis — Apibendrinti požeminio vandens gavybos duomenys"
description: "Spinta table datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/PozeminioVandensGavybaKiekis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/PozeminioVandensGavybaKiekis"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PozeminioVandensGavybaKiekis — Apibendrinti požeminio vandens gavybos duomenys

- **Model:** `datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/PozeminioVandensGavybaKiekis`[^manifest]
- **Dataset:** [Apibendrinti požeminio vandens gavybos duomenys](../apibendrinti_pzv_gavybos_duomenys.md) (`datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys`)
- **Manifest CSV:** [datasets/gov/lgt/pzm_vandens_gavyba.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/PozeminioVandensGavybaKiekis`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikacinis rinkinio numeris | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Požeminio vandens pavadinimas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `isgauta_m3` | `number` | `m^3` | `4` | `open` | — | Išgautas kiekis kubiniais metrais | — |
| `isgauta_m3_per_para` | `number` | `m^3/d` | `4` | `open` | — | Išgauta kubinių metrų per parą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv
