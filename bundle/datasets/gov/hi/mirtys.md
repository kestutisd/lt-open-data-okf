---
type: Dataset
title: "Nuolatinių Lietuvos gyventojų, mirusių Lietuvoje ar užsienyje, mirties atvejų ir jų priežasčių duomenys"
description: "Pateikiami mirusių nuolatinių Lietuvos gyventojų duomenys ir nuolatinių Lietuvos Respublikos gyventojų negyvagimių duomenys pagal amžių, lytį, gyvenamosios vietos administracinę teritoriją, mirties vietą, pagrindinę mirties priežastį (pagal TLK-10-AM)."
resource: "https://get.data.gov.lt/datasets/gov/hi/mirtys"
tags: [gov, hi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/mirties_priezastys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/998/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/mirtys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Nuolatinių Lietuvos gyventojų, mirusių Lietuvoje ar užsienyje, mirties atvejų ir jų priežasčių duomenys

- **Namespace:** `datasets/gov/hi/mirtys`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/mirties_priezastys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/mirtys` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/998/`[^dcat]
- **Publisher (`dct:publisher`):** Higienos institutas[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/mirtys`[^dcat]
- **Portal Title (`@lt`):** Nuolatinių Lietuvos gyventojų, mirusių Lietuvoje ar užsienyje, ir nuolatinių Lietuvos Respublikos gyventojų negyvagimių mirties atvejų ir jų priežasčių duomenys[^dcat]
- **Portal Title (`@en`):** Data on death cases and their causes of residents of Lithuania and stillbirths of residents of Lithuania, who died in Lithuania and abroad[^dcat]
- **Issued (`dct:issued`):** `2023-05-29`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2026-01-29` .. `2026-04-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami mirusių nuolatinių Lietuvos gyventojų duomenys ir nuolatinių Lietuvos Respublikos gyventojų negyvagimių duomenys pagal amžių, lytį, gyvenamosios vietos administracinę teritoriją, mirties vietą, pagrindinę mirties priežastį (pagal TLK-10-AM). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data of residens of Lithuania and stillbirths of residents of Lithuania by age, sex, administrative territory of residence, place of death and underlying cause of death (ICD-10-AM) are presented[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NuolatinisGyventojas](mirtys/NuolatinisGyventojas.md) | Nuolatinių Lietuvos Respublikos gyventojų mirties atvejai ir jų priežastys | `4` | `m_id` | — | `26` | — |
| [Negyvagimis](mirtys/Negyvagimis.md) | Nuolatinių Lietuvos Respublikos gyventojų negyvagimių mirties atvejai ir jų priežastys | `3` | `m_id` | — | `26` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/mirties_priezastys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/mirtys (https://data.gov.lt/datasets/998/)
