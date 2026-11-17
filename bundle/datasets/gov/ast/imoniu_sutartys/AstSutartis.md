---
type: Table
title: "AstSutartis — Alytaus šilumos tinklų sutarčių su įmonėmis duomenys"
description: "Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro."
resource: "https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys/AstSutartis"
tags: [gov, ast, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ast/imoniu_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AstSutartis — Alytaus šilumos tinklų sutarčių su įmonėmis duomenys

Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro. Duomenų turinys: įmonių JAR kodai, adresai, pavadinimai, tarp įmonių ir Alytaus šilumos tinklų sudarytų sutarčių pradžios datos. Svarbu paminėti, kad lentelėje nurodomas vienas juridinis asmuo (viena įmonė) gali turėti kelis skirtingus adresus, dėl to tas pats juridinis asmuo gali turėti ir kelis skirtingus kliento kodus.

Kaupiamų duomenų aprėptis laike – nuo 1993 m., atnaujinant kas metus.

- **Model:** `datasets/gov/ast/imoniu_sutartys/AstSutartis`[^manifest]
- **Dataset:** [Alytaus šilumos tinklų sutarčių su įmonėmis duomenys](../imoniu_sutartys.md) (`datasets/gov/ast/imoniu_sutartys`)
- **Manifest CSV:** [datasets/gov/ast/imoniu_sutartys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys/AstSutartis`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `kliento_kodas` | `string` | — | `4` | `open` | — | Kliento kodas | — |
| `imones_jar_kodas` | `string` | — | `4` | `open` | — | Įmonės juridinio asmens kodas | — |
| `imones_adresas` | `string` | — | `4` | `open` | — | Įmonės adresas | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `sutarties_data` | `date` | `D` | `4` | `open` | — | Sutarties pradžios data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `imones_jar_kodas` | `create(property: "ja_kodas", type: "ref", ref: "datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/imoniu_sutartys.csv
