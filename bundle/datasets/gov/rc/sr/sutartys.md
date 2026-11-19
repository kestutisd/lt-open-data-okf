---
type: Dataset
title: "Reorganizuoto Sutarčių registro (SR) archyviniai duomenys"
description: "Sutarčių registro archyviniai duomenys apie sutartis pagal rūšis."
resource: "https://get.data.gov.lt/datasets/gov/rc/sr/sutartys"
tags: [gov, rc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/sutartys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/sr/sutartys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2132/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/sr/sutartys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Reorganizuoto Sutarčių registro (SR) archyviniai duomenys

- **Namespace:** `datasets/gov/rc/sr/sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/sr/sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/sutartys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/sr/sutartys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2132/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/sr/sutartys`[^dcat]
- **Portal Title (`@lt`):** Reorganizuoto Sutarčių registro archyviniai duomenys apie sutartis pagal rūšis[^dcat]
- **Portal Title (`@en`):** Archival data of the Reorganized Register of Contracts on contracts by type[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2023-08-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Sutarčių registro archyviniai duomenys apie sutartis pagal rūšis. Reorganizuoto SR archyviniai duomenys.[^dcat]

### Portal Description (`@en`)

Contract register archive data on contracts by type. Archive data of the reorganized SR. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](sutartys/Sutartis.md) | SR archyviniai duomenys apie sutartis pagal rūšis | `3` | `dok_nr, turto_tipas` | — | `12` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/sr/sutartys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/sutartys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/sr/sutartys (https://data.gov.lt/datasets/2132/)
