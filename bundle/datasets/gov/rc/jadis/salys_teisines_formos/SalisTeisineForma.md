---
type: Table
title: "SalisTeisineForma — Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą"
description: "Spinta table datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/salys_teisines_formos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# SalisTeisineForma — Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą

- **Model:** `datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą](../salys_teisines_formos.md) (`datasets/gov/rc/jadis/salys_teisines_formos`)
- **Manifest CSV:** [datasets/gov/rc/jadis/salys_teisines_formos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma`
- **Primary Key (`ref`):** `laikotarpis, salies_kodas, forma`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laikotarpis` | `date` | `D` | `4` | `open` | — | Data, kuriai skaičiuojamas dalyvių skaičius (nuo 2015 m. sausio 1 d., periodiškumas - 1 metai) | — |
| `salies_kodas` | `string` | — | `5` | `open` | `locn:adminUnitL1` | Šalies kodas | — |
| `salies_pav` | `string` | — | `3` | `open` | — | Šalies pavadinimas | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../../jar/formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `uzs_fiz_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio fizinių asmenų skaičius | — |
| `uzs_ja_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio juridinių asmenų skaičius | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `locn` | `http://www.w3.org/ns/locn#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/salys_teisines_formos.csv
