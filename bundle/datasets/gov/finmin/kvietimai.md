---
type: Dataset
title: "2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys"
description: "Skelbiama detali informacija apie investicinius prioritetus, uždavinius ir priemones, stebėsenos rodiklius, pagal 2014–2020 metų Europos Sąjungos fondų investicijų veiksmų programą."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai"
tags: [gov, finmin, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2159/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# 2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys

- **Namespace:** `datasets/gov/finmin/kvietimai`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `6` (6 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2159/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai`[^dcat]
- **Portal Title (`@lt`):** 2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys[^dcat]
- **Portal Title (`@en`):** Data on 2014-2020 EU funds competitive calls and measures[^dcat]
- **Issued (`dct:issued`):** `2023-04-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-04-19` .. `2023-04-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Skelbiama detali informacija apie investicinius prioritetus, uždavinius ir priemones, stebėsenos rodiklius, pagal 2014–2020 metų Europos Sąjungos fondų investicijų veiksmų programą. Taip pat skelbiama informacija apie kvietimus teikti paraiškas, patvirtintus sąrašus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Detailed information on investment priorities, objectives and measures, monitoring indicators, according to the Investment Operational Program of the European Union Funds for 2014–2020, as well as information on competitive calls and/or approved lists for proposals is published.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Measure](kvietimai/Measure.md) | Investicinio prioriteto uždavinio priemonė | `4` | `measure_id` | — | `11` | — |
| [Call](kvietimai/Call.md) | Kvietimas / patvirtintas sąrašas | `4` | `call_id` | — | `14` | — |
| [MeasureIndicator](kvietimai/MeasureIndicator.md) | Priemonės stebėsenos rodiklis | `4` | `measure_indicator_id` | — | `17` | — |
| [Task](kvietimai/Task.md) | Investicinio prioriteto uždavinys | `4` | `task_id` | — | `6` | — |
| [Priority](kvietimai/Priority.md) | Prioritetas | `4` | `priority_id` | — | `5` | — |
| [PriorityFund](kvietimai/PriorityFund.md) | Prioriteto fondas | `4` | `priority_fund_id` | — | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai (https://data.gov.lt/datasets/2159/)
