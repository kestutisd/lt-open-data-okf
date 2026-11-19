---
type: Table
title: "Aktas"
description: "Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr."
resource: "https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai/Aktas"
tags: [gov, vat, aktas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/panaikinti_aprobavimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1886/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/panaikinti_aprobavimai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Aktas

**Dataset Context:** Pateikiami duomenys apie tiekėją, dokumento pavadinimą, dokumento Nr. ir datą, augalo rūšį, veislę, dokumento panaikinimo datą, naujai išduoto dokumento datą ir Nr.[^manifest]

- **Model:** `datasets/gov/vat/panaikinti_aprobavimai/Aktas`[^manifest]
- **Dataset:** [Informacija apie panaikintus aprobavimo aktus, kurie skelbiami negaliojančiais](../panaikinti_aprobavimai.md) (`datasets/gov/vat/panaikinti_aprobavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/panaikinti_aprobavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/panaikinti_aprobavimai/Aktas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tiekejas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/panaikinti_aprobavimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/panaikinti_aprobavimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/panaikinti_aprobavimai (https://data.gov.lt/datasets/1886/)
