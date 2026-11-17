---
type: Table
title: "Monitoringas — Saugomų teritorijų lankytojų duomenys"
description: "Spinta table datasets/gov/vstt/lankytojai/Monitoringas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/lankytojai/Monitoringas"
tags: [gov, vstt, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/lankytoju_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Monitoringas — Saugomų teritorijų lankytojų duomenys

- **Model:** `datasets/gov/vstt/lankytojai/Monitoringas`[^manifest]
- **Dataset:** [Saugomų teritorijų lankytojų duomenys](../lankytojai.md) (`datasets/gov/vstt/lankytojai`)
- **Manifest CSV:** [datasets/gov/vstt/lankytoju_monitoringas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/lankytojai/Monitoringas`
- **Primary Key (`ref`):** `teritorija`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teritorija` | `string` | — | `2` | `open` | — | Saugoma teritorija vieta | — |
| `lankytojai` | `integer` | `U` | `4` | `open` | — | Lankytoju skaičius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `geometrija` | `geometry(polygon,3346)` | — | `3` | `open` | — | Lankomos vietos geometrija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref:"Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/lankytoju_monitoringas.csv
