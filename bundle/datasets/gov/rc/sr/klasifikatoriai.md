---
type: Dataset
title: "Reorganizuoto Sutarčių registro (SR) archyviniai duomenys"
description: "Reorganizuoto SR archyviniai klasifikatoriai (Sutarčių registro sutarčių tipų archyvinis klasifikatorius; Sutarčių registro daiktų rūšių archyvinis klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/sr/klasifikatoriai"
tags: [gov, rc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/sr/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2133/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/sr/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Reorganizuoto Sutarčių registro (SR) archyviniai duomenys

- **Namespace:** `datasets/gov/rc/sr/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/sr/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/sr/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2133/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/sr/klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Reorganizuoto SR archyviniai klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Archival classifiers of the reorganized SR[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-01-04` .. `2023-08-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Reorganizuoto SR archyviniai klasifikatoriai (Sutarčių registro sutarčių tipų archyvinis klasifikatorius; Sutarčių registro daiktų rūšių archyvinis klasifikatorius).[^dcat]

### Portal Description (`@en`)

Archival classifiers of the reorganized SR (archival classifier of types of contracts of the Register of Contracts; archival classifier of types of items of the Register of Contracts). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SutartiesTipas](klasifikatoriai/SutartiesTipas.md) | Sutarčių registro sutarčių tipų archyvinis klasifikatorius | `4` | `kodas` | — | `2` | — |
| [TurtoTipas](klasifikatoriai/TurtoTipas.md) | Sutarčių registro daiktų rūšių archyvinis klasifikatorius | `4` | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/sr/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/sr/klasifikatoriai (https://data.gov.lt/datasets/2133/)
