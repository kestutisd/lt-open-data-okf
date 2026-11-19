---
type: Dataset
title: "Statistinis ūkių registras"
description: "Statistinio ūkių registro atviri duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistinis_ukiu_registras"
tags: [gov, lsd, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistinis_ukiu_registras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistinis_ukiu_registras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/5962/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistinis_ukiu_registras"
    author: "team:vda"
    last_modified: "2026-09-07T00:00:00Z"
---

# Statistinis ūkių registras

Statistinio ūkių registro atviri duomenys[^manifest]

- **Namespace:** `datasets/gov/lsd/statistinis_ukiu_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistinis_ukiu_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistinis_ukiu_registras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistinis_ukiu_registras` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/5962/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistinis_ukiu_registras`[^dcat]
- **Portal Title (`@lt`):** Statistinis ūkių registras[^dcat]
- **Portal Title (`@en`):** Statistinis ūkių registras[^dcat]
- **Issued (`dct:issued`):** `2026-08-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-09-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2026-08-06` .. `2026-09-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Statistinio ūkių registro atviri duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [UkiuRegistras](statistinis_ukiu_registras/UkiuRegistras.md) | Statistinis ūkių registras | `4` | `u_id` | — | `11` | Statistinio ūkių registro atviri duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistinis_ukiu_registras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistinis_ukiu_registras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistinis_ukiu_registras (https://data.gov.lt/datasets/5962/)
