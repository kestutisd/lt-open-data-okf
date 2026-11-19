---
type: Table
title: "Bustas2008 — Būstas ir patogumai 2008m."
description: "Būsto tipas, namų ūkio užimamų kambarių skaičius, būsto plotas, patogumai."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Bustas2008"
tags: [gov, lsd, bustas2008, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Bustas2008 — Būstas ir patogumai 2008m.

Būsto tipas, namų ūkio užimamų kambarių skaičius, būsto plotas, patogumai.[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Bustas2008`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Bustas2008` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `dwlowner` | `integer` | — | — | `open` | — | Būsto nuosavybė | — |
| `loanhous` | `integer` | `enum: bool` | — | `open` | — | Ar paimta būsto paskola? | — |
| `formrent` | `integer` | — | — | `open` | — | Nuomojate butą (namą) | — |
| `dwltype` | `integer` | — | — | `open` | — | Gyvenamosios patalpos tipas | — |
| `dw_year` | `integer` | — | — | `open` | — | Namo pastatymo metai | — |
| `dw_other` | `integer` | — | — | `open` | — | Kitas nuosavas būstas | — |
| `elect` | `integer` | `enum: bool` | — | `open` | — | Elektra | — |
| `bath` | `integer` | `enum: bool` | — | `open` | — | Vonia, dušas | — |
| `toilet` | `integer` | `enum: bool` | — | `open` | — | Ar turite tualetą su nutekamuoju vandeniu | — |
| `kitchen` | `integer` | `enum: bool` | — | `open` | — | Atskira virtuvė | — |
| `garage` | `integer` | `enum: bool` | — | `open` | — | Garazas | — |
| `phone` | `integer` | `enum: bool` | — | `open` | — | Fiksuoto ryšio telefonas | — |
| `heating` | `integer` | — | — | `open` | — | Šildymas | — |
| `h_water` | `integer` | — | — | `open` | — | Karšto vandens tiekimas | — |
| `water` | `integer` | — | — | `open` | — | Vandentiekis | — |
| `sewerage` | `integer` | — | — | `open` | — | Kanalizacija | — |
| `liv_year` | `integer` | — | — | `open` | — | Kiek metų gyvenate šiame būste | — |
| `nrooms` | `integer` | — | — | `open` | — | Kambarių skaičius | — |
| `totarea` | `integer` | — | — | `open` | — | Bendras naudingas plotas | — |
| `rent` | `integer` | — | — | `open` | — | Už kiek išnuomotumėte butą | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dwlowner` | `1` | — | — | Yra šio būsto savininkas | — |
| `dwlowner` | `2` | — | — | Yra nuomininkas arba subnuomininkas, mokantis nuomą rinkos kaina | — |
| `dwlowner` | `3` | — | — | Nuomojasi šį būstą mažesne nei rinkos kaina | — |
| `dwlowner` | `4` | — | — | Gyvena nemokėdamas nuomos | — |
| `loanhous` | `1` | — | — | Taip | — |
| `loanhous` | `2` | — | — | Ne | — |
| `loanhous` | `1` | — | — | Vyras | — |
| `loanhous` | `2` | — | — | Moteris | — |
| `formrent` | `1` | — | — | Su baldais | — |
| `formrent` | `2` | — | — | Be baldų | — |
| `dwltype` | `1` | — | — | Atskiras šeimos namas | — |
| `dwltype` | `2` | — | — | Namo dalis, pusiau atskiras namas | — |
| `dwltype` | `3` | — | — | Butas daugiabučiame name | — |
| `dwltype` | `4` | — | — | Kita | — |
| `dw_year` | `1` | — | — | Iki 1946 m. | — |
| `dw_year` | `2` | — | — | 1946–1960 m | — |
| `dw_year` | `3` | — | — | 1961–1980 m. | — |
| `dw_year` | `4` | — | — | 1981–1995 m. | — |
| `dw_year` | `5` | — | — | 1996 ir vėliau | — |
| `dw_other` | `1` | — | — | Taip, Lietuvoje | — |
| `dw_other` | `2` | — | — | Taip, užsienyje | — |
| `dw_other` | `3` | — | — | Ne | — |
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
| `garage` | `1` | — | — | Taip | — |
| `garage` | `2` | — | — | Ne | — |
| `garage` | `1` | — | — | Vyras | — |
| `garage` | `2` | — | — | Moteris | — |
| `phone` | `1` | — | — | Taip | — |
| `phone` | `2` | — | — | Ne | — |
| `phone` | `1` | — | — | Vyras | — |
| `phone` | `2` | — | — | Moteris | — |
| `heating` | `1` | — | — | Taip, centrinis | — |
| `heating` | `2` | — | — | Taip, vietinis | — |
| `heating` | `3` | — | — | Ne | — |
| `h_water` | `1` | — | — | Taip, centrinis | — |
| `h_water` | `2` | — | — | Taip, vietinis | — |
| `h_water` | `3` | — | — | Ne | — |
| `water` | `1` | — | — | Taip, centrinis | — |
| `water` | `2` | — | — | Taip, vietinis | — |
| `water` | `3` | — | — | Ne | — |
| `sewerage` | `1` | — | — | Taip, centrinis | — |
| `sewerage` | `2` | — | — | Taip, vietinis | — |
| `sewerage` | `3` | — | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
