---
type: Dataset
title: "Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys"
description: "Lentelėje pateikti bendrojo ugdymo institucijų turimų kitų, ne klasės tipo, patalpų (pvz.: valgyklų, sporto salių, bibliotekų) skaičiai kiekvienų mokslo metų spalio 1 d."
resource: "https://get.data.gov.lt/datasets/gov/nsa/svis/mokyklu_kitos_patalpos"
tags: [gov, nsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2717/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/svis/mokyklu_kitos_patalpos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys

- **Namespace:** `datasets/gov/nsa/svis/mokyklu_kitos_patalpos`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/svis/mokyklu_kitos_patalpos` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2717/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/svis/mokyklu_kitos_patalpos/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys[^dcat]
- **Portal Title (`@en`):** Data on other premises of general education institutions (e.g. canteens, sports halls, libraries)[^dcat]
- **Issued (`dct:issued`):** `2024-07-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti bendrojo ugdymo institucijų turimų kitų, ne klasės tipo, patalpų (pvz.: valgyklų, sporto salių, bibliotekų) skaičiai kiekvienų mokslo metų spalio 1 d. (pradedant 2013-2014 mokslo metais). Duomenys paimti iš Nacionalinės švietimo agentūros (NŠA) Švietimo valdymo informacinės sistemos (ŠVIS). Duomenys atsinaujina kiekvieno mėnesio pirmąją dieną. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table shows the number of premises (e.g. canteens, sports halls, libraries) held by general education institutions other than the class type on 1 October of each school year (starting with the 2013-2014 school year). The data came from the National Education Agency (NSA) Education Management Information System (SEN). The data updates on the first day of each month. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MokyklosPatalpa](mokyklu_kitos_patalpos/MokyklosPatalpa.md) | Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys | `4` | `iraso_id` | — | `24` | Lentelėje pateikti bendrojo ugdymo institucijų turimų kitų, ne klasės tipo, patalpų (pvz.: valgyklų, sporto salių, bibliotekų) skaičiai kiekvienų mokslo... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/svis/mokyklu_kitos_patalpos (https://data.gov.lt/datasets/2717/)
