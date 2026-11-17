---
type: Table
title: "Bustas2012 — Būstas ir patogumai 2012m."
description: "Būsto tipas, namų ūkio užimamų kambarių skaičius, būsto plotas, patogumai."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Bustas2012"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L717"
    last_modified: "2026-11-11T14:39:20Z"
---

# Bustas2012 — Būstas ir patogumai 2012m.

Būsto tipas, namų ūkio užimamų kambarių skaičius, būsto plotas, patogumai.

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Bustas2012`[^manifest]
- **Dataset:** [datasets/gov/lsd/namu_ukio_biudzetas](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L717](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L717)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Bustas2012`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `dwlowner` | `integer` | — | — | `open` | — | Kam priklauso būstas kuriame Jūs gyvenate? | — |
| `formrent` | `integer` | — | — | `open` | — | Ar Jūs nuomojate šį būstą? | — |
| `dwltype` | `integer` | — | — | `open` | — | Koks Jūsų būsto tipas? | — |
| `nrooms` | `integer` | — | — | `open` | — | Koks bendras Jūsų namų ūkio užimamų kambarių skaičius neįskaitant virtuvės vonios kambario tualeto? | — |
| `totarea` | `integer` | — | — | `open` | — | Koks Jūsų namų ūkio užimamas naudingasis plotas? | — |
| `elect` | `integer` | `bool` | — | `open` | — | Ar būste yra: elektra | — |
| `bath` | `integer` | `bool` | — | `open` | — | Vonia dušas | — |
| `toilet` | `integer` | `bool` | — | `open` | — | Tualetas su nuleidžiamuoju vandeniu | — |
| `kitchen` | `integer` | `bool` | — | `open` | — | Atskira virtuvė | — |
| `phone` | `integer` | `bool` | — | `open` | — | Fiksuotojo ryšio telefonas | — |
| `water` | `integer` | — | — | `open` | — | Vandentiekis | — |
| `h_water` | `integer` | — | — | `open` | — | Karšto vandens tiekimas | — |
| `sewerage` | `integer` | — | — | `open` | — | Kanalizacija | — |
| `heating` | `integer` | — | — | `open` | — | Koks pagrindinis Jūsų būsto šildymo būdas? | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dwlowner` | `1` | — | — | Būstas priklauso namų ūkiui | — |
| `dwlowner` | `2` | — | — | Būstas priklauso kitam namų ūkiui ar įmonei | — |
| `dwlowner` | `3` | — | — | Būstas priklauso valstybei, savivaldybei | — |
| `formrent` | `1` | — | — | Mokėdamas rinkos kaina | — |
| `formrent` | `2` | — | — | Mokėdamas mažesne nei rinkos kaina | — |
| `formrent` | `3` | — | — | Nemokėdamas už nuomą | — |
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
| `phone` | `1` | — | — | Taip | — |
| `phone` | `2` | — | — | Ne | — |
| `phone` | `1` | — | — | Vyras | — |
| `phone` | `2` | — | — | Moteris | — |
| `water` | `1` | — | — | Taip, centrinis | — |
| `water` | `2` | — | — | Taip, vietinis | — |
| `water` | `3` | — | — | Ne | — |
| `h_water` | `1` | — | — | Taip, centrinis | — |
| `h_water` | `2` | — | — | Taip, vietinis | — |
| `h_water` | `3` | — | — | Ne | — |
| `sewerage` | `1` | — | — | Taip, centrinis | — |
| `sewerage` | `2` | — | — | Taip, vietinis | — |
| `sewerage` | `3` | — | — | Ne | — |
| `heating` | `1` | — | — | Centrinis šildymas iš šilumos tinklų | — |
| `heating` | `2` | — | — | Centrinis šildymas iš vietinio šilumos šaltinio | — |
| `heating` | `3` | — | — | Krosnis, židinys | — |
| `heating` | `4` | — | — | Nėra | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv
