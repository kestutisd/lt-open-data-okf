---
type: Table
title: "Saltinis — Šaltiniai"
description: "Literatūros šaltiniai su pilnomis bibliografinėmis nuorodomis ir jų santrumpomis."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Saltinis"
tags: [gov, llti, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L38"
    last_modified: "2026-11-11T14:39:20Z"
---

# Saltinis — Šaltiniai

Literatūros šaltiniai su pilnomis bibliografinėmis nuorodomis ir jų santrumpomis.

- **Model:** `datasets/gov/llti/patarles_priezodziai/Saltinis`[^manifest]
- **Dataset:** [Patarlių ir priežodžių elektroninis sąvadas](../patarles_priezodziai.md) (`datasets/gov/llti/patarles_priezodziai`)
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L38](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L38)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Saltinis`
- **Primary Key (`ref`):** `saltinio_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `saltinio_id` | `string` | — | `4` | `open` | — | Šaltinio identifikatorius | — |
| `santrumpa` | `string` | — | `4` | `open` | — | Šaltinio santrumpa | — |
| `bibliografine_nuoroda` | `string` | — | `4` | `open` | — | Bibliografinė noroda | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bibliografine_nuoroda` | `update(property: "bibliografine_nuoroda", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv
