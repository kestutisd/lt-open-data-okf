---
type: Dataset
title: "Asmenys su negalia"
description: "Duomenų rinkinį sudaro asmenų su negalia duomenys pagal savivaldybę, seniūniją, lytį, amžiaus grupę, neįgalumo/ darbingumo lygį, gimimo šalį ir pašto kodą."
resource: "https://get.data.gov.lt/datasets/gov/datalab/asmenys_su_negalia"
tags: [gov, datalab, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/asmenys_su_negalia.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/datalab/asmenys_su_negalia.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/datalab/asmenys_su_negalia"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Asmenys su negalia

- **Namespace:** `datasets/gov/datalab/asmenys_su_negalia`[^manifest]
- **Manifest CSV:** [datasets/gov/datalab/asmenys_su_negalia.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/asmenys_su_negalia.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/datalab/asmenys_su_negalia` (`deployed`)[^manifest]
- **Provider:** `datalab` — Valstybės duomenų agentūra (DataLab) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3912/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/datalab/asmenys_su_negalia`[^dcat]
- **Portal Title (`@lt`):** Asmenys su negalia[^dcat]
- **Portal Title (`@en`):** Persons with disabilities[^dcat]
- **Issued (`dct:issued`):** `2025-10-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-10-21` .. `2025-10-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinį sudaro asmenų su negalia duomenys pagal savivaldybę, seniūniją, lytį, amžiaus grupę, neįgalumo/ darbingumo lygį, gimimo šalį ir pašto kodą. Duomenų šaltiniai: Asmens su negalia teisių apsaugos agentūros informacinė sistema Lietuvos Respublikos gyventojų registras Lietuvos Respublikos adresų registras Priedangų, kolektyvinių apsaugos statinių, evakavimo punktų ir sirenų duomenų vidinė informacinė sistema Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The dataset consists of data on persons with disabilities by municipality, neighborhood, gender, age group, disability/capacity for work level, country of birth and postal code. Data sources: Information System of the Agency for the Protection of the Rights of Persons with Disabilities Population Register of the Republic of Lithuania Address Register of the Republic of Lithuania Internal information system for data on shelters, collective protection structures, evacuation points and sirens Please contact atverimas@stat.gov.lt by e-mail for information. Please contact atviriduomenys@vssa.lt by e-mail for technical problems with the portal.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AsmuoSuNegalia](asmenys_su_negalia/AsmuoSuNegalia.md) | Asmuo su negalia | `4` | `vda_id` | — | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/datalab/asmenys_su_negalia.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/asmenys_su_negalia.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/datalab/asmenys_su_negalia (https://data.gov.lt/datasets/3912/)
