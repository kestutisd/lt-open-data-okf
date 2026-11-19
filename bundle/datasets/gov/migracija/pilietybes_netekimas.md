---
type: Dataset
title: "Duomenys apie pilietybės netekimą"
description: "Duomenys apie asmenis, kurie neteko Lietuvos Respublikos pilietybės jos atsisakius ar įgijus kitos valstybės pilietybę."
resource: "https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas"
tags: [gov, migracija, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/migracija/pilietybes_netekimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1946/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/pilietybes_netekimas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie pilietybės netekimą

Duomenys apie asmenis, kurie neteko Lietuvos Respublikos pilietybės jos atsisakius ar įgijus kitos valstybės pilietybę.[^manifest]

- **Namespace:** `datasets/gov/migracija/pilietybes_netekimas`[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/pilietybes_netekimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1946/`[^dcat]
- **Publisher (`dct:publisher`):** Migracijos departamentas prie Lietuvos Respublikos vidaus reikalų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie pilietybės netekimą[^dcat]
- **Portal Title (`@en`):** Data on loss of citizenship[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-03` .. `2026-06-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie asmenis, kurie neteko Lietuvos Respublikos pilietybės jos atsisakius ar įgijus kitos valstybės pilietybę. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on persons who have lost the citizenship of the Republic of Lithuania after renouncing it or acquiring the citizenship of another state[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Prasymas](pilietybes_netekimas/Prasymas.md) | Duomenys apie Lietuvos Respublikos piliečių prašymus panaikinti Lietuvos Respublikos pilietybę. | `4` | `id` | `open` | `5` | — |
| [Sprendimas](pilietybes_netekimas/Sprendimas.md) | Duomenys apie Migracijos departamento sprendimus panaikinti Lietuvos Respublikos pilietybę. | `4` | `id` | `open` | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/pilietybes_netekimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/pilietybes_netekimas (https://data.gov.lt/datasets/1946/)
