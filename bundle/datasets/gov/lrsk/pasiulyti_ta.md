---
type: Dataset
title: "Inicijuoti teisės aktų projektai"
description: "Rinkinyje pateikiami duomenys apie teiktus pasiūlymus teisės aktų projektams: teisės aktus ir jų atributus."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/pasiulyti_ta"
tags: [gov, lrsk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/pasiulyti_ta.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/pasiulyti_ta.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2611/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/pasiulyti_ta"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Inicijuoti teisės aktų projektai

- **Namespace:** `datasets/gov/lrsk/pasiulyti_ta`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/pasiulyti_ta.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/pasiulyti_ta.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/pasiulyti_ta` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2611/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrsk/pasiulyti_ta/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Inicijuoti teisės aktų projektai[^dcat]
- **Portal Title (`@en`):** Draft legislation initiated[^dcat]
- **Issued (`dct:issued`):** `2024-04-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-04-15` .. `2026-08-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie teiktus pasiūlymus teisės aktų projektams: teisės aktus ir jų atributus. Jeigu pasiūlymas buvo inicijuotas Seime, nurodyti ir jį teikusių Seimo narių vardai ir pavardės. Duomenų teikėjas – Lietuvos Respublikos Seimo kanceliarija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on legislative proposals submitted: legislation and its attributes. If the proposal was initiated in the Seimas, the names of the Seimas Members who submitted it shall also be indicated. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pasiulymas](pasiulyti_ta/Pasiulymas.md) | Inicijuoti teisės aktų projektai | `4` | `vda_id` | — | `20` | Rinkinyje pateikiami duomenys apie teiktus pasiūlymus teisės aktų projektams: teisės aktus ir jų atributus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/pasiulyti_ta.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/pasiulyti_ta.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/pasiulyti_ta (https://data.gov.lt/datasets/2611/)
