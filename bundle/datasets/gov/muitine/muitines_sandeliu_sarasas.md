---
type: Dataset
title: "Muitinės sandėlių sąrašas"
description: "Rinkinyje pateikiamas Lietuvos teritorijoje esančių muitinės ir prekių laikinojo saugojimo sandėlių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_sarasas"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2833/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_sandeliu_sarasas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Muitinės sandėlių sąrašas

- **Namespace:** `datasets/gov/muitine/muitines_sandeliu_sarasas`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_sarasas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2833/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_sarasas`[^dcat]
- **Portal Title (`@lt`):** Muitinės sandėlių sąrašas[^dcat]
- **Portal Title (`@en`):** List of customs warehouses[^dcat]
- **Issued (`dct:issued`):** `2024-10-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-25` .. `2026-10-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiamas Lietuvos teritorijoje esančių muitinės ir prekių laikinojo saugojimo sandėlių sąrašas. Pateikiami duomenys apie tiek šiuo metu veikiančius, tiek jau neveikiančius sandėlius bei jų adresai, aprašymai, koordinatės, leidimo steigti sandėlį suteikimo ir leidimo pripažinimo negaliojančiu datos ir t.t. Duomenys pateikiami nuo 1996 metų. Rinkinio vieną eilutę sudaro vienas sandėlis. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains a list of temporary storage warehouses of customs and goods located in the territory of Lithuania. Data shall be provided on both existing and existing warehouses and their addresses, descriptions, coordinates, dates of authorisation to establish a warehouse and invalidation of authorisation, etc. Data shall be provided from 1996 onwards. One row of the set consists of one warehouse. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sandelys](muitines_sandeliu_sarasas/Sandelys.md) | Muitinės sandėlių sąrašas | `4` | `vda_prime_key` | — | `27` | Rinkinyje pateikiamas Lietuvos teritorijoje esančių muitinės sandėlių sąrašas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_sandeliu_sarasas (https://data.gov.lt/datasets/2833/)
