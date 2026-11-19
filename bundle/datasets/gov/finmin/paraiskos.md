---
type: Dataset
title: "2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys"
description: "Skelbiama detali informacija apie 2014-2020 metų Europos Sąjungos fondų investicinių projektų paraiškas (paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai, paraiškos projekto biudžetas, veiklos, uždaviniai, stebėsenos rodikliai ir kt.) ir projektų vertinimą."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos"
tags: [gov, finmin, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2160/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# 2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys

- **Namespace:** `datasets/gov/finmin/paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `8` (8 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2160/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos`[^dcat]
- **Portal Title (`@lt`):** 2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys[^dcat]
- **Portal Title (`@en`):** Data on EU funds projects applications and their evaluation for period 2014-2020[^dcat]
- **Issued (`dct:issued`):** `2023-04-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-04-26` .. `2023-06-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Skelbiama detali informacija apie 2014-2020 metų Europos Sąjungos fondų investicinių projektų paraiškas (paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai, paraiškos projekto biudžetas, veiklos, uždaviniai, stebėsenos rodikliai ir kt.) ir projektų vertinimą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Detailed information on the 2014-2020 European Union fund investment projects applications (sources of funding for the eligible costs of the application projects, budget of the project applications, activities, objectives, monitoring indicators, etc.) and project evaluation is published.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Project](paraiskos/Project.md) | Projektas ir jo vertinimai | `4` | `project_id` | — | `17` | — |
| [Application](paraiskos/Application.md) | Projekto paraiška | `4` | `project` | — | `17` | — |
| [AppPartner](paraiskos/AppPartner.md) | Paraiškos partneriai | `4` | `app_partner_id` | — | `7` | — |
| [AppPurchase](paraiskos/AppPurchase.md) | Vykdomi ir iki paraiškos pateikimo įvykdyti pirkimai | `4` | `app_purchase_id` | — | `6` | — |
| [AppIndicator](paraiskos/AppIndicator.md) | Paraiškos produkto ir rezultato stebėsenos rodikliai | `4` | `app_indicator_id` | — | `4` | — |
| [AppFinSource](paraiskos/AppFinSource.md) | Paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai | `4` | `app_fin_source_id` | — | `5` | — |
| [AppTask](paraiskos/AppTask.md) | Paraiškos uždaviniai | `4` | `app_task_id` | — | `4` | — |
| [AppActivity](paraiskos/AppActivity.md) | Paraiškos uždavinio veiklos | `4` | `app_activity_id` | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos (https://data.gov.lt/datasets/2160/)
