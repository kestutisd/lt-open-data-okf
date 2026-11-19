---
type: Dataset
title: "Mokiniams suteiktos socialinės paramos duomenys"
description: "Socialinės Apsaugos ir Darbo Ministerijos duomenys apie mokiniams suteiktą socialinę paramą savivaldybėse (nemokamas maitinimas ir parama mokinio reikmenims įsigyti)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams"
tags: [gov, sadm, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/sadm/parama_mokiniams.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1997/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/parama_mokiniams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mokiniams suteiktos socialinės paramos duomenys

Socialinės Apsaugos ir Darbo Ministerijos duomenys apie mokiniams suteiktą socialinę paramą savivaldybėse (nemokamas maitinimas ir parama mokinio reikmenims įsigyti). Duomenys atnaujinami kas ketvirtį.[^manifest]

- **Namespace:** `datasets/gov/sadm/parama_mokiniams`[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/parama_mokiniams.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1997/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams`[^dcat]
- **Portal Title (`@lt`):** Mokiniams suteiktos socialinės paramos duomenys[^dcat]
- **Portal Title (`@en`):** Data on social support provided to students[^dcat]
- **Issued (`dct:issued`):** `2023-05-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-03-07` .. `2026-10-19`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie mokiniams suteiktą socialinę paramą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on social support provided to students[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Aprupinimas](parama_mokiniams/Aprupinimas.md) | Duomenys apie paramą mokiniams | `4` | `id` | `open` | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/parama_mokiniams.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/parama_mokiniams (https://data.gov.lt/datasets/1997/)
