---
type: Dataset
title: "2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys"
description: "Skelbiama detali informacija apie 2014-2020 metų Europos Sąjungos fondų investicinių projektų kontrolės veiksmus (projekto patikra, projekto patikros vietoje pastebėjimai, grąžintinos lėšos, audito pastebėjimai ir kt.)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai"
tags: [gov, finmin, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2162/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kontroles_veiksmai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# 2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys

- **Namespace:** `datasets/gov/finmin/kontroles_veiksmai`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kontroles_veiksmai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2162/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai`[^dcat]
- **Portal Title (`@lt`):** 2014-2020 m. Europos Sąjungos fondų projektų kontrolės veiksmų duomenys[^dcat]
- **Portal Title (`@en`):** Data on control actions of 2014-2020 EU funds projects[^dcat]
- **Issued (`dct:issued`):** `2023-06-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-05-30` .. `2023-06-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Skelbiama detali informacija apie 2014-2020 metų Europos Sąjungos fondų investicinių projektų kontrolės veiksmus (projekto patikra, projekto patikros vietoje pastebėjimai, grąžintinos lėšos, audito pastebėjimai ir kt.). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Detailed information on control actions of investment projects of EU funds for the period 2014-2020 (project inspection, allegations of irregularities, audit observations, etc.) is published.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Revise](kontroles_veiksmai/Revise.md) | Projekto patikros vietoje | `4` | `revise_id` | — | `13` | — |
| [Suspicion](kontroles_veiksmai/Suspicion.md) | Įtarimas | `4` | `suspicion_id` | — | `19` | — |
| [Audit](kontroles_veiksmai/Audit.md) | Projekto audito pastebėjimai | `4` | `audit_id` | — | `18` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kontroles_veiksmai (https://data.gov.lt/datasets/2162/)
