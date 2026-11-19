---
type: Table
title: "Mokejimas — Duomenys apie išmokas vaikams"
description: "Spinta table datasets/gov/sadm/ismokos_vaikams/Mokejimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/ismokos_vaikams/Mokejimas"
tags: [gov, sadm, mokejimas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/ismokos_vaikams.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/sadm/ismokos_vaikams.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1999/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/ismokos_vaikams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mokejimas — Duomenys apie išmokas vaikams

- **Model:** `datasets/gov/sadm/ismokos_vaikams/Mokejimas`[^manifest]
- **Dataset:** [Išmokų vaikams duomenys](../ismokos_vaikams.md) (`datasets/gov/sadm/ismokos_vaikams`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/ismokos_vaikams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/ismokos_vaikams.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/ismokos_vaikams/Mokejimas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/ismokos_vaikams.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/ismokos_vaikams.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/ismokos_vaikams (https://data.gov.lt/datasets/1999/)
