---
type: Dataset
title: "Lietuvos Respublikos visuotinio žemės ūkio surašymo rezultatų duomenys"
description: "Pateikiami apskričių, gyvenamųjų vietovių, savivaldybių, seniūnijų taškiniai geoerdviniai duomenys, remiantis Lietuvos Respublikos 2010 m. , 2020 m. visuotiniu žemės ūkio surašymu."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis"
tags: [gov, lsd, deployed, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1909/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lietuvos Respublikos visuotinio žemės ūkio surašymo rezultatų duomenys

- **Namespace:** `datasets/gov/lsd/zemes_ukis`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1909/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos visuotinio žemės ūkio surašymo rezultatų duomenys[^dcat]
- **Portal Title (`@en`):** Agricultural census data[^dcat]
- **Issued (`dct:issued`):** `2022-10-27`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DECENNIAL` (`http://publications.europa.eu/resource/authority/frequency/DECENNIAL`)[^dcat]
- **Distribution Date Span:** `2022-04-18` .. `2022-04-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami apskričių, gyvenamųjų vietovių, savivaldybių, seniūnijų taškiniai geoerdviniai duomenys, remiantis Lietuvos Respublikos 2010 m. , 2020 m. visuotiniu žemės ūkio surašymu. Surašymas vykdomas kas 10 metų. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Based on the Agricultural Census of the Republic of Lithuania 2010, point geospatial data of counties, residential areas, municipalities and elderships are presented. The census is conducted every 10 years.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ApsGeoDuom2010](zemes_ukis/ApsGeoDuom2010.md) | Apskričių taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių surašymu 2010 m. | `4` | `objectid` | — | `11` | — |
| [GyvVietTaskas2010](zemes_ukis/GyvVietTaskas2010.md) | Gyvenamųjų vietovių taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių surašymu 2010 m. | `4` | `objectid` | — | `14` | — |
| [SavTaskDuom2010](zemes_ukis/SavTaskDuom2010.md) | Savivaldybių taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkio surašymu 2010 m. | `4` | `objectid` | — | `12` | — |
| [SenGeoDuom2010](zemes_ukis/SenGeoDuom2010.md) | Seniūnijų taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių sura | `4` | `objectid` | — | `13` | — |
| [ZemesUkioTaskas2020](zemes_ukis/ZemesUkioTaskas2020.md) | Žemės ūkio surašymo taškiniai duomenys | `4` | — | `open` | `30` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis (https://data.gov.lt/datasets/1909/)
