---
type: Dataset
title: "Įmonių bankroto ataskaitų duomenys"
description: "Įmonių bankroto ataskaitų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas"
tags: [gov, avnt, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_bankrotas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1979/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_bankrotas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Įmonių bankroto ataskaitų duomenys

- **Namespace:** `datasets/gov/avnt/imoniu_bankrotas`[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/imoniu_bankrotas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1979/`[^dcat]
- **Publisher (`dct:publisher`):** Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba prie Lietuvos Respublikos finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas`[^dcat]
- **Portal Title (`@lt`):** Įmonių bankroto ataskaitų duomenys[^dcat]
- **Portal Title (`@en`):** Data from corporate bankruptcy reports[^dcat]
- **Issued (`dct:issued`):** `2022-07-20`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2022-07-20` .. `2026-09-19`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Įmonių bankroto ataskaitų duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data from corporate bankruptcy reports[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BankrotoAtaskaitosDatos](imoniu_bankrotas/BankrotoAtaskaitosDatos.md) | Įmonių bankroto ataskaitų duomenys | `2` | — | — | `23` | — |
| [BankrotoAtaskaitosFinansai](imoniu_bankrotas/BankrotoAtaskaitosFinansai.md) | Įmonių bankroto ataskaitų duomenų finansiniai duomenys | `3` | — | — | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_bankrotas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_bankrotas (https://data.gov.lt/datasets/1979/)
