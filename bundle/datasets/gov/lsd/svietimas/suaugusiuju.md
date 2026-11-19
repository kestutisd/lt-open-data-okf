---
type: Dataset
title: "Suaugusiųjų švietimo statistinio tyrimo duomenys"
description: "Kas 5 metus atliekamas suaugusiųjų švietimo statistinis tyrimas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju"
tags: [gov, lsd, deployed, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1621/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Suaugusiųjų švietimo statistinio tyrimo duomenys

- **Namespace:** `datasets/gov/lsd/svietimas/suaugusiuju`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/svietimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1621/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju`[^dcat]
- **Portal Title (`@lt`):** Suaugusiųjų švietimo statistinio tyrimo duomenys[^dcat]
- **Portal Title (`@en`):** Statistical survey of adult education[^dcat]
- **Issued (`dct:issued`):** `2022-10-27`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUINQUENNIAL` (`http://publications.europa.eu/resource/authority/frequency/QUINQUENNIAL`)[^dcat]
- **Distribution Date Span:** `2021-10-04` .. `2024-12-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kas 5 metus atliekamas suaugusiųjų švietimo statistinis tyrimas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Statistical survey of adult education[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SuaugusiujuSvietimas2005](suaugusiuju/SuaugusiujuSvietimas2005.md) | Suaugusiųjų švietimo statistinis tyrimas 2005 m. | — | — | — | `90` | 2005 metais atliktas suaugusiųjų švietimo statistinio tyrimas |
| [SuaugusiujuSvietimas2011](suaugusiuju/SuaugusiujuSvietimas2011.md) | Suaugusiųjų švietimo statistinis tyrimas 2011 m. | — | — | — | `58` | 2011 metais atliktas suaugusiųjų švietimo statistinio tyrimas |
| [SuaugusiujuSvietimas2016](suaugusiuju/SuaugusiujuSvietimas2016.md) | Suaugusiųjų švietimo statistinis tyrimas 2016 m. | — | — | — | `241` | 2016 metais atliktas suaugusiųjų švietimo statistinio tyrimas |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju (https://data.gov.lt/datasets/1621/)
