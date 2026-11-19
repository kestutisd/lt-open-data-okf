---
type: Table
title: "Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų išvadą."
description: "Spinta table datasets/gov/vat/seklu_mainai/Siunta (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/seklu_mainai/Siunta"
tags: [gov, vat, siunta, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r26_seklu_mainai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r26_seklu_mainai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1882/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/seklu_mainai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Siunta — Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) /...

- **Model:** `datasets/gov/vat/seklu_mainai/Siunta`[^manifest]
- **Dataset:** [Informacija apie daržovių sėklos perdavimus / mainus](../seklu_mainai.md) (`datasets/gov/vat/seklu_mainai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r26_seklu_mainai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r26_seklu_mainai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/seklu_mainai/Siunta` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `rusis` | `string` | — | `3` | `open` | — | Asmens nurodyta augalo rūšis | — |
| `veisle` | `string` | — | `3` | `open` | — | Asmens nurodyta augalo veislė | — |
| `kiekis` | `number` | `g` | `4` | `open` | — | Sėklos kiekis, g | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "metai", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r26_seklu_mainai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r26_seklu_mainai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/seklu_mainai (https://data.gov.lt/datasets/1882/)
