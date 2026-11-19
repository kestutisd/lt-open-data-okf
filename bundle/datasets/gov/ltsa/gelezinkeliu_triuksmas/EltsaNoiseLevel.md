---
type: Table
title: "EltsaNoiseLevel — Triukšmas pagrindiniuose geležinkelio keliuose ne aglomeracijos zonose"
description: "Spinta table datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel"
tags: [gov, ltsa, eltsanoiselevel, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2092/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_triuksmas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# EltsaNoiseLevel — Triukšmas pagrindiniuose geležinkelio keliuose ne aglomeracijos zonose

- **Model:** `datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel`[^manifest]
- **Dataset:** [Triukšmas pagrindiniuose geležinkelio keliuose ne aglomeracijos zonose](../gelezinkeliu_triuksmas.md) (`datasets/gov/ltsa/gelezinkeliu_triuksmas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/gelezinkeliu_triuksmas/EltsaNoiseLevel` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ctryid` | `string` | — | `4` | `open` | — | Valstybės kodas | — |
| `db_high` | `integer` | `dB` | `4` | `open` | — | Triukšmo viršutinė reikšmė | — |
| `db_low` | `integer` | `dB` | `4` | `open` | — | Triukšmo žemutinė reikšmė | — |
| `geom` | `geometry(multipolygonzm, 3346)` | — | `3` | `open` | — | Teritorija | — |
| `gid` | `integer` | — | `4` | `open` | — | ID | — |
| `group` | `string` | — | `3` | `open` | — | Grupė | — |
| `period` | `string` | — | `3` | `open` | — | Paros laikas | — |
| `year` | `integer` | — | `2` | `open` | — | Metai | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/gelezinkeliu_triuksmas.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/gelezinkeliu_triuksmas (https://data.gov.lt/datasets/2092/)
