---
type: Table
title: "Dokumentas"
description: "Spinta table datasets/gov/sakiai/gaunami_dokumentai/Dokumentas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/Dokumentas"
tags: [gov, sakiai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas

- **Model:** `datasets/gov/sakiai/gaunami_dokumentai/Dokumentas`[^manifest]
- **Dataset:** [Šakių rajono savivaldybės gaunami dokumentai](../gaunami_dokumentai.md) (`datasets/gov/sakiai/gaunami_dokumentai`)
- **Manifest CSV:** [datasets/gov/sakiai/gaunami_dokumentai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/Dokumentas`
- **Primary Key (`ref`):** `obj_id`
- **Access:** `open` (inherited)

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obj_id` | `integer` | — | `4` | `open` (inherited) | — | — | — |
| `obj_data` | `datetime` | `S` | `4` | `open` (inherited) | — | Registravimo data | — |
| `obj_rz_id` | `ref` | [Registras](Registras.md) | `4` | `open` (inherited) | — | — | — |
| `obj_rastine_sbj_id` | `ref` | [Subjektas](Subjektas.md) | `4` | `open` (inherited) | — | Raštinė kuriai priklauso dokumentas | — |
| `obj_elektroninis` | `boolean` | — | `3` | `open` (inherited) | — | Yra elektroninis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv
