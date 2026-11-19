---
type: Table
title: "KursiuMariuBaltijosJurosBukle — Kuršių marių ir Baltijos jūros būklė"
description: "Spinta table datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle"
tags: [gov, aaa, kursiumariubaltijosjurosbukle, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_bukle.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_bukle.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1791/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_bukle"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# KursiuMariuBaltijosJurosBukle — Kuršių marių ir Baltijos jūros būklė

- **Model:** `datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle`[^manifest]
- **Dataset:** [Kuršių marių ir Baltijos jūros būklės duomenys](../juros_mariu_bukle.md) (`datasets/gov/aaa/juros_mariu_bukle`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_bukle.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_bukle.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_bukle/KursiuMariuBaltijosJurosBukle` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_bukle.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_bukle.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_bukle (https://data.gov.lt/datasets/1791/)
