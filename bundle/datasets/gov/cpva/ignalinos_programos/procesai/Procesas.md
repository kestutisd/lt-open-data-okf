---
type: Table
title: "Procesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ procesų sąrašas"
description: "Spinta table datasets/gov/cpva/ignalinos_programos/procesai/Procesas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Procesas"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# Procesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ procesų sąrašas

- **Model:** `datasets/gov/cpva/ignalinos_programos/procesai/Procesas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys](../procesai.md) (`datasets/gov/cpva/ignalinos_programos/procesai`)
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_procesai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Procesas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Proceso identifikatorius | — |
| `proceso_tipas` | `string` | — | `4` | `open` | — | Proceso tipas | — |
| `procesas` | `string` | — | `4` | `open` | — | Proceso pavadinimas | — |
| `proceso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Proceso sukūrimo data | — |
| `proceso_kurejas` | `string` | — | `4` | `open` | — | Proceso kūrėjo id | — |
| `statusas` | `string` | — | `4` | `open` | — | Proceso statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv
