---
type: Table
title: "UzsienioAsmuo — Juridinių asmenų dalyvių duomenys apie užsienio fizinius ir juridinius asmenis"
description: "Spinta table datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/uzsienio_asmenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# UzsienioAsmuo — Juridinių asmenų dalyvių duomenys apie užsienio fizinius ir juridinius asmenis

- **Model:** `datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys apie užsienio fizinius ir juridinius asmenis](../uzsienio_asmenys.md) (`datasets/gov/rc/jadis/uzsienio_asmenys`)
- **Manifest CSV:** [datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo`
- **Primary Key (`ref`):** `laikotarpis, salies_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laikotarpis` | `date` | `D` | `4` | `open` | — | Data, kuriai skaičiuojamas dalyvių skaičius (nuo 2015 m. sausio 1 d., periodiškumas - 1 metai) | — |
| `salies_kodas` | `string` | — | `5` | `open` | `locn:adminUnitL1` | Šalies kodas | — |
| `sal_pav` | `string` | — | `3` | `open` | — | Šalies pavadinimas | — |
| `uzs_fiz_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniuose asmenyse dalyvaujančių skirtingų užsienio fizinių asmenų skaičius | — |
| `uzs_ja_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniuose asmenyse dalyvaujančių skirtingų užsienio juridinių asmenų skaičius | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `locn` | `http://www.w3.org/ns/locn#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/uzsienio_asmenys.csv
