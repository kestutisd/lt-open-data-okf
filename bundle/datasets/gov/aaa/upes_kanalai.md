---
type: Dataset
title: "Upių, kanalų duomenys"
description: "Upių, kanalų duomenys: unikalus identifikatorius, identifikavimo kodas, pavadinimas, vandens telkinio registravimo ir redagavimo data, vandens telkinio kategorijos pavadinimo kodas, upės pabaseinio arba baseino, kuriame yra vandens objektas, kodas, vyresniosios upės, į kurią..."
resource: "https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai"
tags: [gov, aaa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/upes_kanalai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1779/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/upes_kanalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Upių, kanalų duomenys

- **Namespace:** `datasets/gov/aaa/upes_kanalai`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/upes_kanalai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1779/`[^dcat]
- **Publisher (`dct:publisher`):** Aplinkos apsaugos agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/upes_kanalai`[^dcat]
- **Portal Title (`@lt`):** Upių, kanalų duomenys[^dcat]
- **Portal Title (`@en`):** Data of rivers and canals[^dcat]
- **Issued (`dct:issued`):** `2023-06-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-03-01` .. `2025-07-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Upių, kanalų duomenys: unikalus identifikatorius, identifikavimo kodas, pavadinimas, vandens telkinio registravimo ir redagavimo data, vandens telkinio kategorijos pavadinimo kodas, upės pabaseinio arba baseino, kuriame yra vandens objektas, kodas, vyresniosios upės, į kurią įteka upės, unikalus identifikatorius, žiočių centro X ir Y koordinatės LKS 94 koordinačių sistemoje, įtekėjimo į vyresniąją upę krantas, upės įtekėjimo eiliškumas, ilgis Lietuvos teritorijoje, vidutinis daugiametis vandens debitas upės žiotyse. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data for rivers and canals: identification code, name, date of registration, date of the editing of the water body, water body category name code, the code of the river sub-basin or basin in which the water body is located, the unique identifier of the older river into which the rivers flow, X and Y coordinates of the centre of the mouth in the LKS 94 coordinate system, the bank of the inflow into the older river, sequence of inflow of the river, length in the territory of Lithuania, average multi-year water flow at the mouth of the river.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [UpeKanalas](upes_kanalai/UpeKanalas.md) | Upės ir kanalai | `2` | — | — | `14` | Pagal Upių, ežerų ir tvenkinių kadastro nuostatus, patvirtintų Lietuvos Respublikos Vyriausybės 2000-09-19 nutarimu Nr. 1114, kadastre kaupiama informacija... |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/upes_kanalai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upes_kanalai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/upes_kanalai (https://data.gov.lt/datasets/1779/)
