---
type: Table
title: "Banda — Užregistruotų gyvulių bandų ataskaita"
description: "Spinta table datasets/gov/zuikvc/bandos/Banda (6 columns)."
tags: [gov, zuikvc, banda, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/bandos.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Banda — Užregistruotų gyvulių bandų ataskaita

- **Model:** `datasets/gov/zuikvc/bandos/Banda`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/bandos](../bandos.md) (`datasets/gov/zuikvc/bandos`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/bandos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `galviju_bandu_sk` | `integer` | `U` | `4` | `open` | — | Galvijų bandų skaičius | — |
| `aviu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Avių bandų skaičius | — |
| `ozku_bandu_sk` | `integer` | `U` | `4` | `open` | — | Ožkų bandų skaičius | — |
| `arkliu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Arklių bandų skaičius | — |
| `kiauliu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių bandų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/bandos.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos.csv#L8)
