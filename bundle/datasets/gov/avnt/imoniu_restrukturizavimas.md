---
type: Dataset
title: "Įmonių restruktūrizavimo ataskaitų duomenys"
description: "Procedūrų ir finansiniai duomenys apie restruktūrizavimo procesus (duomenys apie įmonę, procedūrų datos, turtas, kreditorių reikalavimai, darbuotojų skaičius)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas"
tags: [gov, avnt, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1333/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_restrukturizavimas"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# Įmonių restruktūrizavimo ataskaitų duomenys

- **Namespace:** `datasets/gov/avnt/imoniu_restrukturizavimas`[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/imoniu_restrukturizavimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1333/`[^dcat]
- **Publisher (`dct:publisher`):** Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba prie Lietuvos Respublikos finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas`[^dcat]
- **Portal Title (`@lt`):** Įmonių restruktūrizavimo ataskaitų duomenys[^dcat]
- **Portal Title (`@en`):** Details of the restructuring process[^dcat]
- **Issued (`dct:issued`):** `2022-07-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-25`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2022-07-20` .. `2026-02-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Procedūrų ir finansiniai duomenys apie restruktūrizavimo procesus (duomenys apie įmonę, procedūrų datos, turtas, kreditorių reikalavimai, darbuotojų skaičius). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Procedural and financial data on restructuring processes (company data, dates of proceedings, assets, creditors' claims, number of employees)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [RestrukturizavimoAtaskaitosDatos](imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosDatos.md) | Įmonių restruktūrizavimo ataskaitų duomenys | — | — | — | `16` | — |
| [RestrukturizavimoAtaskaitosFinansiniai](imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai.md) | — | `4` | — | — | `11` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_restrukturizavimas (https://data.gov.lt/datasets/1333/)
