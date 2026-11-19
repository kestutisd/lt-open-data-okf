---
type: Dataset
title: "Valstybės kontrolės metinio veiklos plano duomenys"
description: "Valstybės kontrolės metinio veiklos plano, kuriame pateikiama informacija apie planuojamus, atliekamus auditus ir vertinimus, duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/mvp"
tags: [gov, vk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/mvp.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vk/mvp.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1694/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/mvp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės kontrolės metinio veiklos plano duomenys

- **Namespace:** `datasets/gov/vk/mvp`[^manifest]
- **Manifest CSV:** [datasets/gov/vk/mvp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/mvp.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/mvp` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1694/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos Respublikos valstybės kontrolė[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vk/mvp`[^dcat]
- **Portal Title (`@lt`):** Valstybės kontrolės metinio veiklos plano duomenys[^dcat]
- **Portal Title (`@en`):** Data of the annual activity plan of the State Audit Office[^dcat]
- **Issued (`dct:issued`):** `2023-02-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-02-20` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės kontrolės metinio veiklos plano, kuriame pateikiama informacija apie planuojamus, atliekamus auditus ir vertinimus, duomenys[^dcat]

### Portal Description (`@en`)

Data on the annual activity plan of the State Audit Office, which provides information on planned and performed audits and evaluations[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MetinisVeiklosPlanas](mvp/MetinisVeiklosPlanas.md) | Valstybės kontrolės metinio veiklos plano duomenys | `4` | — | — | `7` | Valstybės kontrolės metinio veiklos plano, kuriame pateikiama informacija apie planuojamus, atliekamus auditus ir vertinimus, duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/mvp.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/mvp.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/mvp (https://data.gov.lt/datasets/1694/)
