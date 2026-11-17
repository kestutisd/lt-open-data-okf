---
type: Table
title: "Leidimas — Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą laikotarpį (išdavimo data; leidimo numeris; būsena; ūkio..."
description: "Spinta table datasets/gov/vat/prekyba_aap/Leidimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/prekyba_aap/Leidimas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r10_prekyba_aap.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Pateikiama informacija apie išduotus, patikslintus ar panaikintus leidimus platinti augalų apsaugos produktus per tam tikrą laikotarpį (išdavimo data; leidimo numeris; būsena; ūkio...

- **Model:** `datasets/gov/vat/prekyba_aap/Leidimas`[^manifest]
- **Dataset:** [datasets/gov/vat/prekyba_aap](../prekyba_aap.md) (`datasets/gov/vat/prekyba_aap`)
- **Manifest CSV:** [datasets/gov/vat/r10_prekyba_aap.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r10_prekyba_aap.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/prekyba_aap/Leidimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r10_prekyba_aap.csv
