---
type: Table
title: "Pranesimas — Oro Navigacijos (NOTAM) pranešimai aviatoriams"
description: "Rinkinyje pateikiami duomenys apie Oro Navigacijos siunčiamus pranešimus aviatoriams."
resource: "https://get.data.gov.lt/datasets/gov/on/notam/Pranesimas"
tags: [gov, on, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/on/notam.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/notam.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pranesimas — Oro Navigacijos (NOTAM) pranešimai aviatoriams

Rinkinyje pateikiami duomenys apie Oro Navigacijos siunčiamus pranešimus aviatoriams. Duomenys kaupiami nuo 2023m. rugsėjo mėn.

- **Model:** `datasets/gov/on/notam/Pranesimas`[^manifest]
- **Dataset:** [Oro Navigacijos (NOTAM) pranešimai aviatoriams](../notam.md) (`datasets/gov/on/notam`)
- **Manifest CSV:** [datasets/gov/on/notam.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/notam.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/notam/Pranesimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `id` | `string` | — | `4` | `open` | — | NOTAM pranešimo numeris | — |
| `date` | `datetime` | `S` | `4` | `open` | — | NOTAM pranešimo gavimo data | — |
| `type` | `string` | — | `4` | `open` | — | NOTAM tipas | — |
| `reference` | `string` | — | `4` | `open` | — | Seno NOTAM pranešimo numeris, jei toks yra | — |
| `fir` | `string` | — | `4` | `open` | — | FIR (Flight Information Region) - oro erdvė, nurodoma ICAO kodu. | — |
| `coordinates` | `string` | — | `4` | `open` | — | Koordinatės Lietuvos oro erdvėje | — |
| `koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | WGS koordinatės Lietuvos oro erdvėje | — |
| `code` | `string` | — | `4` | `open` | — | Erdvės ar oro uosto, kuriam skirtas NOTAM pranešimas, ICAO kodas | — |
| `date_from` | `datetime` | `S` | `4` | `open` | — | Įsigaliojimo data, laikas | — |
| `date_to` | `datetime` | `S` | `4` | `open` | — | Galiojimo pabaigos data ir laikas | — |
| `permanent` | `boolean` | — | `4` | `open` | — | Nuoroda, ar NOTAM pranešimas pastovus, be galiojimo pabaigos | — |
| `raw_lt` | `string` | — | `2` | `open` | — | NOTAM Pranešimo turinys | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `"NOTAMN"` | — | — | — | — |
| `type` | `"NOTAMR"` | — | — | — | — |
| `type` | `"SNOWTAM"` | — | — | — | — |
| `fir` | `"EYVL"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `raw_lt` | `update(property: "raw_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/on/notam.csv
