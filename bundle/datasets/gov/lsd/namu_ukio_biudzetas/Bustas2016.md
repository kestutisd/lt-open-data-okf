---
type: Table
title: "Bustas2016 — Būstas ir patogumai 2016m."
description: "Būsto tipas, namų ūkio užimamų kambarių skaičius, būsto plotas, patogumai."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Bustas2016"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1326"
    last_modified: "2026-11-11T14:39:20Z"
---

# Bustas2016 — Būstas ir patogumai 2016m.

Būsto tipas, namų ūkio užimamų kambarių skaičius, būsto plotas, patogumai.

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Bustas2016`[^manifest]
- **Dataset:** [datasets/gov/lsd/namu_ukio_biudzetas](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L1326](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1326)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Bustas2016`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio identifikatorius | — |
| `dwltype` | `integer` | — | — | `open` | — | Būsto tipas | — |
| `nrooms` | `integer` | — | — | `open` | — | Bendras namų ūkio užimamų kambarių skaičius neįskaitant virtuvės vonios kambario tualeto | — |
| `totarea` | `integer` | — | — | `open` | — | Namų ūkio užimamas naudingasis plotas | — |
| `elect` | `integer` | `bool` | — | `open` | — | Ar būste yra: elektra | — |
| `bath` | `integer` | `bool` | — | `open` | — | Vonia dušas | — |
| `toilet` | `integer` | `bool` | — | `open` | — | Tualetas su nuleidžiamuoju vandeniu | — |
| `kitchen` | `integer` | `bool` | — | `open` | — | Atskira virtuvė | — |
| `water` | `integer` | — | — | `open` | — | koks vandens tiekimas būste: | — |
| `h_water` | `integer` | — | — | `open` | — | Koks karšto vandens tiekimas būste: | — |
| `sewerage` | `integer` | — | — | `open` | — | Koks nuotekų tvarkymas (kanalizacija) būste: | — |
| `heating` | `integer` | — | — | `open` | — | Pagrindinis būsto šildymo būdas: | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dwltype` | `1` | — | — | Vieno buto namas | — |
| `dwltype` | `2` | — | — | Butas dviejų butų ar sublokuotame name | — |
| `dwltype` | `3` | — | — | Butas daugiabučiame name | — |
| `dwltype` | `4` | — | — | Kita gyvenamoji patalpa | — |
| `elect` | `1` | — | — | Taip | — |
| `elect` | `2` | — | — | Ne | — |
| `elect` | `1` | — | — | Vyras | — |
| `elect` | `2` | — | — | Moteris | — |
| `bath` | `1` | — | — | Taip | — |
| `bath` | `2` | — | — | Ne | — |
| `bath` | `1` | — | — | Vyras | — |
| `bath` | `2` | — | — | Moteris | — |
| `toilet` | `1` | — | — | Taip | — |
| `toilet` | `2` | — | — | Ne | — |
| `toilet` | `1` | — | — | Vyras | — |
| `toilet` | `2` | — | — | Moteris | — |
| `kitchen` | `1` | — | — | Taip | — |
| `kitchen` | `2` | — | — | Ne | — |
| `kitchen` | `1` | — | — | Vyras | — |
| `kitchen` | `2` | — | — | Moteris | — |
| `water` | `1` | — | — | Centralizuotas | — |
| `water` | `2` | — | — | Vietinis | — |
| `water` | `3` | — | — | Nėra karšto vandens | — |
| `h_water` | `1` | — | — | Centralizuotas | — |
| `h_water` | `2` | — | — | Vietinis | — |
| `h_water` | `3` | — | — | Nėra kanalizacijos | — |
| `heating` | `1` | — | — | Centrinis šildymas iš šilumos tinklų | — |
| `heating` | `2` | — | — | Centrinis šildymas iš vietinio šilumos šaltinio | — |
| `heating` | `3` | — | — | Krosnis, židinys | — |
| `heating` | `4` | — | — | Nėra | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv
