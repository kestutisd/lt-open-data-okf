---
type: Table
title: "TeisineForma — Juridinių asmenų dalyvių duomenys pagal juridinio asmens teisinę formą"
description: "Spinta table datasets/gov/rc/jadis/teisines_formos/TeisineForma (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/teisines_formos/TeisineForma"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/teisines_formos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/teisines_formos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TeisineForma — Juridinių asmenų dalyvių duomenys pagal juridinio asmens teisinę formą

- **Model:** `datasets/gov/rc/jadis/teisines_formos/TeisineForma`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys pagal juridinio asmens teisinę formą](../teisines_formos.md) (`datasets/gov/rc/jadis/teisines_formos`)
- **Manifest CSV:** [datasets/gov/rc/jadis/teisines_formos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/teisines_formos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/teisines_formos/TeisineForma`
- **Primary Key (`ref`):** `laikotarpis, forma`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laikotarpis` | `date` | `D` | `4` | `open` | — | Data, kuriai skaičiuojamas dalyvių skaičius (nuo 2015 m. sausio 1 d., periodiškumas - 1 metai) | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../../jar/formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `fiz_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių fizinių asmenų skaičius | — |
| `ja_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių juridinių asmenų skaičius | — |
| `uzs_fiz_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio fizinių asmenų skaičius | — |
| `uzs_ja_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio juridinių asmenų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/teisines_formos.csv
