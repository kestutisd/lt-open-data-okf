---
type: Table
title: "Saltinis — Šaltiniai"
description: "Literatūros šaltiniai su pilnomis bibliografinėmis nuorodomis ir jų santrumpomis."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Saltinis"
tags: [gov, llti, saltinis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L38"
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L38"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2920/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Saltinis — Šaltiniai

Literatūros šaltiniai su pilnomis bibliografinėmis nuorodomis ir jų santrumpomis.[^manifest]

- **Model:** `datasets/gov/llti/patarles_priezodziai/Saltinis`[^manifest]
- **Dataset:** [Patarlių ir priežodžių elektroninis sąvadas](../patarles_priezodziai.md) (`datasets/gov/llti/patarles_priezodziai`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L38](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L38)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Saltinis` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `saltinio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L38 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L38)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai (https://data.gov.lt/datasets/2920/)
