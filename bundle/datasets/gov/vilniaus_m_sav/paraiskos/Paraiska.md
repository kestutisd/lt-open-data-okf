---
type: Table
title: "Paraiska — Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys"
description: "Aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos/Paraiska"
tags: [gov, vilniaus_m_sav, paraiska, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3848/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paraiska — Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys

Aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo. Lentelės objektas – konkursui teikta paraiška.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/paraiskos/Paraiska`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys](../paraiskos.md) (`datasets/gov/vilniaus_m_sav/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/paraiskos.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos/Paraiska` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `teikejo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teikejo_id` | `string` | — | `4` | `open` | — | Paraiškos teikėjo identifikacinis numeris | — |
| `statusas` | `string` | — | `4` | `open` | — | Paraiškos statusas | — |
| `programos_kodas` | `string` | — | `4` | `open` | — | Konkurso programos, kuriai teikta paraiška, kodas | — |
| `teikimas` | `date` | `D` | `4` | `open` | — | Paraiškos teikimo data | — |
| `ivertis` | `number` | — | `4` | `open` | — | Paraiškos įvertis po vertinimo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/paraiskos (https://data.gov.lt/datasets/3848/)
