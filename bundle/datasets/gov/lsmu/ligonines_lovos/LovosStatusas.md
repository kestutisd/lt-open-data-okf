---
type: Table
title: "LovosStatusas — Lovų užimtumo duomenys"
description: "Spinta table datasets/gov/lsmu/ligonines_lovos/LovosStatusas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosStatusas"
tags: [gov, lsmu, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# LovosStatusas — Lovų užimtumo duomenys

- **Model:** `datasets/gov/lsmu/ligonines_lovos/LovosStatusas`[^manifest]
- **Dataset:** [Lietuvos sveikatos universiteto Kauno klinikų Lovų duomenys](../ligonines_lovos.md) (`datasets/gov/lsmu/ligonines_lovos`)
- **Manifest CSV:** [datasets/gov/lsmu/ligonines_lovos.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosStatusas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `lovos_id` | `string` | — | `4` | `open` | — | Lovos eilutės unikalus identifikatorius | — |
| `vietos_id` | `string` | — | `4` | `open` | — | Vietos identifikatorius (referuoja į lovos_vieta.vietos_id) | — |
| `lovos_statusas` | `string` | — | `4` | `open` | — | Lovos statusas (Užimta, laisva, tvarkoma ...) | — |
| `statuso_pradzia` | `datetime` | `S` | `4` | `open` | — | Statuso galiojimo pradžios laikas | — |
| `statuso_pabaiga` | `datetime` | `S` | `4` | `open` | — | Statuso galiojimo terminas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lovos_statusas` | `"VACANT"` | — | `open` | Laisva | — |
| `lovos_statusas` | `"OCCUPIED"` | — | `open` | Užimta | — |
| `lovos_statusas` | `"IN_MAINTENANCE"` | — | `open` | Tvarkoma | — |
| `lovos_statusas` | `"RESERVED"` | — | `open` | Rezervuota | — |
| `lovos_statusas` | `"BEING_CLEANED"` | — | `open` | Valoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv
