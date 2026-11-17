---
type: Table
title: "Siunta — Siuntų duomenys"
description: "Pateikiami siuntų duomenys: kilmės šalis, produkto grupė, produkto pavadinimas, partijos numeris, tinkamumo terminas ir tinkamumo tipas."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Siunta"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# Siunta — Siuntų duomenys

Pateikiami siuntų duomenys: kilmės šalis, produkto grupė, produkto pavadinimas, partijos numeris, tinkamumo terminas ir tinkamumo tipas.

- **Model:** `datasets/gov/vmvt/pranesimai/Siunta`[^manifest]
- **Dataset:** [Pranešimai](../pranesimai.md) (`datasets/gov/vmvt/pranesimai`)
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Siunta`
- **Primary Key (`ref`):** `siuntos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `siuntos_id` | `string` | — | `4` | `open` | — | Unikalus siuntos identifikatorius | — |
| `pranesimo_id` | `string` | — | `4` | `open` | — | Pranešimo identifikatorius | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Kilmės šalis | — |
| `produkto_grupe` | `string` | — | `4` | `open` | — | Produkto grupė | — |
| `produkto_pavadinimas` | `string` | — | `4` | `open` | — | Produkto pavadinimas | — |
| `partijos_numeris` | `string` | — | `4` | `open` | — | Partijos numeris | — |
| `tinkamumo_terminas` | `date` | — | `4` | `open` | — | Tinkamumo terminas | — |
| `tinkamumo_tipas` | `string` | — | `4` | `open` | — | Tinkamumo tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv
