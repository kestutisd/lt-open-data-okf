---
type: Table
title: "BDalis — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų B dalies duomenys"
description: "Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/BDalis"
tags: [gov, vmi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# BDalis — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų B dalies duomenys

Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje. Iki 2022-06-30 deklaracijos B dalis naudota azartinių lošimų įrenginiams.

- **Model:** `datasets/gov/vmi/azartiniai_losimai/BDalis`[^manifest]
- **Dataset:** [Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys](../azartiniai_losimai.md) (`datasets/gov/vmi/azartiniai_losimai`)
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/BDalis`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `pirma` | `number` | — | `2` | `open` | — | Mokesčio B dalies ketvirčio pirmo mėnesio suma | — |
| `antra` | `number` | — | `2` | `open` | — | Mokesčio B dalies ketvirčio antro mėnesio suma | — |
| `trecia` | `number` | — | `2` | `open` | — | Mokesčio B dalies ketvirčio trečio mėnesio suma | — |
| `bendra` | `number` | — | `2` | `open` | — | Mokesčio B dalies bendra ketvirčių suma | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pirma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `antra` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `trecia` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `bendra` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv
