---
type: Table
title: "AstSutartis — Alytaus šilumos tinklų sutarčių su įmonėmis duomenys"
description: "Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro."
resource: "https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys/AstSutartis"
tags: [gov, ast, astsutartis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ast/imoniu_sutartys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2770/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ast/imoniu_sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AstSutartis — Alytaus šilumos tinklų sutarčių su įmonėmis duomenys

Lentelėje pateikti Alytaus šilumos tinklų sutarčių su įmonėmis duomenys iš Įmonių sutarčių registro. Duomenų turinys: įmonių JAR kodai, adresai, pavadinimai, tarp įmonių ir Alytaus šilumos tinklų sudarytų sutarčių pradžios datos. Svarbu paminėti, kad lentelėje nurodomas vienas juridinis asmuo (viena įmonė) gali turėti kelis skirtingus adresus, dėl to tas pats juridinis asmuo gali turėti ir kelis skirtingus kliento kodus. Kaupiamų duomenų aprėptis laike – nuo 1993 m., atnaujinant kas metus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ast/imoniu_sutartys/AstSutartis`[^manifest]
- **Dataset:** [Alytaus šilumos tinklų sutarčių su įmonėmis duomenys](../imoniu_sutartys.md) (`datasets/gov/ast/imoniu_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/ast/imoniu_sutartys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/imoniu_sutartys/AstSutartis` (`deployed`)[^manifest]
- **Provider:** `ast` — Alytaus šilumos tinklai *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/imoniu_sutartys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/imoniu_sutartys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ast/imoniu_sutartys (https://data.gov.lt/datasets/2770/)
