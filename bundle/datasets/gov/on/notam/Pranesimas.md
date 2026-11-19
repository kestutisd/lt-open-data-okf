---
type: Table
title: "Pranesimas — Oro Navigacijos (NOTAM) pranešimai aviatoriams"
description: "Rinkinyje pateikiami duomenys apie Oro Navigacijos siunčiamus pranešimus aviatoriams."
resource: "https://get.data.gov.lt/datasets/gov/on/notam/Pranesimas"
tags: [gov, "on", pranesimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/notam.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/on/notam.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2666/"
    title: "data.gov.lt DCAT-AP — datasets/gov/on/notam"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pranesimas — Oro Navigacijos (NOTAM) pranešimai aviatoriams

Rinkinyje pateikiami duomenys apie Oro Navigacijos siunčiamus pranešimus aviatoriams. Duomenys kaupiami nuo 2023m. rugsėjo mėn.[^manifest]

- **Model:** `datasets/gov/on/notam/Pranesimas`[^manifest]
- **Dataset:** [Oro Navigacijos (NOTAM) pranešimai aviatoriams](../notam.md) (`datasets/gov/on/notam`)[^manifest]
- **Manifest CSV:** [datasets/gov/on/notam.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/notam.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/notam/Pranesimas` (`deployed`)[^manifest]
- **Provider:** `on` — Oro Navigacija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `"NOTAMN"` | — | — | — | — |
| `type` | `"NOTAMR"` | — | — | — | — |
| `type` | `"SNOWTAM"` | — | — | — | — |
| `fir` | `"EYVL"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `raw_lt` | `update(property: "raw_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/on/notam.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/notam.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/on/notam (https://data.gov.lt/datasets/2666/)
