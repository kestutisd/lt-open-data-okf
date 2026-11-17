---
type: Table
title: "Subprocesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ subprocesų sąrašas"
description: "Spinta table datasets/gov/cpva/ignalinos_programos/procesai/Subprocesas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Subprocesas"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subprocesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ subprocesų sąrašas

- **Model:** `datasets/gov/cpva/ignalinos_programos/procesai/Subprocesas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys](../procesai.md) (`datasets/gov/cpva/ignalinos_programos/procesai`)
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_procesai.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Subprocesas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Subproceso identifikatorius | — |
| `priklauso_procesui` | `string` | — | `4` | `open` | — | Priklauso procesui | — |
| `subproceso_tipas` | `string` | — | `4` | `open` | — | Subproceso tipas | — |
| `subprocesas` | `string` | — | `4` | `open` | — | Subproceso pavadinimas | — |
| `subproceso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Subproceso sukūrimo data | — |
| `atlikti_iki` | `datetime` | `L` | `4` | `open` | — | Subproceso atlikimo data iki | — |
| `subproceso_kurejas` | `string` | — | `4` | `open` | — | Subproceso kūrėjo id | — |
| `statusas` | `string` | — | `4` | `open` | — | Subproceso statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv
