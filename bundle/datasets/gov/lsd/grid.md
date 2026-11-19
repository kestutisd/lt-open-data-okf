---
type: Dataset
title: "Tinkleliai sudaryti LKS-94 Lietuvos valstybinėje koordinačių sistemoje"
description: "Naudojamas Lietuvoje stabilus teritorinis vienetas skelbti statistinę informaciją."
resource: "https://get.data.gov.lt/datasets/gov/lsd/grid"
tags: [gov, lsd, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/grid.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2047/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/grid"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Tinkleliai sudaryti LKS-94 Lietuvos valstybinėje koordinačių sistemoje

- **Namespace:** `datasets/gov/lsd/grid`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/grid.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/grid` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `10` (10 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2047/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/grid`[^dcat]
- **Portal Title (`@lt`):** Statistiniai tinkleliai: 1 km stačiakampės ir šešiakampės gardelės[^dcat]
- **Portal Title (`@en`):** Statistical grids: 1 km rectangular and hexagonal grids[^dcat]
- **Issued (`dct:issued`):** `2023-06-06`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2022-10-21` .. `2025-02-11`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Naudojamas Lietuvoje stabilus teritorinis vienetas skelbti statistinę informaciją. Gardelių tinklas sudarytas LKS-94 Lietuvos valstybinėje koordinačių sistemoje. Duomenų rinkinyje pateikiamos stačiakampės 1x1 km ir šešiakampės 1km dydžio gardelės. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

A stable territorial unit is used in Lithuania to publish statistical information. The lattice network is drawn up in the LKS-94 Lithuanian state coordinate system. The dataset contains rectangular 1x1 km and hexagonal 1 km grids[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Grid1KmSq](grid/Grid1KmSq.md) | Stačiakampės gardelės 1 km (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid1KmHx](grid/Grid1KmHx.md) | Šešiakampės gardelės 1 km (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid100mSq](grid/Grid100mSq.md) | Šešiakampės gardelės 100 m (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid250mSq](grid/Grid250mSq.md) | Šešiakampės gardelės 250 m (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid500mSq](grid/Grid500mSq.md) | Šešiakampės gardelės 500 m (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid2KmHq](grid/Grid2KmHq.md) | Šešiakampės gardelės 2 km (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid2500mSq](grid/Grid2500mSq.md) | Šešiakampės gardelės 2500 m (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid5KmHx](grid/Grid5KmHx.md) | Šešiakampės gardelės 5 km (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid5KmSq](grid/Grid5KmSq.md) | Šešiakampės gardelės 5 km (LKS-94) | `4` | `grid_id` | — | `6` | — |
| [Grid10KmSq](grid/Grid10KmSq.md) | Šešiakampės gardelės 10 km (LKS-94) | `4` | `grid_id` | — | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/grid.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/grid.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/grid (https://data.gov.lt/datasets/2047/)
