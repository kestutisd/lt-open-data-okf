---
type: Table
title: "Verte — Pateikiama informacija apie atlikto ūkinio vertingumo tyrimo duomenis."
description: "Spinta table datasets/gov/vat/saugomos_veisles/Verte (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/Verte"
tags: [gov, vat, verte, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L42"
    title: "atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L42"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1868/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Verte — Pateikiama informacija apie atlikto ūkinio vertingumo tyrimo duomenis.

- **Model:** `datasets/gov/vat/saugomos_veisles/Verte`[^manifest]
- **Dataset:** [Nacionalinis saugomų augalų veislių sąrašas, Lietuvos Respublikoje saugomų augalų veislių...](../saugomos_veisles.md) (`datasets/gov/vat/saugomos_veisles`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/saugomos_veisles.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L42)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/Verte` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `rusis` | `string` | — | `2` | `open` | — | Augalo rūšis | — |
| `stotis` | `string` | — | `4` | `open` | — | Augalų veislių tyrimo skyriaus pavadinimas | — |
| `veisle` | `string` | — | `2` | `open` | — | Veislės pavadinimas | Skliaustuose pateikiamas selekcinis veislės žymuo |
| `rodiklis_en` | `string` | — | `4` | `open` | — | Tyrimo rodiklio pavadinimas anglų kalba | — |
| `rodiklis_lt` | `string` | — | `4` | `open` | — | Tyrimo rodiklio pavadinimas | — |
| `palaikytojas` | `string` | — | `1` | `open` | — | Veislės palaikytojas | — |
| `metai` | `integer` | — | `2` | `open` | — | Derliaus metai | — |
| `reiksme` | `number` | — | `4` | `open` | — | Tyrimo rodiklio reikšmė | — |
| `standartine` | `boolean` | — | `4` | `open` | — | Nuoroda, ar augalų veislė yra standartinė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `stotis` | `"Kauno augalų veislių tyrimo skyrius"` | — | — | — | — |
| `stotis` | `"Pasvalio augalų veislių tyrimo skyrius"` | — | — | — | — |
| `stotis` | `"Plungės augalų veislių tyrimo skyrius"` | — | — | — | — |
| `stotis` | `"Utenos augalų veislių tyrimo skyrius"` | — | — | — | — |
| `stotis` | `"Rumokų bandymų stotis"` | — | — | — | — |
| `stotis` | `"Kaišiadorių augalų veislių tyrimo skyrius"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L42 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L42)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles (https://data.gov.lt/datasets/1868/)
