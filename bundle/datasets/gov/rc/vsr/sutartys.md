---
type: Dataset
title: "Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis"
description: "VSR duomenys apie vedybų sutartis."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/sutartys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2153/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/vsr/sutartys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis

- **Namespace:** `datasets/gov/rc/vsr/sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/vsr/sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2153/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys`[^dcat]
- **Portal Title (`@lt`):** Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis[^dcat]
- **Portal Title (`@en`):** VSR data on marriage contracts[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-05` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

VSR duomenys apie vedybų sutartis. Vedybų sutarčių registro (VSR) duomenys.[^dcat]

### Portal Description (`@en`)

VSR data on marriage contracts. Data from the Register of Marriage Contracts (VSR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VsrSutartis](sutartys/VsrSutartis.md) | Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis | — | `dok_id` | — | `9` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/sutartys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/vsr/sutartys (https://data.gov.lt/datasets/2153/)
