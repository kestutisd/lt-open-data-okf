---
type: Table
title: "BanduGyvuliuSkaicius — Registruotų bandų ir gyvūlių skaičius savivaldybėse"
description: "Spinta table datasets/gov/zuikvc/bandos_gyvuliai/BanduGyvuliuSkaicius (9 columns)."
tags: [gov, zuikvc, bandugyvuliuskaicius, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos_gyvuliai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/bandos_gyvuliai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# BanduGyvuliuSkaicius — Registruotų bandų ir gyvūlių skaičius savivaldybėse

- **Model:** `datasets/gov/zuikvc/bandos_gyvuliai/BanduGyvuliuSkaicius`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/bandos_gyvuliai](../bandos_gyvuliai.md) (`datasets/gov/zuikvc/bandos_gyvuliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/bandos_gyvuliai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos_gyvuliai.csv#L8)[^manifest]
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
| `galviju_sk` | `integer` | `U` | `4` | `open` | — | Galvijų skaičius | — |
| `aviu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Avių bandų skaičius | — |
| `aviu_sk` | `integer` | `U` | `4` | `open` | — | Avių skaičius | — |
| `ozku_bandu_sk` | `integer` | `U` | `4` | `open` | — | Ožkų bandų skaičius | — |
| `ozku_sk` | `integer` | `U` | `4` | `open` | — | Ožkų skaičius | — |
| `arkliu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Arklių bandų skaičius | — |
| `arkliu_sk` | `integer` | `U` | `4` | `open` | — | Arklių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/bandos_gyvuliai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos_gyvuliai.csv#L8)
