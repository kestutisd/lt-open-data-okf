---
type: Table
title: "Pensija"
description: "Spinta table datasets/gov/vsdfv/pensijos/Pensija (12 columns)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pensijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pensijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pensija

- **Model:** `datasets/gov/vsdfv/pensijos/Pensija`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/pensijos](../pensijos.md) (`datasets/gov/vsdfv/pensijos`)
- **Manifest CSV:** [datasets/gov/vsdfv/pensijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pensijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `metu_menuo`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metu_menuo` | `date` | `1M` | `2` | `open` | — | Metų mėnuo | — |
| `pensijos_rusis` | `string` | — | `3` | `open` | — | Pensijos rūšis | — |
| `pensijos_porusis` | `string` | — | `3` | `open` | — | Pensijos porūšis | — |
| `net_darb_grupe` | `string` | — | `3` | `open` | — | Netekto darbingumo grupė | — |
| `biudzetas` | `string` | — | `3` | `open` | — | Valstybinio socialinio draudimo biudžetas | — |
| `lytis` | `string` | — | `3` | `open` | — | Lytis | — |
| `ar_dirba` | `string` | — | `4` | `open` | — | Ar dirba mėnesio pabaigoje? | — |
| `ar_turi_staza` | `string` | — | `4` | `open` | — | Ar turi stažą? | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[pavadinimas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `2` | `open` | — | Savivaldybė | — |
| `prisk_suma_eur` | `number` | — | `2` | `open` | — | Priskaičiuota suma, Eur | — |
| `gaveju_sk` | `number` | — | `4` | `open` | — | Gavėjų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `ar_dirba` | `"Dirba"` | — | — | Dirba | — |
| `ar_dirba` | `"Nedirba"` | — | — | Nedirba | — |
| `ar_turi_staza` | `"Turi"` | — | — | Turi stažo | — |
| `ar_turi_staza` | `"Neturi"` | — | — | Neturi stažo | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `prisk_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pensijos.csv
