---
type: Dataset
title: "pagd sirenos"
description: "Sirenų informacija"
resource: "https://get.data.gov.lt/datasets/gov/pagd/sirenos"
tags: [gov, pagd, deployed, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pagd/sirenos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/sirenos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# pagd sirenos

Sirenų informacija[^manifest]

- **Namespace:** `datasets/gov/pagd/sirenos`[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/sirenos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/sirenos` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2880/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pagd/sirenos`[^dcat]
- **Portal Title (`@lt`):** PAGD sirenos[^dcat]
- **Portal Title (`@en`):** PAGD sirens[^dcat]
- **Issued (`dct:issued`):** `2024-11-29`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `OTHER` (`http://publications.europa.eu/resource/authority/frequency/OTHER`)[^dcat]
- **Distribution Date Span:** `2024-11-29` .. `2026-10-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Sirenų informacija. Duomenis numatoma atnaujinti kiekvieną kartą kai atsinaujina duomenys. Valstybės priešgaisrinės gelbėjimo tarnybos informacinė sistema. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Sirens information. The data is expected to be updated each time the data updates. Information system of the State Fire and Rescue Service.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sirena](sirenos/Sirena.md) | — | `4` | `vda_id` | — | `17` | Sirenų informacija |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/sirenos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/sirenos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/sirenos (https://data.gov.lt/datasets/2880/)
