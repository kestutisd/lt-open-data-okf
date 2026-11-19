---
type: Dataset
title: "Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius"
description: "Lietuvos Respublikos Seimo sesijų tvarkaraštis."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos"
tags: [gov, lrsk, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2610/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/kadencijos_sesijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius

- **Namespace:** `datasets/gov/lrsk/kadencijos_sesijos`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/kadencijos_sesijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2610/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius[^dcat]
- **Portal Title (`@en`):** Classification of the term and session of the Seimas of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-04-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2024-04-15` .. `2026-08-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos Seimo sesijų tvarkaraštis. Pateikiama eilinių ir neeilinių sesijų pradžia ir pabaiga bei kadencijos, kuriai priklauso sesija, id. Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis. Duomenų teikėjas – Lietuvos Respublikos Seimo kanceliarija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Schedule of sessions of the Seimas of the Republic of Lithuania. The beginning and end of ordinary and extraordinary sessions and the id of the term of office to which the session belongs shall be presented. Schedule of term of office of the Seimas of the Republic of Lithuania with dates of commencement and expiry of term of office. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sesija](kadencijos_sesijos/Sesija.md) | Lietuvos Respublikos Seimo sesijų tvarkaraštis | `4` | `id` | — | `7` | Lietuvos Respublikos Seimo sesijų tvarkaraštis. |
| [Kadencija](kadencijos_sesijos/Kadencija.md) | Lietuvos Respublikos Seimo kadencijų tvarkaraštis | `4` | `id` | — | `3` | Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/kadencijos_sesijos (https://data.gov.lt/datasets/2610/)
