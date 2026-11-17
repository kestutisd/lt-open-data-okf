---
type: Table
title: "Lova — Faktinis PSDF biudžeto lėšomis finansuojamų paliatyvios pagalbos, slaugos ir palaikomojo gydymo lovų skaičius"
description: "Informacija apie faktinį PSDF biudžeto lėšomis finansuojamų lovų skaičių pagal savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/vlk/faktines_lovos/Lova"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/faktines_lovos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/faktines_lovos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lova — Faktinis PSDF biudžeto lėšomis finansuojamų paliatyvios pagalbos, slaugos ir palaikomojo gydymo lovų skaičius

Informacija apie faktinį PSDF biudžeto lėšomis finansuojamų lovų skaičių pagal savivaldybes

- **Model:** `datasets/gov/vlk/faktines_lovos/Lova`[^manifest]
- **Dataset:** [datasets/gov/vlk/faktines_lovos](../faktines_lovos.md) (`datasets/gov/vlk/faktines_lovos`)
- **Manifest CSV:** [datasets/gov/vlk/faktines_lovos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/faktines_lovos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/faktines_lovos/Lova`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `savivaldybe` | `string` | — | `3` | `open` | — | Savivaldybė | — |
| `jar` | `integer` | — | `2` | `open` | — | Įstaiga iš juridinių asmenų registro | — |
| `tipas` | `string` | — | `3` | `open` | — | Lovos tipas | — |
| `lovu_sk` | `number` | `U` | `4` | `open` | — | Finansuojamų lovų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date, ref: "Y")"` | `type` | `4` | `open` | — | — | — |
| `jar` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/faktines_lovos.csv
