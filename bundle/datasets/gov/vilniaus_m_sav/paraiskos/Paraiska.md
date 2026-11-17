---
type: Table
title: "Paraiska — Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys"
description: "Aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos/Paraiska"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paraiska — Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys

Aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo. Lentelės objektas – konkursui teikta paraiška.

- **Model:** `datasets/gov/vilniaus_m_sav/paraiskos/Paraiska`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys](../paraiskos.md) (`datasets/gov/vilniaus_m_sav/paraiskos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/paraiskos.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos/Paraiska`
- **Primary Key (`ref`):** `teikejo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teikejo_id` | `string` | — | `4` | `open` | — | Paraiškos teikėjo identifikacinis numeris | — |
| `statusas` | `string` | — | `4` | `open` | — | Paraiškos statusas | — |
| `programos_kodas` | `string` | — | `4` | `open` | — | Konkurso programos, kuriai teikta paraiška, kodas | — |
| `teikimas` | `date` | `D` | `4` | `open` | — | Paraiškos teikimo data | — |
| `ivertis` | `number` | — | `4` | `open` | — | Paraiškos įvertis po vertinimo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv
