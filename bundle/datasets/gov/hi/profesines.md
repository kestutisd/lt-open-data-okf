---
type: Dataset
title: "Lietuvos Respublikos profesinių ligų valstybės registro duomenys"
description: "Duomenys apie profesinių ligų atvejus ir asmenis, kuriems nustatyta profesinė liga."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines"
tags: [gov, hi, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2257/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/profesines"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos Respublikos profesinių ligų valstybės registro duomenys

- **Namespace:** `datasets/gov/hi/profesines`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2257/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/profesines`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos profesinių ligų valstybės registro duomenys[^dcat]
- **Portal Title (`@en`):** Data from the State Register of Occupational Diseases of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2023-06-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2026-04-03` .. `2026-06-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie profesinių ligų atvejus ir asmenis, kuriems nustatyta profesinė liga. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on cases of occupational diseases and persons diagnosed with an occupational disease.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Issilavinimas](profesines/Issilavinimas.md) | Profesinių ligų atvejai pagal išsilavinimą | `4` | `atvejis_id` | — | `8` | — |
| [DarboStazas](profesines/DarboStazas.md) | Profesinių ligų atvejai pagal darbo stažą | `4` | `atvejis_id` | — | `8` | — |
| [Asmuo](profesines/Asmuo.md) | Profesinių ligų įvykių pagrindiniai duomenys | `4` | `m_id` | — | `15` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/profesines (https://data.gov.lt/datasets/2257/)
