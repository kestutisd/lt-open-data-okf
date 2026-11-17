---
type: Table
title: "Subjektas — Subjektų duomenys"
description: "Pateikiama informacija apie ukio subjektus: subjekto pavadinimas, tipas ir šalis."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Subjektas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Subjektų duomenys

Pateikiama informacija apie ukio subjektus: subjekto pavadinimas, tipas ir šalis.

- **Model:** `datasets/gov/vmvt/pranesimai/Subjektas`[^manifest]
- **Dataset:** [Pranešimai](../pranesimai.md) (`datasets/gov/vmvt/pranesimai`)
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai/Subjektas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus subjekto identifikatorius | — |
| `siuntos_id` | `string` | — | `4` | `open` | — | Siuntos identifikatorius | — |
| `pranesimo_id` | `string` | — | `4` | `open` | — | Pranešimo identifikatorius | — |
| `ukio_subjektas` | `string` | — | `4` | `open` | — | ūkio subjekto pavadinimas | — |
| `subjekto_tipas` | `string` | — | `4` | `open` | — | Subjekto tipas | — |
| `ukio_subjekto_salis` | `string` | — | `4` | `open` | — | ūkio subjekto šalis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv
