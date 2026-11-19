---
type: Table
title: "EriavedziuOzkavedziuPasiskirstymas — Ėriavedžių ir ožkavedžių laikytojų pasiskirstymas"
description: "Spinta table datasets/gov/zuikvc/eriavedes_ozkavedes/EriavedziuOzkavedziuPasiskirstymas (5 columns)."
tags: [gov, zuikvc, eriavedziuozkavedziupasiskirstymas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/eriavedes_ozkavedes.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/eriavedes_ozkavedes.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# EriavedziuOzkavedziuPasiskirstymas — Ėriavedžių ir ožkavedžių laikytojų pasiskirstymas

- **Model:** `datasets/gov/zuikvc/eriavedes_ozkavedes/EriavedziuOzkavedziuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/eriavedes_ozkavedes](../eriavedes_ozkavedes.md) (`datasets/gov/zuikvc/eriavedes_ozkavedes`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/eriavedes_ozkavedes.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/eriavedes_ozkavedes.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `eriavedes_laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko ėriavedes, skaičius | — |
| `eriavedes` | `integer` | `U` | `4` | `open` | — | Ėriavedžių skaičius | — |
| `ozkavedes_laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko ožkavedes, skaičius | — |
| `ozkavedes` | `integer` | `U` | `4` | `open` | — | Ožkavedžių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/eriavedes_ozkavedes.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/eriavedes_ozkavedes.csv#L8)
