---
type: Dataset
title: "Likviduoto hipotekos registro (HR) archyviniai duomenys apie sandorius"
description: "HR archyviniai duomenys apie sandorius (pagal hipotekos sandorių rūšis, vertę ir kt.)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/sandoriai"
tags: [gov, rc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/sandoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/sandoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/hr/sandoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Likviduoto hipotekos registro (HR) archyviniai duomenys apie sandorius

- **Namespace:** `datasets/gov/rc/hr/sandoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/hr/sandoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/sandoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/sandoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1996/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/hr/sandoriai`[^dcat]
- **Portal Title (`@lt`):** Likviduoto hipotekos registro (HR) archyviniai duomenys apie sandorius[^dcat]
- **Portal Title (`@en`):** Archive data on transactions of the Liquidated Mortgage Register (HR).[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2022-10-25` .. `2023-11-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

HR archyviniai duomenys apie sandorius (pagal hipotekos sandorių rūšis, vertę ir kt.). Likviduoto Lietuvos Respublikos hipotekos registro (HR) archyviniai duomenys.[^dcat]

### Portal Description (`@en`)

HR archival data on transactions (by types of mortgage transactions, value, etc.). Archive data of the liquidated mortgage register of the Republic of Lithuania (HR). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sandoris](sandoriai/Sandoris.md) | HR archyviniai duomenys apie sandorius (pagal hipotekos sandorių rūšis, vertė ir kt.) | `4` | `id` | — | `19` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/sandoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/sandoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/hr/sandoriai (https://data.gov.lt/datasets/1996/)
