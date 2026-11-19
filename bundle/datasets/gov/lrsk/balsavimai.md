---
type: Dataset
title: "Balsavimai"
description: "Seimo narių balsavimo rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/lrsk/balsavimai"
tags: [gov, lrsk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/6101/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/balsavimai"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# Balsavimai

- **Namespace:** `datasets/gov/lrsk/balsavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/balsavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/balsavimai` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/6101/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Seimo narių balsavimo rezultatai[^dcat]
- **Portal Title (`@en`):** Seimo narių balsavimo rezultatai[^dcat]
- **Issued (`dct:issued`):** `2026-10-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-27`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-10-15` .. `2026-10-27`[^dcat]

### Portal Description (`@lt`)

Seimo narių balsavimo rezultatai[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Balsavimas](balsavimai/Balsavimas.md) | Balsavimai | `4` | `balsavimo_id` | — | `18` | — |
| [IndividualusBalsavimai](balsavimai/IndividualusBalsavimai.md) | Individualūs balsavimai | `4` | `rezultato_id` | — | `8` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/balsavimai (https://data.gov.lt/datasets/6101/)
