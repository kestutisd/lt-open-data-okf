---
type: Table
title: "Mikroprocesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ mikroprocesų sąrašas"
description: "Spinta table datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L29"
    last_modified: "2026-11-11T14:39:20Z"
---

# Mikroprocesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ mikroprocesų sąrašas

- **Model:** `datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys](../procesai.md) (`datasets/gov/cpva/ignalinos_programos/procesai`)
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_procesai.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L29)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Mikroproceso identifikatorius | — |
| `priklauso_subprocesui` | `string` | — | `4` | `open` | — | Priklauso subprocesui | — |
| `mikroproceso_tipas` | `string` | — | `4` | `open` | — | Mikroproceso tipas | — |
| `mikroprocesas` | `string` | — | `4` | `open` | — | Mikroproceso pavadinimas | — |
| `mikroproceso_kodas` | `string` | — | `4` | `open` | — | Mikroproceso kodas | — |
| `mikroproceso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Mikroproceso sukūrimo data | — |
| `atlikti_iki` | `datetime` | `L` | `4` | `open` | — | Mikroprocesą reikia atliki iki | — |
| `mikroproceso_kurejas` | `string` | — | `4` | `open` | — | Mikroproceso kūrėjo id | — |
| `statusas` | `string` | — | `4` | `open` | — | Mikroproceso statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv
