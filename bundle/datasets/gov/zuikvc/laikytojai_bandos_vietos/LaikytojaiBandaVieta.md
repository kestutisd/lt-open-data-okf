---
type: Table
title: "LaikytojaiBandaVieta — Laikytojų, bandų ir laikymo vietų skaičius"
description: "Spinta table datasets/gov/zuikvc/laikytojai_bandos_vietos/LaikytojaiBandaVieta (4 columns)."
tags: [gov, zuikvc, laikytojaibandavieta, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaikytojaiBandaVieta — Laikytojų, bandų ir laikymo vietų skaičius

- **Model:** `datasets/gov/zuikvc/laikytojai_bandos_vietos/LaikytojaiBandaVieta`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/laikytojai_bandos_vietos](../laikytojai_bandos_vietos.md) (`datasets/gov/zuikvc/laikytojai_bandos_vietos`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `laikytoju_skaicius` | `integer` | `U` | `4` | `open` | — | Laikytojų skaičius | — |
| `bandu_skaicius` | `integer` | `U` | `4` | `open` | — | Bandų skaičius | — |
| `laikymo_vietu_skaicius` | `integer` | `U` | `4` | `open` | — | Laikymo vietų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8)
