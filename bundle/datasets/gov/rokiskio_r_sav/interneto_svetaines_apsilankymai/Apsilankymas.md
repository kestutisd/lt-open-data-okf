---
type: Table
title: "Apsilankymas — Interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymai"
description: "Lentelėje pateikta informacija apie interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymus iš Rokiškio rajono savivaldybės interneto turinio valdymo sistemos (ITVS)."
resource: "https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai/Apsilankymas"
tags: [gov, rokiskio_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apsilankymas — Interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymai

Lentelėje pateikta informacija apie interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymus iš Rokiškio rajono savivaldybės interneto turinio valdymo sistemos (ITVS). Duomenų laiko aprėptis - nuo 2020 metų. Informacija lentelėje papildoma kas mėnesį.

- **Model:** `datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai/Apsilankymas`[^manifest]
- **Dataset:** [Interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymai](../interneto_svetaines_apsilankymai.md) (`datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai`)
- **Manifest CSV:** [datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai/Apsilankymas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `puslapio_id` | `string` | — | `4` | `open` | — | Puslapio (skilties) identifikatorius | — |
| `uri` | `string` | — | `4` | `open` | — | Puslapio (skilties) nuoroda | — |
| `tipas` | `string` | — | `4` | `open` | — | Puslapio (skilties) tipas | — |
| `data` | `date` | `D` | `4` | `open` | — | Data | — |
| `apsilankymu_skaicius` | `integer` | `U` | `4` | `open` | — | Apsilankymų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv
