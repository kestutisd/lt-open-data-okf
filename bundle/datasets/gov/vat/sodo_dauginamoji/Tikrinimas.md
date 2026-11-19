---
type: Table
title: "Tikrinimas — Sodo augalų dauginamosios medžiagos tikrinimai"
description: "Spinta table datasets/gov/vat/sodo_dauginamoji/Tikrinimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/sodo_dauginamoji/Tikrinimas"
tags: [gov, vat, tikrinimas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r18_sodo_dm.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r18_sodo_dm.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1874/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/sodo_dauginamoji"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Tikrinimas — Sodo augalų dauginamosios medžiagos tikrinimai

- **Model:** `datasets/gov/vat/sodo_dauginamoji/Tikrinimas`[^manifest]
- **Dataset:** [Sodo augalų dauginamosios medžiagos tikrinimai](../sodo_dauginamoji.md) (`datasets/gov/vat/sodo_dauginamoji`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r18_sodo_dm.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r18_sodo_dm.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/sodo_dauginamoji/Tikrinimas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `gentis` | `string` | — | `3` | `open` | — | Gentis | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `aprobuota_augalu` | `number` | `U` | `4` | `open` | — | Aprobuota augalų iš viso | — |
| `isbrokuota` | `number` | `U` | `4` | `open` | — | Išbrokuota | — |
| `elitine_medziaga` | `number` | `U` | `4` | `open` | — | Pripažintos kategorijos elitinė medžiaga | — |
| `sertifikuota_medziaga` | `number` | `U` | `4` | `open` | — | Pripažintos kategorijos sertifikuota medžiaga | — |
| `super_elitine_medziaga` | `number` | `U` | `4` | `open` | — | Pripažintos kategorijos super elitinė medžiaga | — |
| `skiepugliu_ugliu_poskiepiu_daigai` | `number` | `U` | `4` | `open` | — | Skiepūglių, ūglių, poskiepių, daigų iš viso | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r18_sodo_dm.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r18_sodo_dm.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/sodo_dauginamoji (https://data.gov.lt/datasets/1874/)
