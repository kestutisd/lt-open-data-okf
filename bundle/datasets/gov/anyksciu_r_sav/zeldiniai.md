---
type: Dataset
title: "Anykščių miesto želdiniai ir želdynai"
description: "Informacija apie Anykščių miesto želdinius ir želdynus"
resource: "https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai"
tags: [gov, anyksciu_r_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2900/"
    title: "data.gov.lt DCAT-AP — datasets/gov/anyksciu_r_sav/zeldiniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Anykščių miesto želdiniai ir želdynai

Informacija apie Anykščių miesto želdinius ir želdynus[^manifest]

- **Namespace:** `datasets/gov/anyksciu_r_sav/zeldiniai`[^manifest]
- **Manifest CSV:** [datasets/gov/anyksciu_r_sav/zeldiniai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai` (`deployed`)[^manifest]
- **Provider:** `anyksciu_r_sav` — Anykščių rajono savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2900/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai`[^dcat]
- **Portal Title (`@lt`):** Anykščių miesto želdiniai ir želdynai[^dcat]
- **Portal Title (`@en`):** Greenery and green areas of the city of Anykščiai[^dcat]
- **Issued (`dct:issued`):** `2024-12-16`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-05` .. `2026-10-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie Anykščių miesto želdinius (medžius, krūmus, augalus ir pan.) ir želdynus, esančius prie gatvių, parkuose ir skveruose, viešuosiuose soduose ir kitur. Informacija kaupiama nuo 2020 metų. Duomenų teikėjas – Anykščių rajono savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data collection contains information about Anykščiai city plantations (trees, bushes, plants, etc.) and plantations located near streets, parks and squares, public gardens and elsewhere. Information has been gathering since 2020. Data provider – Anyksciai District. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Zeldinys](zeldiniai/Zeldinys.md) | Anykščių miesto želdiniai | `4` | `objekto_id` | — | `12` | Informacija apie Anykščių miesto želdinius |
| [Zeldynas](zeldiniai/Zeldynas.md) | Anykščių miesto želdynai | `4` | `objekto_id` | — | `10` | Informacija apie Anykščių miesto želdynus |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/anyksciu_r_sav/zeldiniai (https://data.gov.lt/datasets/2900/)
