---
type: Table
title: "Lova — Faktinis PSDF biudžeto lėšomis finansuojamų paliatyvios pagalbos, slaugos ir palaikomojo gydymo lovų skaičius"
description: "Informacija apie faktinį PSDF biudžeto lėšomis finansuojamų lovų skaičių pagal savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/vlk/faktines_lovos/Lova"
tags: [gov, vlk, lova, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/faktines_lovos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/faktines_lovos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1796/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/faktines_lovos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lova — Faktinis PSDF biudžeto lėšomis finansuojamų paliatyvios pagalbos, slaugos ir palaikomojo gydymo lovų skaičius

Informacija apie faktinį PSDF biudžeto lėšomis finansuojamų lovų skaičių pagal savivaldybes[^manifest]

- **Model:** `datasets/gov/vlk/faktines_lovos/Lova`[^manifest]
- **Dataset:** [Faktinis PSDF biudžeto lėšomis kompensuojamųjų paliatyvios pagalbos, slaugos ir palaikomojo...](../faktines_lovos.md) (`datasets/gov/vlk/faktines_lovos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/faktines_lovos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/faktines_lovos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/faktines_lovos/Lova` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/faktines_lovos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/faktines_lovos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/faktines_lovos (https://data.gov.lt/datasets/1796/)
