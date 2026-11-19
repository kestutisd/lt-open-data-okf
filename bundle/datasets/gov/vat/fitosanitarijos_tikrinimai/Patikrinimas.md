---
type: Table
title: "Patikrinimas — Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; žyma, kad tikrinami ne LR ūkio subjektai; metodinė sritis; tikrinimo sritis; tikrinimo pobūdis..."
description: "Spinta table datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas"
tags: [gov, vat, patikrinimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1864/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_tikrinimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Patikrinimas — Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo...

- **Model:** `datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas`[^manifest]
- **Dataset:** [Fitosanitarinių tikrinimų duomenys](../fitosanitarijos_tikrinimai.md) (`datasets/gov/vat/fitosanitarijos_tikrinimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai/Patikrinimas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis stulpelis | — |
| `tikrinimo_pradzia` | `date` | `D` | `4` | `open` | — | Tikrinimo pradžios data | — |
| `tikrinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Tikrinimo pabaigos data | — |
| `pobudis` | `string` | — | `4` | `open` | — | Tikrinimo pobūdis | — |
| `rusis` | `string` | — | `4` | `open` | — | Tikrinimo rūšis | — |
| `paimtas_meginys` | `boolean` | — | `4` | `open` | — | Paimtas mėginys | — |
| `tikrinamas_objektas` | `string` | — | `4` | `open` | — | Tikrinamo objekto rūšis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rusis` | `"neplaninis"` | — | — | — | — |
| `rusis` | `"planinis"` | — | — | — | — |
| `rusis` | `"planinis+neplaninis"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_tikrinimai (https://data.gov.lt/datasets/1864/)
