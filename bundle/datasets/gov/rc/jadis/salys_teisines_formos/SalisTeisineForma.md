---
type: Table
title: "SalisTeisineForma — Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą"
description: "Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinio asmens dalyvių šalis ir juridinio asmens teisinę formą"
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma"
tags: [gov, rc, salisteisineforma, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/salys_teisines_formos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1733/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/salys_teisines_formos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# SalisTeisineForma — Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą

**Dataset Context:** Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinio asmens dalyvių šalis ir juridinio asmens teisinę formą[^manifest]

- **Model:** `datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys pagal juridinio asmens dalyvių šalis ir teisinę formą](../salys_teisines_formos.md) (`datasets/gov/rc/jadis/salys_teisines_formos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/salys_teisines_formos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/salys_teisines_formos/SalisTeisineForma` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `laikotarpis, salies_kodas, forma`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laikotarpis` | `date` | `D` | `4` | `open` | — | Data, kuriai skaičiuojamas dalyvių skaičius (nuo 2015 m. sausio 1 d., periodiškumas - 1 metai) | — |
| `salies_kodas` | `string` | — | `5` | `open` | `locn:adminUnitL1` | Šalies kodas | — |
| `salies_pav` | `string` | — | `3` | `open` | — | Šalies pavadinimas | — |
| `forma` | `ref` | [Forma](../../jar/formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `uzs_fiz_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio fizinių asmenų skaičius | — |
| `uzs_ja_dalyviai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio juridinių asmenų skaičius | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `locn` | `http://www.w3.org/ns/locn#` |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/salys_teisines_formos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/salys_teisines_formos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/salys_teisines_formos (https://data.gov.lt/datasets/1733/)
