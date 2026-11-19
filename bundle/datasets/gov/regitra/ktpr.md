---
type: Dataset
title: "Tranporto priemonių valstybiniai numeriai pagal markę ir modelį"
description: "AB „Regitra“ Kelių transporto priemonių registre kaupiami motorinių transporto priemonių, išskyrus nurodytų Lietuvos Respublikos saugaus eismo automobilių keliais įstatymo 27 straipsnio 7 dalyje, ir jų priekabų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/regitra/ktpr"
tags: [gov, regitra, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/regitra/ktpr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2749/"
    title: "data.gov.lt DCAT-AP — datasets/gov/regitra/ktpr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Tranporto priemonių valstybiniai numeriai pagal markę ir modelį

- **Namespace:** `datasets/gov/regitra/ktpr`[^manifest]
- **Manifest CSV:** [datasets/gov/regitra/ktpr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/ktpr` (`deployed`)[^manifest]
- **Provider:** `regitra` — AB „Regitra“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2749/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/regitra/ktpr`[^dcat]
- **Portal Title (`@lt`):** Transporto priemonių valstybiniai numeriai pagal markę ir modelį[^dcat]
- **Portal Title (`@en`):** Transmitter State Numbers by Mark and Model[^dcat]
- **Issued (`dct:issued`):** `2024-08-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-08-13` .. `2025-01-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AB „Regitra“ Kelių transporto priemonių registre kaupiami motorinių transporto priemonių, išskyrus nurodytų Lietuvos Respublikos saugaus eismo automobilių keliais įstatymo 27 straipsnio 7 dalyje, ir jų priekabų duomenys. Rinkinio duomenys kaupiami nuo 2005 m. ir yra atnaujinami kasdien. Duomenų rinkinį sudaro: automobilio markė, modelis ir valstybinių numerių žymėjimas, raides pakeitus į „X“, o skaitmenis – „0“. Duomenų teikėjas – AB „Regitra“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Register of Road Vehicles of Regitra AB shall store data on motor vehicles, with the exception of those specified in Article 27(7) of the Law of the Republic of Lithuania on Road Safety and their trailers. Collection data has been collected since 2005 and is updated daily. The dataset consists of a car make, model, and state number markup, replacing letters with “X” and numbers with “0”.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ValstybinisNumeris](ktpr/ValstybinisNumeris.md) | Tranporto priemonių valstybiniai numeriai pagal markę ir modelį | `4` | `vda_id` | — | `4` | AB „Regitra“ Kelių transporto priemonių registre kaupiami motorinių transporto priemonių, išskyrus nurodytų Lietuvos Respublikos saugaus eismo automobilių... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/ktpr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/regitra/ktpr (https://data.gov.lt/datasets/2749/)
