---
type: Table
title: "GalvijuSkerdimas — Galvijų skerdimai"
description: "Spinta table datasets/gov/zuikvc/galviju_skerdimai/GalvijuSkerdimas (4 columns)."
tags: [gov, zuikvc, galvijuskerdimas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_skerdimai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galviju_skerdimai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuSkerdimas — Galvijų skerdimai

- **Model:** `datasets/gov/zuikvc/galviju_skerdimai/GalvijuSkerdimas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galviju_skerdimai](../galviju_skerdimai.md) (`datasets/gov/zuikvc/galviju_skerdimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/galviju_skerdimai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_skerdimai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `paskerstu_galviju_iki_1_sk` | `integer` | `U` | `4` | `open` | — | Paskerstų galvijų iki 1 metų amžiaus skaičius | — |
| `paskerstu_galviju_virs_30_sk` | `integer` | `U` | `4` | `open` | — | Paskerstų galvijų virš 30 mėnesių amžiaus skaičius | — |
| `paskerstu_galviju_sk` | `integer` | `U` | `4` | `open` | — | Paskerstų galvijų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `property` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galviju_skerdimai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_skerdimai.csv#L8)
