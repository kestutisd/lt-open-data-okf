---
type: Table
title: "Subjektas — Pateikiama informacija (adresas, pavadinimas) apie ūkio subjektus, kurių darbuotojams suteikta teisė imti sėklos mėginius iš sėklos siuntų."
description: "Spinta table datasets/gov/vat/seklu_emejai/Subjektas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/seklu_emejai/Subjektas"
tags: [gov, vat, subjektas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_emejai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/seklu_emejai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1871/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/seklu_emejai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Subjektas — Pateikiama informacija (adresas, pavadinimas) apie ūkio subjektus, kurių darbuotojams suteikta teisė imti sėklos mėginius iš...

- **Model:** `datasets/gov/vat/seklu_emejai/Subjektas`[^manifest]
- **Dataset:** [Įgaliotieji sėklų mėginių ėmėjai](../seklu_emejai.md) (`datasets/gov/vat/seklu_emejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/seklu_emejai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_emejai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/seklu_emejai/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `emejo_kodas` | `string` | — | `4` | `open` | — | Ėmėjo kodas | — |
| `darbo_vieta` | `string` | — | `2` | `open` | — | Ėmėjo darbo vieta | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Darbo vietos koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `darbo_vieta` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/seklu_emejai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_emejai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/seklu_emejai (https://data.gov.lt/datasets/1871/)
