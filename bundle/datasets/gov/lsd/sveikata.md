---
type: Dataset
title: "Gyventojų sveikatos statistinio tyrimo duomenys"
description: "Kas 5 metus atliekamas gyventojų sveikatos statistinis tyrimas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata"
tags: [gov, lsd, deployed, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1622/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Gyventojų sveikatos statistinio tyrimo duomenys

- **Namespace:** `datasets/gov/lsd/sveikata`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1622/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata`[^dcat]
- **Portal Title (`@lt`):** Gyventojų sveikatos statistinio tyrimo duomenys[^dcat]
- **Portal Title (`@en`):** Population Health Statistical Survey[^dcat]
- **Issued (`dct:issued`):** `2022-10-27`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUINQUENNIAL` (`http://publications.europa.eu/resource/authority/frequency/QUINQUENNIAL`)[^dcat]
- **Distribution Date Span:** `2021-08-20` .. `2021-10-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kas 5 metus atliekamas gyventojų sveikatos statistinis tyrimas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Population Health Statistical Survey[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyventojuSveikata2014](sveikata/GyventojuSveikata2014.md) | Gyventojų sveikatos statistinis tyrimas 2014 m. | — | — | — | `145` | 2014 metais atliktas gyventojų sveikatos statistinis tyrimas |
| [GyventojuSveikata2019](sveikata/GyventojuSveikata2019.md) | Gyventojų sveikatos statistinis tyrimas 2019 m. | — | — | — | `144` | 2019 metais atliktas gyventojų sveikatos statistinis tyrimas |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |
| `sex` | `1` | — | — | Taip | — |
| `sex` | `2` | — | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata (https://data.gov.lt/datasets/1622/)
