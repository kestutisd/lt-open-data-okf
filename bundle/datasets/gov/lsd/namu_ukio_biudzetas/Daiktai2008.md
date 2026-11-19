---
type: Table
title: "Daiktai2008 — Ilgalaikio naudojimo prietaisai 2008m."
description: "Namų ūkis turi/neturi ilgalaikio naudojimo prietaisus"
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Daiktai2008"
tags: [gov, lsd, daiktai2008, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L61"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L61"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Daiktai2008 — Ilgalaikio naudojimo prietaisai 2008m.

Namų ūkis turi/neturi ilgalaikio naudojimo prietaisus[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Daiktai2008`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L61)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Daiktai2008` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `p8tn_1` | `integer` | `enum: bool` | — | `open` | — | Kultūros ir poilsio daiktai | — |
| `p8_1` | `integer` | `enum: bool` | — | `open` | — | 1.Spalvotas TV | — |
| `p8_1a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_2` | `integer` | `enum: bool` | — | `open` | — | 2.Nespalvotas TV | — |
| `p8_2a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_3` | `integer` | `enum: bool` | — | `open` | — | 3.Vaizdo magnetofonas, DVD grotuvas, namų kinas | — |
| `p8_3a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_4` | `integer` | `enum: bool` | — | `open` | — | 4.Muzikos centras | — |
| `p8_4a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_5` | `integer` | `enum: bool` | — | `open` | — | 5.Mobilusis telefonas | — |
| `p8_5a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_6` | `integer` | `enum: bool` | — | `open` | — | 6.Kompiuteris | — |
| `p8_6a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8tn_2` | `integer` | `enum: bool` | — | `open` | — | Buitiniai prietaisai | — |
| `p8_8` | `integer` | `enum: bool` | — | `open` | — | 8.Šaldytuvas | — |
| `p8_8a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_9` | `integer` | `enum: bool` | — | `open` | — | 9.Šaldiklis | — |
| `p8_9a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_10` | `integer` | `enum: bool` | — | `open` | — | 10.Automatinė skalbimo mašina | — |
| `p8_10a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_11` | `integer` | `enum: bool` | — | `open` | — | 11.Mechaninė skalbimo mašina | — |
| `p8_11a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_12` | `integer` | `enum: bool` | — | `open` | — | 12.Dulkių siurblys | — |
| `p8_12a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_13` | `integer` | `enum: bool` | — | `open` | — | 13.Mikrobangų krosnelė | — |
| `p8_13a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_14` | `integer` | `enum: bool` | — | `open` | — | 14.Indų plovimo mašina | — |
| `p8_14a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8tn_3` | `integer` | `enum: bool` | — | `open` | — | Transporto priemonės | — |
| `p8_15` | `integer` | `enum: bool` | — | `open` | — | 15.Dviratis (išskyrus vaikišką) | — |
| `p8_15a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_16` | `integer` | `enum: bool` | — | `open` | — | 16.Mopedas, motociklas, motoroleris | — |
| `p8_16a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |
| `p8_17` | `integer` | `enum: bool` | — | `open` | — | 17.Automobilis, mikroautobusas | — |
| `p8_17a` | `integer` | — | — | `open` | — | Prietaisų skaičius namų ūkyje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `p8tn_1` | `1` | — | — | Taip | — |
| `p8tn_1` | `2` | — | — | Ne | — |
| `p8tn_1` | `1` | — | — | Vyras | — |
| `p8tn_1` | `2` | — | — | Moteris | — |
| `p8_1` | `1` | — | — | Taip | — |
| `p8_1` | `2` | — | — | Ne | — |
| `p8_1` | `1` | — | — | Vyras | — |
| `p8_1` | `2` | — | — | Moteris | — |
| `p8_2` | `1` | — | — | Taip | — |
| `p8_2` | `2` | — | — | Ne | — |
| `p8_2` | `1` | — | — | Vyras | — |
| `p8_2` | `2` | — | — | Moteris | — |
| `p8_3` | `1` | — | — | Taip | — |
| `p8_3` | `2` | — | — | Ne | — |
| `p8_3` | `1` | — | — | Vyras | — |
| `p8_3` | `2` | — | — | Moteris | — |
| `p8_4` | `1` | — | — | Taip | — |
| `p8_4` | `2` | — | — | Ne | — |
| `p8_4` | `1` | — | — | Vyras | — |
| `p8_4` | `2` | — | — | Moteris | — |
| `p8_5` | `1` | — | — | Taip | — |
| `p8_5` | `2` | — | — | Ne | — |
| `p8_5` | `1` | — | — | Vyras | — |
| `p8_5` | `2` | — | — | Moteris | — |
| `p8_6` | `1` | — | — | Taip | — |
| `p8_6` | `2` | — | — | Ne | — |
| `p8_6` | `1` | — | — | Vyras | — |
| `p8_6` | `2` | — | — | Moteris | — |
| `p8tn_2` | `1` | — | — | Taip | — |
| `p8tn_2` | `2` | — | — | Ne | — |
| `p8tn_2` | `1` | — | — | Vyras | — |
| `p8tn_2` | `2` | — | — | Moteris | — |
| `p8_8` | `1` | — | — | Taip | — |
| `p8_8` | `2` | — | — | Ne | — |
| `p8_8` | `1` | — | — | Vyras | — |
| `p8_8` | `2` | — | — | Moteris | — |
| `p8_9` | `1` | — | — | Taip | — |
| `p8_9` | `2` | — | — | Ne | — |
| `p8_9` | `1` | — | — | Vyras | — |
| `p8_9` | `2` | — | — | Moteris | — |
| `p8_10` | `1` | — | — | Taip | — |
| `p8_10` | `2` | — | — | Ne | — |
| `p8_10` | `1` | — | — | Vyras | — |
| `p8_10` | `2` | — | — | Moteris | — |
| `p8_11` | `1` | — | — | Taip | — |
| `p8_11` | `2` | — | — | Ne | — |
| `p8_11` | `1` | — | — | Vyras | — |
| `p8_11` | `2` | — | — | Moteris | — |
| `p8_12` | `1` | — | — | Taip | — |
| `p8_12` | `2` | — | — | Ne | — |
| `p8_12` | `1` | — | — | Vyras | — |
| `p8_12` | `2` | — | — | Moteris | — |
| `p8_13` | `1` | — | — | Taip | — |
| `p8_13` | `2` | — | — | Ne | — |
| `p8_13` | `1` | — | — | Vyras | — |
| `p8_13` | `2` | — | — | Moteris | — |
| `p8_14` | `1` | — | — | Taip | — |
| `p8_14` | `2` | — | — | Ne | — |
| `p8_14` | `1` | — | — | Vyras | — |
| `p8_14` | `2` | — | — | Moteris | — |
| `p8tn_3` | `1` | — | — | Taip | — |
| `p8tn_3` | `2` | — | — | Ne | — |
| `p8tn_3` | `1` | — | — | Vyras | — |
| `p8tn_3` | `2` | — | — | Moteris | — |
| `p8_15` | `1` | — | — | Taip | — |
| `p8_15` | `2` | — | — | Ne | — |
| `p8_15` | `1` | — | — | Vyras | — |
| `p8_15` | `2` | — | — | Moteris | — |
| `p8_16` | `1` | — | — | Taip | — |
| `p8_16` | `2` | — | — | Ne | — |
| `p8_16` | `1` | — | — | Vyras | — |
| `p8_16` | `2` | — | — | Moteris | — |
| `p8_17` | `1` | — | — | Taip | — |
| `p8_17` | `2` | — | — | Ne | — |
| `p8_17` | `1` | — | — | Vyras | — |
| `p8_17` | `2` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L61 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L61)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
