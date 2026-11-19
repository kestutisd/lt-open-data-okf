---
type: Table
title: "Sarasas — Lošimo įrenginių tipų sąrašas"
description: "Lošimo įrenginių tipų klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/lpt/irenginiu_tipas/Sarasas"
tags: [gov, lpt, sarasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/irenginiu_tipas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lpt/irenginiu_tipas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/779/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lpt/irenginiu_tipas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sarasas — Lošimo įrenginių tipų sąrašas

Lošimo įrenginių tipų klasifikatorius[^manifest]

- **Model:** `datasets/gov/lpt/irenginiu_tipas/Sarasas`[^manifest]
- **Dataset:** [Lošimo įrenginių tipų sąrašas](../irenginiu_tipas.md) (`datasets/gov/lpt/irenginiu_tipas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lpt/irenginiu_tipas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/irenginiu_tipas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/irenginiu_tipas/Sarasas` (`deployed`)[^manifest]
- **Provider:** `lpt` — Lošimų priežiūros tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `irenginio_tipo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginio_tipo_id` | `string` | — | `4` | `open` | — | Įrenginio tipo unikalus identifikatorius | — |
| `tipo_pavadinimas_lt` | `string` | — | `4` | `open` | — | Įrenginio tipas | — |
| `irenginio_kategorija` | `string` | — | `4` | `open` | — | Įrenginio kategorija | — |
| `gamintojas` | `string` | — | `4` | `open` | — | Gamintojo pavadinimas | — |
| `patvirtinimo_data` | `date` | `D` | `4` | `open` | — | Patvirtinimo data | — |
| `patvirtinimo_isakymas` | `string` | — | `4` | `open` | — | Patvirtinimo įsakymas | — |
| `panaikinimo_data` | `date` | `D` | `4` | `open` | — | Panaikinimo data | — |
| `panaikinimo_isakymas` | `string` | — | `4` | `open` | — | Panaikinimo įsakymas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `irenginio_kategorija` | `"A kategorijos automatai"` | — | — | A kategorijos automatai | — |
| `irenginio_kategorija` | `"B kategorijos automatai"` | — | — | B kategorijos automatai | — |
| `irenginio_kategorija` | `"Kiti įrenginiai"` | — | — | Kiti įrenginiai | — |
| `irenginio_kategorija` | `"Ruletė"` | — | — | Ruletė | — |
| `irenginio_kategorija` | `"Kortų stalai"` | — | — | Kortų stalai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipo_pavadinimas_lt` | `update(property: "tipo_pavadinimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/irenginiu_tipas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/irenginiu_tipas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lpt/irenginiu_tipas (https://data.gov.lt/datasets/779/)
