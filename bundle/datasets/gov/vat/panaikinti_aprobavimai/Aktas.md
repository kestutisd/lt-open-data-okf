---
type: Table
title: "Aktas"
description: "Spinta table datasets/gov/vat/panaikinti_aprobavimai/Aktas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai/Aktas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/panaikinti_aprobavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Aktas

- **Model:** `datasets/gov/vat/panaikinti_aprobavimai/Aktas`[^manifest]
- **Dataset:** [datasets/gov/vat/panaikinti_aprobavimai](../panaikinti_aprobavimai.md) (`datasets/gov/vat/panaikinti_aprobavimai`)
- **Manifest CSV:** [datasets/gov/vat/panaikinti_aprobavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai/Aktas`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | `Eilės numeris` | — | — |
| `tiekejas` | `string` | — | `2` | `open` | `Tiekėjas` | — | — |
| `dokumentas` | `string` | — | `3` | `open` | `Dokumento tipas` | — | — |
| `data` | `date` | `D` | `4` | `open` | `Dokumento data` | — | — |
| `rusis` | `string` | — | `3` | `open` | `Augalo rūšis` | — | — |
| `veisle` | `string` | — | `4` | `open` | `Augalo veislė` | — | — |
| `panaikinimas` | `date` | `D` | `4` | `open` | `Panaikinimo data` | — | — |
| `pastabos` | `string` | — | `2` | `open` | `Pastabos (vietoj panaikinto, išduoto dokumento data ir Nr.)` | — | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | `Tiekėjo vietos koordinatės (LKS)` | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tiekejas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/panaikinti_aprobavimai.csv
