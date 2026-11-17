---
type: Table
title: "VizuRezimas"
description: "Spinta table datasets/gov/urm/vr/VizuRezimas (4 columns)."
tags: [gov, urm, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/urm/vr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vr.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VizuRezimas

- **Model:** `datasets/gov/urm/vr/VizuRezimas`[^manifest]
- **Dataset:** [Vidutinio mėnesio darbo užmokesčio duomenys](../vr.md) (`datasets/gov/urm/vr`)
- **Manifest CSV:** [datasets/gov/urm/vr.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vr.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `valstybe` | `string` | — | `3` | `open` | — | Valstybė | — |
| `vizos_reikalingumas` | `string` | — | `4` | `open` | — | Vizos reikalingumas | — |
| `pastaba` | `string` | — | `3` | `open` | — | Pastabos | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vizos_reikalingumas` | `"Taip"` | — | — | Viza reikalinga | — |
| `vizos_reikalingumas` | `"Ne"` | — | — | Vizos nereikia | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/urm/vr.csv
