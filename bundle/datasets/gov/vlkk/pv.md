---
type: Dataset
title: "Vietovardžių duomenys"
description: "Valstybinės lietuvių kalbos komisijos (VLKK) pasvetainė „Pasaulio vietovardžiai“ kaupia sulietuvintus pasaulio objektų vietovardžius."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/pv"
tags: [gov, vlkk, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/pv.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlkk/pv.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2703/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlkk/pv"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vietovardžių duomenys

- **Namespace:** `datasets/gov/vlkk/pv`[^manifest]
- **Manifest CSV:** [datasets/gov/vlkk/pv.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/pv.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/pv` (`deployed`)[^manifest]
- **Provider:** `vlkk` — Valstybinė lietuvių kalbos komisija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2703/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlkk/pv`[^dcat]
- **Portal Title (`@lt`):** Vietovardžių duomenys[^dcat]
- **Portal Title (`@en`):** Location Name Data[^dcat]
- **Issued (`dct:issued`):** `2024-07-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-07-15` .. `2025-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybinės lietuvių kalbos komisijos (VLKK) pasvetainė „Pasaulio vietovardžiai“ kaupia sulietuvintus pasaulio objektų vietovardžius. Duomenų pagrindas sudarytas iš Mokslo ir enciklopedijų leidybos centro (MELC) parengto ir išleisto žodyno. Duomenys kaupiami nuo 2014 m. ir yra atnaujinami iki šiol. Duomenys apima objekto identifikatorių, apjungiantį jo pavadinimus originalo ir lietuvių kalbomis, pavadinimus su ir be kirčio ženklų, požymį, ar pavadinimas sulietuvintas, objekto rūšį, šalį, žemyną, lokalizaciją, skirtą nurodyti objekto vietovę bei paieškų skaičių, anksčiausią ir vėliausią datas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The website of the State Commission for Lithuanian Language (VLKK) “World Site Names” collects merged names of objects of the world. The data base consists of a dictionary prepared and published by the Centre for Science and Encyclopaedia Publishing (MELC). Data have been collected since 2014 and are up-to-date. The data includes an object identifier that combines its names in the original and Lithuanian languages, names with and without accents, an indication of whether the name is merged, the object type, country, continent, location to indicate the location of the object and the number of searches, the earliest and most recent dates.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Vietovardis](pv/Vietovardis.md) | Vietovardžių duomenys | `4` | `vda_id` | `open` | `12` | Valstybinės lietuvių kalbos komisijos (VLKK) pasvetainė „Pasaulio vietovardžiai“ kaupia sulietuvintus pasaulio objektų vietovardžius. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/pv.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/pv.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlkk/pv (https://data.gov.lt/datasets/2703/)
