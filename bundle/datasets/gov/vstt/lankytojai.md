---
type: Dataset
title: "Saugomų teritorijų lankytojų duomenys"
description: "Lankytojų monitoringo duomenys saugomose teritorijose."
resource: "https://get.data.gov.lt/datasets/gov/vstt/lankytojai"
tags: [gov, vstt, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vstt/lankytoju_monitoringas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2303/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/lankytojai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Saugomų teritorijų lankytojų duomenys

- **Namespace:** `datasets/gov/vstt/lankytojai`[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/lankytoju_monitoringas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/lankytojai` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2303/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vstt/lankytojai`[^dcat]
- **Portal Title (`@lt`):** Lankytojų monitoringo duomenys saugomose teritorijose[^dcat]
- **Portal Title (`@en`):** Visitor Monitoring Data in Protected Areas[^dcat]
- **Issued (`dct:issued`):** `2023-05-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-05-26` .. `2023-07-11`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lankytojų monitoringo duomenys saugomose teritorijose. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Visitor Monitoring Data in Protected Areas[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Monitoringas](lankytojai/Monitoringas.md) | Saugomų teritorijų lankytojų duomenys | `2` | `teritorija` | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/lankytoju_monitoringas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/lankytoju_monitoringas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/lankytojai (https://data.gov.lt/datasets/2303/)
