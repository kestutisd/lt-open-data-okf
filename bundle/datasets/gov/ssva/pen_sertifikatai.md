---
type: Dataset
title: "Duomenys apie pastatų energinio naudingumo sertifikatus"
description: "Duomenys apie pastatų energinio naudingumo sertifikatus."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai"
tags: [gov, ssva, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2366/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pen_sertifikatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Duomenys apie pastatų energinio naudingumo sertifikatus

- **Namespace:** `datasets/gov/ssva/pen_sertifikatai`[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/pens_ekspertu_atestatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2366/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ssva/pen_sertifikatai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie pastatų energinio naudingumo sertifikatus[^dcat]
- **Portal Title (`@en`):** Data on building energy performance certificates[^dcat]
- **Issued (`dct:issued`):** `2023-09-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-09-27` .. `2026-01-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie pastatų energinio naudingumo sertifikatus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on building energy performance certificates[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sertifikatas](pen_sertifikatai/Sertifikatas.md) | Pastatų energinio naudingumo sertifikatai | `2` | `id` | — | `19` | Pastatų energinio naudingumo sertifikatai |
| [Paskirtis](pen_sertifikatai/Paskirtis.md) | Pastatų paskirtys | `4` | `id` | — | `3` | Pagal STR 2.01.09:2005 ir STR 2.01.02:2016 |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pens_ekspertu_atestatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pens_ekspertu_atestatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pen_sertifikatai (https://data.gov.lt/datasets/2366/)
