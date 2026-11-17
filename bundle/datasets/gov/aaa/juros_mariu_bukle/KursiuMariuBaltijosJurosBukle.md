---
type: Table
title: "KursiuMariuBaltijosJurosBukle — Kuršių marių ir Baltijos jūros būklė"
description: "Spinta table datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_bukle.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_bukle.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# KursiuMariuBaltijosJurosBukle — Kuršių marių ir Baltijos jūros būklė

- **Model:** `datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle`[^manifest]
- **Dataset:** [datasets/gov/aaa/juros_mariu_bukle](../juros_mariu_bukle.md) (`datasets/gov/aaa/juros_mariu_bukle`)
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_bukle.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_bukle.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_pav` | `string` | — | `3` | `open` | — | Objekto, kuriam priklauso vandens telkiniai, pavadinimas | Objektai, kuriems priskiriami vandens telkiniai: Kuršių marios; Baltijos jūra |
| `telkinio_pav` | `string` | — | `3` | `open` | — | Vandens telkinio, kuriame vertinama būklė, pavadinimas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais vertinama telkinio būklė | — |
| `eko_bukle` | `string` | — | `3` | `open` | — | Vandens telkinio fizikinių-cheminių ir biologinių kokybės elementų vertinimo rezultatas | Ekologinė būklė/potencialas vertinama remiantis Lietuvos Respublikos aplinkos ministro įsakymu 2021 m. lapkričio 4 d. Nr. D1-645 "Dėl paviršinių vandens telkinių būklės nustatymo metodikos patvirtinimo" ir Lietuvos Respublikos aplinkos ministro įsakymu 2020 m lapkričio 9 d. Nr. D1-675 "Dėl Baltijos jūros rajono geros aplinkos būklės savybių nustatymo rekalavimų patvirtinimo". |
| `chem_bukle` | `string` | — | `3` | `open` | — | Vandens telkinio pavojingų, prioritetinių pavojingų ir kitų teršalų vertinimo rezultatas | Cheminė būklė vertinama remiantis Lietuvos Respulikos aplinkos ministro įsakymu 2020 m lapkričio 9 d. Nr. D1-675 "Dėl Baltijos jūros rajono geros aplinkos būklės savybių nustatymo rekalavimų patvirtinimo" ir Lietuvos Respublikos aplinkos ministro įsakymas 2022 m. balandžio 22 d. Nr. D1-109 "Dėl nuotekų tvarkymo reglamento patvirtinimo". |
| `rodikliai` | `string` | — | `2` | `open` | — | Rodikliai, kurie viršijo didžiausią leidžiamą koncentraciją arba aplinkos kokybės standartą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_bukle.csv
