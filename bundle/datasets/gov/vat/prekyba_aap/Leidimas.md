---
type: Table
title: "Leidimas — Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą laikotarpį (išdavimo data; leidimo numeris; būsena; ūkio subjekto pavadinimas, adresas)"
description: "Spinta table datasets/gov/vat/prekyba_aap/Leidimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/prekyba_aap/Leidimas"
tags: [gov, vat, leidimas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r10_prekyba_aap.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1866/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/prekyba_aap"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Leidimas — Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą...

- **Model:** `datasets/gov/vat/prekyba_aap/Leidimas`[^manifest]
- **Dataset:** [Leidimai platinti augalų apsaugos produktus](../prekyba_aap.md) (`datasets/gov/vat/prekyba_aap`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r10_prekyba_aap.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/prekyba_aap/Leidimas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Išdavimo data | — |
| `zyme` | `string` | — | `3` | `open` | — | Būsenos žymė | — |
| `gavejas` | `string` | — | `1` | `open` | — | Leidimo gavėjas | — |
| `kodas` | `string` | — | `2` | `open` | — | Gavėjo įmonės kodas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Gavėjo vietos koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `create(property: "imone", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |
| `kodas` | `update(property: "imone.ja_kodas", type: "")` | `property` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r10_prekyba_aap.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/prekyba_aap (https://data.gov.lt/datasets/1866/)
