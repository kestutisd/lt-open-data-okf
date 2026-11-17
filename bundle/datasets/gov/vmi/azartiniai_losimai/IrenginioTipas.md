---
type: Table
title: "IrenginioTipas — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų įrenginio tipai"
description: "Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/IrenginioTipas"
tags: [gov, vmi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L49"
    last_modified: "2026-11-11T14:39:20Z"
---

# IrenginioTipas — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų įrenginio tipai

Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje.

- **Model:** `datasets/gov/vmi/azartiniai_losimai/IrenginioTipas`[^manifest]
- **Dataset:** [Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys](../azartiniai_losimai.md) (`datasets/gov/vmi/azartiniai_losimai`)
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L49](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L49)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/IrenginioTipas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `irenginio_tipas` | `integer` | — | `4` | `open` | — | Įrenginio tipas | — |
| `pirmas` | `integer` | `U` | `4` | `open` | — | Įrenginių skaičius sausio, balandžio, liepos, spalio mėnesiais | Ketvirčio pirmo mėnesio įrenginių skaičius |
| `antras` | `integer` | `U` | `4` | `open` | — | Įrenginių skaičius vasario, gegužės, rugpjūčio, lapkričio mėnesiais | Ketvirčio antro mėnesio įrenginių skaičius |
| `trecias` | `integer` | `U` | `4` | `open` | — | Įrenginių skaičius kovo, birželio, rugsėjo, gruodžio mėnesiais | Ketvirčio trečio mėnesio įrenginių skaičius |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `irenginio_tipas` | `1` | — | — | A kategorijos lošimų automatai | — |
| `irenginio_tipas` | `2` | — | — | B kategorijos lošimų automatai | — |
| `irenginio_tipas` | `3` | — | — | Ruletė | — |
| `irenginio_tipas` | `4` | — | — | Kortų stalai | — |
| `irenginio_tipas` | `5` | — | — | Kauliukų stalai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv
