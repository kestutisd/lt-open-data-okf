---
type: Dataset
title: "Aktualių adresų gardelės"
description: "Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles"
tags: [gov, lsd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2693/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/aktualiu_adresu_gardeles"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Aktualių adresų gardelės

- **Namespace:** `datasets/gov/lsd/aktualiu_adresu_gardeles`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2693/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles`[^dcat]
- **Portal Title (`@lt`):** Aktualių adresų gardelės[^dcat]
- **Portal Title (`@en`):** Current address stalls[^dcat]
- **Issued (`dct:issued`):** `2024-06-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-02-16` .. `2026-04-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais. Gardelių identifikatoriai paimti iš tinklelių lentelių (https://get.data.gov.lt/datasets/gov/lsd/grid/:ns). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Geospatial data (points) of relevant (valid) addresses of the graphic address register with identifiers of different sizes of cells. Cell IDs are taken from grid tables (https://get.data.gov.lt/datasets/gov/lsd/grid/:ns)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AdresoGardele](aktualiu_adresu_gardeles/AdresoGardele.md) | Aktualių adresų gardelės | `4` | `iraso_id` | — | `19` | Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/aktualiu_adresu_gardeles (https://data.gov.lt/datasets/2693/)
