---
type: Dataset
title: "Muitinės prievolininkų registras"
description: "Ekonominės veiklos vykdytojai ir kiti asmenys įtraukti į muitinės prievolininkų registrą"
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_prievolininku_registras"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_prievolininkai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_prievolininkai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2705/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_prievolininku_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Muitinės prievolininkų registras

Ekonominės veiklos vykdytojai ir kiti asmenys įtraukti į muitinės prievolininkų registrą[^manifest]

- **Namespace:** `datasets/gov/muitine/muitines_prievolininku_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_prievolininkai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_prievolininkai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_prievolininku_registras` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2705/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/muitines_prievolininku_registras`[^dcat]
- **Portal Title (`@lt`):** Ekonominės veiklos vykdytojai ir kiti asmenys įrašyti į Muitinės prievolininkų sąrašą[^dcat]
- **Portal Title (`@en`):** Economic operators and other persons entered in the List of Customs Companies[^dcat]
- **Issued (`dct:issued`):** `2024-07-16`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-07-16` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Publikuojama informacija apie Lietuvos ir kitų šalių Ekonominės veiklos vykdytojus bei kitus asmenis, kurie įtraukti į Lietuvos Muitinės prievolininkų registrą nuo 2009 metų. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information about economic operators of Lithuania and other countries and other persons entered in the Register of Customs Companies of Lithuania since 2009 shall be published[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MuitinesPrievolininkas](muitines_prievolininku_registras/MuitinesPrievolininkas.md) | Ekonominės veiklos vykdytojai įtraukti į MPR | `4` | `muitines_prievolininko_id` | — | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_prievolininkai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_prievolininkai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_prievolininku_registras (https://data.gov.lt/datasets/2705/)
