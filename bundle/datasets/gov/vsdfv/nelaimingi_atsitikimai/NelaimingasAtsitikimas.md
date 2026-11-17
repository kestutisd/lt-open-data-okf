---
type: Table
title: "NelaimingasAtsitikimas"
description: "Spinta table datasets/gov/vsdfv/nelaimingi_atsitikimai/NelaimingasAtsitikimas (11 columns)."
tags: [gov, vsdfv, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/nelaimingi_atsitikimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# NelaimingasAtsitikimas

- **Model:** `datasets/gov/vsdfv/nelaimingi_atsitikimai/NelaimingasAtsitikimas`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/nelaimingi_atsitikimai](../nelaimingi_atsitikimai.md) (`datasets/gov/vsdfv/nelaimingi_atsitikimai`)
- **Manifest CSV:** [datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `pasalpos_rusis, pasalpos_priezastis`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metu_menuo` | `date` | `1M` | `2` | `open` | — | Metų mėnuo | — |
| `pasalpos_rusis` | `string` | — | `3` | `open` | — | Pašalpos rūšis | — |
| `pasalpos_priezastis` | `string` | — | `3` | `open` | — | Pašalpos priežastis | — |
| `net_darb_lygis` | `string` | — | `3` | `open` | — | Netekto darbingumo lygis | — |
| `net_darb_tipas` | `string` | — | `3` | `open` | — | Netekto darbingumo tipas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[pavadinimas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `2` | `open` | — | Savivaldybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `gaveju_sk` | `number` | — | `4` | `open` | — | Gavėjų skaičius | — |
| `prisk_suma_eur` | `number` | — | `2` | `open` | — | Priskaičiuota suma, Eur | — |
| `ismoku_sk` | `number` | — | `4` | `open` | — | Išmokų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `prisk_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/nelaimingi_atsitikimai.csv
