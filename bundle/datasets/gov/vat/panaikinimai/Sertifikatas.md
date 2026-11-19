---
type: Table
title: "Sertifikatas — Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr."
description: "Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais"
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinimai/Sertifikatas"
tags: [gov, vat, sertifikatas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/panaikinimai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Sertifikatas — Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo...

**Dataset Context:** Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais[^manifest]

- **Model:** `datasets/gov/vat/panaikinimai/Sertifikatas`[^manifest]
- **Dataset:** [Informacija apie panaikintus sertifikatus, kurie skelbiami negaliojančiais](../panaikinimai.md) (`datasets/gov/vat/panaikinimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinimai/Sertifikatas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r24_panaikinti_sertifikatai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/panaikinimai (https://data.gov.lt/datasets/1880/)
