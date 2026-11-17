---
type: Table
title: "ProjektoPirkimas — Projekto išlaidų duomenys"
description: "Spinta table datasets/gov/sppd/socialiniu_projektu_duomenys/ProjektoPirkimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/ProjektoPirkimas"
tags: [gov, sppd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L66"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProjektoPirkimas — Projekto išlaidų duomenys

- **Model:** `datasets/gov/sppd/socialiniu_projektu_duomenys/ProjektoPirkimas`[^manifest]
- **Dataset:** [Socialinių projektu duomenys](../socialiniu_projektu_duomenys.md) (`datasets/gov/sppd/socialiniu_projektu_duomenys`)
- **Manifest CSV:** [datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L66](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L66)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/ProjektoPirkimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `pirkimo_id` | `string` | — | `4` | `open` | — | Unikalus pirkimo identifikatorius | Projekto išlaidai priskirta id reikšmė kuri unikaliai identifikuoja eilutę lentelėje |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius kurio lėšomis darytas pirkimas | Išorinis raktas į projektų lentelę |
| `pirkimo_aprasymas` | `string` | — | `4` | `open` | — | Pirkimo trumpas aprašymas | Pirkimo aprašymas pagal Lietuvos Respublikos valstybės ir savivaldybių biudžetų pajamų ir išlaidų klasifikatorių |
| `atsiskaitymo_data` | `date` | `D` | `4` | `open` | — | Atsiskaitymo data už pirkinį | — |
| `ketvirtis` | `string` | — | `4` | `open` | — | Atsiskaitymo ketvirtis | — |
| `sumoketa_suma` | `number` | — | `4` | `open` | — | Sumokėta suma atsiskaitymo metu | — |
| `iraso_sukurimo_momentas` | `datetime` | `S` | `4` | `open` | — | Įrašo sukūrimo momentas | Įrašo sukūrimo momentas duomenų bazėje |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sumoketa_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv
