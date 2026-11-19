---
type: Dataset
title: "Saugomų rūšių duomenys"
description: "Saugojamos rūšys,Saugojamų augalų, gyvūnų, grybų rūšių duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/rusys"
tags: [gov, vstt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugojamos_rusys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugojamos_rusys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2269/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/rusys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Saugomų rūšių duomenys

Saugojamos rūšys,Saugojamų augalų, gyvūnų, grybų rūšių duomenys[^manifest]

- **Namespace:** `datasets/gov/vstt/rusys`[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/saugojamos_rusys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugojamos_rusys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/rusys` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2269/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vstt/rusys`[^dcat]
- **Portal Title (`@lt`):** Saugomų rūšių duomenys[^dcat]
- **Portal Title (`@en`):** Protected species data[^dcat]
- **Issued (`dct:issued`):** `2023-03-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-03-23` .. `2025-04-24`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Saugomų rūšių informacinėje sistemoje (SRIS) kaupiama ir teikiama informacija apie Lietuvos Respublikos teritorijoje aptiktas saugomas rūšis. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Protected Species Information System collects and provides information on protected species found in the territory of the Republic of Lithuania.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Rusis](rusys/Rusis.md) | Saugojamos rūšys | `4` | `vda_id` | — | `24` | Saugojamų augalų, gyvūnų, grybų rūšių duomenys |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugojamos_rusys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugojamos_rusys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/rusys (https://data.gov.lt/datasets/2269/)
