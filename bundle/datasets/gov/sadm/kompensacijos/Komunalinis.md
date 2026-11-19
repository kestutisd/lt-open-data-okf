---
type: Table
title: "Komunalinis — Duomenys apie kompensacijas"
description: "Duomenys apie būsto šildymo išlaidų, išlaidų geriamam ir (arba) karštam vandeniui kompensacijas praėjusiais metais"
resource: "https://get.data.gov.lt/datasets/gov/sadm/kompensacijos/Komunalinis"
tags: [gov, sadm, komunalinis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/kompensacijos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/sadm/kompensacijos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2242/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/kompensacijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Komunalinis — Duomenys apie kompensacijas

Duomenys apie būsto šildymo išlaidų, išlaidų geriamam ir (arba) karštam vandeniui kompensacijas praėjusiais metais[^manifest]

- **Model:** `datasets/gov/sadm/kompensacijos/Komunalinis`[^manifest]
- **Dataset:** [Būsto šildymo išlaidų, išlaidų geriamam ir (arba) karštam vandeniui kompensacijų duomenys](../kompensacijos.md) (`datasets/gov/sadm/kompensacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/kompensacijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/kompensacijos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/kompensacijos/Komunalinis` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `skaiciavimas` | `date` | `D` | `4` | `open` | — | Kompensacijos skaičiavimo data | — |
| `kompensavimas` | `date` | `D` | `4` | `open` | — | Kompensavimo data | — |
| `suma` | `number` | — | `2` | `open` | — | Kompensacijos suma | Eurais |
| `komunaline_paslauga` | `string` | — | `3` | `open` | — | Kompensacijos paslaugos reikšmės pavadinimas | — |
| `sav_kodas` | `string` | — | `2` | `open` | — | Savivaldybės, kur buvo išmokėta kompensacija, kodas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sav_kodas` | `create(property: "sav_kodas", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/kompensacijos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/kompensacijos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/kompensacijos (https://data.gov.lt/datasets/2242/)
