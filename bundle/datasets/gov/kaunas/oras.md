---
type: Dataset
title: "Kauno miesto savivaldybės teikiami duomenys"
description: "Kauno miesto aplinkos parametrai"
resource: "https://get.data.gov.lt/datasets/gov/kaunas/oras"
tags: [gov, kaunas, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/oras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kaunas/oras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1948/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kaunas/oras"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kauno miesto savivaldybės teikiami duomenys

Kauno miesto aplinkos parametrai[^manifest]

- **Namespace:** `datasets/gov/kaunas/oras`[^manifest]
- **Manifest CSV:** [datasets/gov/kaunas/oras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/oras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kaunas/oras` (`deployed`)[^manifest]
- **Provider:** `kaunas` — Kauno miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1948/`[^dcat]
- **Publisher (`dct:publisher`):** Kauno miesto savivaldybės administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kaunas/oras`[^dcat]
- **Portal Title (`@lt`):** Oro kokybė Kauno mieste[^dcat]
- **Portal Title (`@en`):** Air quality in Kaunas[^dcat]
- **Issued (`dct:issued`):** `2022-06-08`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-05-23` .. `2024-07-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Oro kokybės daviklių stebėjimo duomenys[^dcat]

### Portal Description (`@en`)

Monitoring data for air quality sensors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Oras](oras/Oras.md) | Rodikliai per periodą | — | `id,dt` | — | `13` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kaunas/oras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/oras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kaunas/oras (https://data.gov.lt/datasets/1948/)
