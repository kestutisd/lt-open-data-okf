---
type: Dataset
title: "Lietuvos Respublikos Seimo YouTube transliacijų duomenys"
description: "Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/youtube"
tags: [gov, lrsk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/youtube.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2614/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/youtube"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos Respublikos Seimo YouTube transliacijų duomenys

- **Namespace:** `datasets/gov/lrsk/youtube`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/youtube.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/youtube` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2614/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrsk/youtube/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos Seime vykusių renginių transliacijų YouTube duomenys[^dcat]
- **Portal Title (`@en`):** YouTube data of events held in the Seimas of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-04-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-04-15` .. `2026-08-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan. Taip pat pateikiama informacija apie transliacijos pradžios ir pabaigos laiko žymas. Duomenų teikėjas – Lietuvos Respublikos Seimo kanceliarija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on YouTube broadcasts conducted in the Seimas from committee meetings, conferences, press conferences, congresses, debates, etc. Information on the start and end time labels of the broadcast shall also be provided. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Transliacija](youtube/Transliacija.md) | Lietuvos Respublikos Seimo YouTube transliacijų duomenys | `4` | `vda_id` | — | `5` | Rinkinyje pateikiami duomenys apie Seime vykdytas YouTube transliacijas iš komitetų posėdžių, konferencijų, spaudos konferencijų, kongresų, diskusijų ir pan. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/youtube.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/youtube.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/youtube (https://data.gov.lt/datasets/2614/)
