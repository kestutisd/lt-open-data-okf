---
type: Table
title: "VizuRezimas"
description: "Spinta table datasets/gov/urm/vr/VizuRezimas (4 columns)."
tags: [gov, urm, vizurezimas, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vr.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/urm/vr.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# VizuRezimas

- **Model:** `datasets/gov/urm/vr/VizuRezimas`[^manifest]
- **Dataset:** [Vidutinio mėnesio darbo užmokesčio duomenys](../vr.md) (`datasets/gov/urm/vr`)[^manifest]
- **Manifest CSV:** [datasets/gov/urm/vr.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vr.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `urm` — Lietuvos Respublikos užsienio reikalų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `valstybe` | `string` | — | `3` | `open` | — | Valstybė | — |
| `vizos_reikalingumas` | `string` | — | `4` | `open` | — | Vizos reikalingumas | — |
| `pastaba` | `string` | — | `3` | `open` | — | Pastabos | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vizos_reikalingumas` | `"Taip"` | — | — | Viza reikalinga | — |
| `vizos_reikalingumas` | `"Ne"` | — | — | Vizos nereikia | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/urm/vr.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vr.csv#L4)
