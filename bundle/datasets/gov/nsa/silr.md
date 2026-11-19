---
type: Dataset
title: "Švietimo įstaigų lankomumo rodikliai"
description: "Duomenų rinkinį sudaro mokinių lankomumo mėnesiniai duomenys pagal mokyklą, klasę ir mokomąjį dalyką."
resource: "https://get.data.gov.lt/datasets/gov/nsa/silr"
tags: [gov, nsa, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2910/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/silr"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Švietimo įstaigų lankomumo rodikliai

- **Namespace:** `datasets/gov/nsa/silr`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/silr/silr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/silr` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2910/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/silr`[^dcat]
- **Portal Title (`@lt`):** Bendrojo ugdymo mokyklų lankomumo rodikliai[^dcat]
- **Portal Title (`@en`):** Attendance rates of general education schools[^dcat]
- **Issued (`dct:issued`):** `2024-12-31`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2024-12-31` .. `2026-07-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinį sudaro mokinių lankomumo mėnesiniai duomenys pagal mokyklą, klasę ir mokomąjį dalyką. Duomenys gauti naudojant UAB „Tavo mokykla“ elektroninio TAMO dienyno (www.tamo.lt) įrašus nuo 2018-09-01 ir UAB „Nacionalinio švietimo centro“ elektroninio dienyno „Mano dienynas“ (www.manodienynas.lt) įrašus nuo 2012-09-01 iki 2024-08-31. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The dataset consists of monthly data on pupils attendance by school, class and subject matter. The data were obtained using the records OF the electronic TAMO daily (www.tamo.lt) of UAB “TAVO mokykla” from 2018-09-01 and the records of the electronic daily “Mano dienynas” (www.manodienynas.lt) of UAB “Nacionalinis švietimo centras” from 2012-09-01 to 2024-08-31. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Lankomumas](silr/Lankomumas.md) | "Mokinių lankomumas" | `4` | `vda_id` | — | `12` | — |
| [Mokykla](silr/Mokykla.md) | "Mokinių lankomumo duomenų mokyklos" | `4` | `vda_id` | — | `7` | — |
| [MokDalykas](silr/MokDalykas.md) | Mokinių lankomumo duomenų mokomųjų dalykų klasifikatorius | `4` | `vda_id` | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/silr (https://data.gov.lt/datasets/2910/)
