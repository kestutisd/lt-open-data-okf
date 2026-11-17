---
type: Table
title: "Sertifikatas — Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr."
description: "Spinta table datasets/gov/vat/panaikinimai/Sertifikatas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinimai/Sertifikatas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sertifikatas — Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr.

- **Model:** `datasets/gov/vat/panaikinimai/Sertifikatas`[^manifest]
- **Dataset:** [datasets/gov/vat/panaikinimai](../panaikinimai.md) (`datasets/gov/vat/panaikinimai`)
- **Manifest CSV:** [datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinimai/Sertifikatas`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `tiekejas` | `string` | — | `2` | `open` | — | Tiekėjo vardas, pavardė / pavadinimas | — |
| `dokumentas` | `string` | — | `3` | `open` | — | Dokumento pavadinimas | — |
| `data` | `string` | — | `2` | `open` | — | Dokumento data ir Nr. | — |
| `rusis` | `string` | — | `3` | `open` | — | Augalo rūšis | — |
| `veisle` | `string` | — | `3` | `open` | — | Veislė | — |
| `panaikinimas` | `date` | `D` | `4` | `open` | — | Panaikinimo data | — |
| `pastaba` | `string` | — | `2` | `open` | — | Pastabos (vietoj jo išduoto dokumento data ir Nr.) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tiekejas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv
