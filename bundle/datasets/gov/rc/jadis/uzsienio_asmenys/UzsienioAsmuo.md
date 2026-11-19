---
type: Table
title: "UzsienioAsmuo — Juridinių asmenų dalyvių duomenys apie užsienio fizinius ir juridinius asmenis"
description: "Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie užsienio fizinius ir juridinius asmenis."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo"
tags: [gov, rc, uzsienioasmuo, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1734/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/uzsienio_asmenys"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# UzsienioAsmuo — Juridinių asmenų dalyvių duomenys apie užsienio fizinius ir juridinius asmenis

**Dataset Context:** Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie užsienio fizinius ir juridinius asmenis.[^manifest]

- **Model:** `datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys apie užsienio fizinius ir juridinius asmenis](../uzsienio_asmenys.md) (`datasets/gov/rc/jadis/uzsienio_asmenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/uzsienio_asmenys/UzsienioAsmuo` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `laikotarpis, salies_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/uzsienio_asmenys.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/uzsienio_asmenys (https://data.gov.lt/datasets/1734/)
