---
type: Dataset
title: "Pridėtinės vertės mokesčio deklaracijų duomenų rinkinys"
description: "PVM deklaracijų (forma FR0600) duomenys, agreguoti pagal ekonominės veiklos skyrius."
resource: "https://get.data.gov.lt/datasets/gov/vmi/pvm_deklaracijos"
tags: [gov, vmi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/pvm_deklaracijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/pvm_deklaracijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1163/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/pvm_deklaracijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pridėtinės vertės mokesčio deklaracijų duomenų rinkinys

- **Namespace:** `datasets/gov/vmi/pvm_deklaracijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/pvm_deklaracijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/pvm_deklaracijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/pvm_deklaracijos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1163/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/pvm_deklaracijos`[^dcat]
- **Portal Title (`@lt`):** PVM deklaracijų duomenys[^dcat]
- **Portal Title (`@en`):** VAT declarations (FR0600)[^dcat]
- **Issued (`dct:issued`):** `2022-07-01`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-04-20` .. `2026-10-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

PVM deklaracijų (forma FR0600) duomenys, agreguoti pagal ekonominės veiklos skyrius. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data of FR0600 declarations, aggregated by economic activity[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VtsFr0600Mainai](pvm_deklaracijos/VtsFr0600Mainai.md) | FR0600_DUOMENYS | — | — | — | `30` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/pvm_deklaracijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/pvm_deklaracijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/pvm_deklaracijos (https://data.gov.lt/datasets/1163/)
