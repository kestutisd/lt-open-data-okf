---
type: Table
title: "Subjektas — Pateikiama informacija (adresas, pavadinimas) apie ūkio subjektus, kurių darbuotojams suteikta teisė imti sėklos mėginius iš sėklos siuntų."
description: "Spinta table datasets/gov/vat/seklu_emejai/Subjektas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/seklu_emejai/Subjektas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/seklu_emejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_emejai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Pateikiama informacija (adresas, pavadinimas) apie ūkio subjektus, kurių darbuotojams suteikta teisė imti sėklos mėginius iš sėklos siuntų.

- **Model:** `datasets/gov/vat/seklu_emejai/Subjektas`[^manifest]
- **Dataset:** [datasets/gov/vat/seklu_emejai](../seklu_emejai.md) (`datasets/gov/vat/seklu_emejai`)
- **Manifest CSV:** [datasets/gov/vat/seklu_emejai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_emejai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/seklu_emejai/Subjektas`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/seklu_emejai.csv
