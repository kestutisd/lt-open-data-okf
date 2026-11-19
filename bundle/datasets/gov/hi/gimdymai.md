---
type: Dataset
title: "Duomenys apie gimdymus Lietuvoje."
description: "Duomenų rinkinyje pateikiama informacija apie gimdymus Lietuvoje nuo 2021m."
resource: "https://get.data.gov.lt/datasets/gov/hi/gimdymai"
tags: [gov, hi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/hi/gimdymai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2732/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/gimdymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Duomenys apie gimdymus Lietuvoje.

Duomenų rinkinyje pateikiama informacija apie gimdymus Lietuvoje nuo 2021m. Rinkinio objektas - vienavaisis arba daugiavaisis gimdymas. Duomenys surinkti iš statistinių formų Nėščiosios ir negyvagimio kortelė Nr.2016-10-07_Nr_V-1149_forma+010-2-1a ir Nėščiosios ir negyvagimio kortelė Nr.2016-10-07_Nr_V-1149_forma+010-1-1a. Pateikiama informacija apie gimdymo datą, gimdyvės kilmės rajoną, gimdymo vietą, bendrą vaisių skaičių gimdymo metu bei gimdyvės RhD antigeną. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/hi/gimdymai`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/gimdymai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gimdymai` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2732/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/gimdymai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie gimdymus Lietuvoje[^dcat]
- **Portal Title (`@en`):** Data on births in Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-08-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-08-01` .. `2024-09-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie gimdymus Lietuvoje nuo 2021m. Rinkinio objektas - vienavaisis arba daugiavaisis gimdymas. Duomenys surinkti iš statistinių formų Nėščiosios ir negyvagimio kortelė Nr.2016-10-07_Nr_V-1149_forma+010-2-1a ir Nėščiosios ir negyvagimio kortelė Nr.2016-10-07_Nr_V-1149_forma+010-1-1a. Pateikiama informacija apie gimdymo datą, gimdyvės kilmės rajoną, gimdymo vietą, bendrą vaisių skaičių gimdymo metu bei gimdyvės RhD antigeną. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set contains information about births in Lithuania from 2021. The object of the kit is single or multiple birth. The data are collected from statistical forms Pregnancy and Dead Cards No. 2016-10-07_Nr_V-1149_forma +010-2-1a and Pregnancy and Dead Cards No. 2016-10-07_Nr_V-1149_forma +010-1-1a. Information on date of birth, maternal area, place of birth, total number of fruit at birth and maternal RhD antigen shall be provided. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Gimimas](gimdymai/Gimimas.md) | Duomenys apie gimdymus Lietuvoje. | `4` | `vda_id` | — | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gimdymai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/gimdymai (https://data.gov.lt/datasets/2732/)
