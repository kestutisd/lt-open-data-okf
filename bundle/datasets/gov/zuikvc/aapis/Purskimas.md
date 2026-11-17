---
type: Table
title: "Purskimas — Augalų apsaugos produktais purškiamų plotų ir augalų sėklų, apdorotų augalų apsaugos produktais, duomenys"
description: "Spinta table datasets/gov/zuikvc/aapis/Purskimas (10 columns)."
tags: [gov, zuikvc, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/aapis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aapis.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Purskimas — Augalų apsaugos produktais purškiamų plotų ir augalų sėklų, apdorotų augalų apsaugos produktais, duomenys

- **Model:** `datasets/gov/zuikvc/aapis/Purskimas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/aapis](../aapis.md) (`datasets/gov/zuikvc/aapis`)
- **Manifest CSV:** [datasets/gov/zuikvc/aapis.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aapis.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `numeris`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `busena` | `string` | — | `4` | `open` | — | Purškimo ar sėjos būsena | — |
| `numeris` | `integer` | — | `4` | `open` | — | Purškimo ar sėjos numeris | — |
| `lauko_plotas` | `number` | `ha` | `4` | `open` | — | Purškimo ar sėjos lauko plotas hektarais; | — |
| `panaudoto_aap_pavadinimas1` | `string` | — | `3` | `open` | — | Panaudoto augalų apsaugos produkto pavadinimas | — |
| `panaudoto_aap_pavadinimas2` | `string` | — | `3` | `open` | — | Panaudoto augalų apsaugos produkto pavadinimas | — |
| `panaudoto_aap_pavadinimas3` | `string` | — | `3` | `open` | — | Panaudoto augalų apsaugos produkto pavadinimas | — |
| `pradzia` | `datetime` | `T` | `4` | `open` | — | Purškimo ar sėjos pradžios data ir laikas | — |
| `pabaiga` | `datetime` | `T` | `4` | `open` | — | Purškimo ar sėjos pabaigos data ir laikas | — |
| `iregistruotas` | `datetime` | `S` | `4` | `open` | — | Purškimo įregistravimo data ir laikas. | Pildomas tik tiems purškimams ar sėjoms, kurių būsena yra registruota |
| `centro_koordinates` | `geometry(point,3346)` | — | `3` | `open` | — | Purškiamo ar sėjamo ploto erdviniai duomenys | Centro x,y koordinatės WKT formatu |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"P"` | — | — | Planuojamas | — |
| `busena` | `"R"` | — | — | Registruotas | — |
| `busena` | `"A"` | — | — | Atšauktas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/aapis.csv
