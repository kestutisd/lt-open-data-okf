---
type: Dataset
title: "Informacija apie paimtus mėginius iš siuntų dėl genetinės modifikacijos nustatymo"
description: "Pateikiama informacija apie ŪS pavadinimą / vardą, pavardę, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų išvadą."
resource: "https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r32_gmo_nustatymas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1888/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/gmo_nustatymas"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Informacija apie paimtus mėginius iš siuntų dėl genetinės modifikacijos nustatymo

- **Namespace:** `datasets/gov/vat/gmo_nustatymas`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r32_gmo_nustatymas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1888/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/gmo_nustatymas`[^dcat]
- **Portal Title (`@lt`):** Informacija apie paimtus mėginius iš siuntų dėl genetinės modifikacijos nustatymo[^dcat]
- **Portal Title (`@en`):** Information on samples taken from consignments for the detection of genetic modification[^dcat]
- **Issued (`dct:issued`):** `2023-05-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-05-09` .. `2023-08-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie ŪS pavadinimą / vardą, pavardę, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų išvadą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information on the name of the UA, name, sample serial number, variety, category / class, lot number, lot weight (kg) / unit, crop area, ha, date of sampling, conclusion of test results[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Siunta](gmo_nustatymas/Siunta.md) | Pateikiama informacija apie ŪS pavadinimą, mėginio eilės Nr., veislę, kategoriją / klasę, siuntos Nr., siuntos svorį (kg) / vnt., pasėlio plotą, ha, mėginio ėmimo datą, tyrimų rezultatų išvadą. | `4` | `eil_nr` | `open` | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r32_gmo_nustatymas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r32_gmo_nustatymas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/gmo_nustatymas (https://data.gov.lt/datasets/1888/)
