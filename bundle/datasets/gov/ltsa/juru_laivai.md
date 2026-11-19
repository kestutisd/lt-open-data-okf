---
type: Dataset
title: "Jūrų laivų duomenys"
description: "Lietuvoje registruotų jūrų laivų duomenų rinkinys"
resource: "https://get.data.gov.lt/datasets/gov/ltsa/juru_laivai"
tags: [gov, ltsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/juru_laivai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/juru_laivai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2090/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/juru_laivai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Jūrų laivų duomenys

- **Namespace:** `datasets/gov/ltsa/juru_laivai`[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/juru_laivai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/juru_laivai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/juru_laivai` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2090/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos transporto saugos administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ltsa/juru_laivai`[^dcat]
- **Portal Title (`@lt`):** Jūrų laivų duomenys[^dcat]
- **Portal Title (`@en`):** Marine vessel data[^dcat]
- **Issued (`dct:issued`):** `2023-10-04`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-09-25` .. `2024-09-19`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvoje registruotų jūrų laivų duomenų rinkinys[^dcat]

### Portal Description (`@en`)

A collection of data on marine vessels registered in Lithuania[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [JuruLaivas](juru_laivai/JuruLaivas.md) | Jūrų laivai | `4` | `reg_perm_id,reg_temp_id,own_le,own_np_sys_id` | `open` | `27` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/juru_laivai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/juru_laivai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/juru_laivai (https://data.gov.lt/datasets/2090/)
