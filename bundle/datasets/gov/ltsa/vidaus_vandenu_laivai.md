---
type: Dataset
title: "Vidaus vandenų laivų duomenys"
description: "Lietuvoje registruotų komercinių vidaus vandenų laivų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai"
tags: [gov, ltsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2091/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/vidaus_vandenu_laivai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Vidaus vandenų laivų duomenys

- **Namespace:** `datasets/gov/ltsa/vidaus_vandenu_laivai`[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2091/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos transporto saugos administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ltsa/vidaus_vandenu_laivai`[^dcat]
- **Portal Title (`@lt`):** Vidaus vandenų laivų duomenys[^dcat]
- **Portal Title (`@en`):** Data of inland vessels[^dcat]
- **Issued (`dct:issued`):** `2023-10-04`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-09-25` .. `2024-10-08`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvoje registruotų komercinių vidaus vandenų laivų duomenys[^dcat]

### Portal Description (`@en`)

Data of commercial inland water vessels registered in Lithuania[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VidausVandenuLaivas](vidaus_vandenu_laivai/VidausVandenuLaivas.md) | Vidaus vandenų laivai | `4` | `ship_id,own_le` | — | `19` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/vidaus_vandenu_laivai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/vidaus_vandenu_laivai (https://data.gov.lt/datasets/2091/)
