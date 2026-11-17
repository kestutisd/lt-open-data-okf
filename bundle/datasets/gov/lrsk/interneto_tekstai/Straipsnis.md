---
type: Table
title: "Straipsnis — Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys"
description: "Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lrsk/interneto_tekstai/Straipsnis"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/tekstai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/tekstai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Straipsnis — Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys

Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys

- **Model:** `datasets/gov/lrsk/interneto_tekstai/Straipsnis`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys](../interneto_tekstai.md) (`datasets/gov/lrsk/interneto_tekstai`)
- **Manifest CSV:** [datasets/gov/lrsk/tekstai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/tekstai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/interneto_tekstai/Straipsnis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo unikalus identifikatorius | — |
| `tekst_pav_lt` | `string` | — | `2` | `open` | — | Teksto pavadinimas internetiniame puslapyje | — |
| `tekstas_lt` | `string` | — | `2` | `open` | — | Publikuoto teksto turinys | — |
| `kalba` | `string` | — | `4` | `open` | — | Teksto kalba | — |
| `paskelbimas` | `date` | `D` | `4` | `open` | — | Teksto paskelbimo data | — |
| `koregavimas` | `date` | `D` | `4` | `open` | — | Paskutinė teksto redagavimo data | — |
| `tekst_url` | `string` | — | `4` | `open` | — | Nuoroda į tekstą Lietuvos Respublikos Seimo portale | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tekst_pav_lt` | `update(property: "tekst_pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `tekstas_lt` | `update(property: "tekstas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/tekstai.csv
