---
type: Table
title: "GyvGeoTer1Km2020 — Gyventojų surašymo geoerdviniai duomenys 1x1 km gardelėse 2020 m."
description: "Spinta table datasets/gov/lsd/gyventojai_bustas/GyvGeoTer1Km2020 (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas/GyvGeoTer1Km2020"
tags: [gov, lsd, gyvgeoter1km2020, deployed, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L128"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L128"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1911/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# GyvGeoTer1Km2020 — Gyventojų surašymo geoerdviniai duomenys 1x1 km gardelėse 2020 m.

- **Model:** `datasets/gov/lsd/gyventojai_bustas/GyvGeoTer1Km2020`[^manifest]
- **Dataset:** [Lietuvos Respublikos visuotinio gyventojų ir būstų surašymo rezultatų duomenys](../gyventojai_bustas.md) (`datasets/gov/lsd/gyventojai_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gyventojai_bustas.csv#L128](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L128)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas/GyvGeoTer1Km2020` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DECENNIAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m00_15_` | `string` | — | `4` | `open` | — | 0–15 metų amžiaus moterų skaičius | — |
| `v00_15_` | `string` | — | `4` | `open` | — | 0–15 metų amžiaus vyrų skaičius | — |
| `gyv_sk_` | `string` | — | `4` | `open` | — | Gyventojų skaičius | — |
| `moterys_` | `string` | — | `4` | `open` | — | Moterų skaičius | — |
| `v65_` | `string` | — | `4` | `open` | — | 65 metų amžiaus ir vyresnių vyrų skaičius | — |
| `vyrai_` | `string` | — | `4` | `open` | — | Vyrų skaičius | — |
| `all65_` | `string` | — | `4` | `open` | — | 65 metų amžiaus ir vyresnių gyventojų skaičius | — |
| `grid_id` | `string` | — | `4` | `open` | — | Gardelės identifikavimo kodas | — |
| `m65_` | `string` | — | `4` | `open` | — | 65 metų amžiaus ir vyresnių moterų skaičius | — |
| `all16_64_` | `string` | — | `4` | `open` | — | 16–64 metų amžiaus gyventojų skaičius | — |
| `all00_15_` | `string` | — | `4` | `open` | — | 0–15 metų amžiaus gyventojų skaičius | — |
| `v16_64_` | `string` | — | `4` | `open` | — | 16–64 metų amžiaus vyrų skaičius | — |
| `shape_length` | `number` | — | `4` | `open` | — | gradelės ilgis | — |
| `m16_64_` | `string` | — | `4` | `open` | — | 16–64 metų amžiaus moterų skaičius | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikacinis numeris | — |
| `shape_area` | `number` | — | `4` | `open` | — | gardelės plotas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L128 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L128)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas (https://data.gov.lt/datasets/1911/)
