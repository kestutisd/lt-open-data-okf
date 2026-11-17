---
type: Table
title: "Mokejimas — Duomenys apie išmokas vaikams"
description: "Spinta table datasets/gov/sadm/ismokos_vaikams/Mokejimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/ismokos_vaikams/Mokejimas"
tags: [gov, sadm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sadm/ismokos_vaikams.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/ismokos_vaikams.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Mokejimas — Duomenys apie išmokas vaikams

- **Model:** `datasets/gov/sadm/ismokos_vaikams/Mokejimas`[^manifest]
- **Dataset:** [datasets/gov/sadm/ismokos_vaikams](../ismokos_vaikams.md) (`datasets/gov/sadm/ismokos_vaikams`)
- **Manifest CSV:** [datasets/gov/sadm/ismokos_vaikams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/ismokos_vaikams.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/ismokos_vaikams/Mokejimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `pasalpos_tipas` | `string` | — | `3` | `open` | — | Išmokėtos pašalpos tipas | — |
| `paskyrimo_pradzia` | `date` | `D` | `4` | `open` | — | Išmokų mokėjimo datos intervalo pradžia | — |
| `paskyrimo_pabaiga` | `date` | `D` | `4` | `open` | — | Išmokų mokėjimo datos intervalo pabaiga | — |
| `nuo` | `integer` | — | `2` | `open` | — | Išmokų mokėjimo pradžios data | — |
| `iki` | `integer` | — | `2` | `open` | — | Išmokų mokėjimo pabaigos data | — |
| `mokejimas` | `date` | `M` | `4` | `open` | — | Išmokos skaičiavimo mėnuo | — |
| `priskaiciuota` | `number` | — | `2` | `open` | — | Priskaičiuota išmokų suma | — |
| `ismoketa` | `number` | — | `2` | `open` | — | Išmokėta išmokų suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priskaiciuota` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ismoketa` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/ismokos_vaikams.csv
