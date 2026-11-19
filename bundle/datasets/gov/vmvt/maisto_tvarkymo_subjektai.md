---
type: Dataset
title: "Duomenys apie maisto tvarkymo subjektus"
description: "Kaupiami duomenys apie maisto tvarkymo subjektus bei informacija apie jų vykdomą (-as) veiklą (-as), taip pat kaupiami šių subjektų kontrolės duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai"
tags: [gov, vmvt, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/maisto_tvarkymo_subjektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie maisto tvarkymo subjektus

- **Namespace:** `datasets/gov/vmvt/maisto_tvarkymo_subjektai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/802/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė maisto ir veterinarijos tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai`[^dcat]
- **Portal Title (`@lt`):** Maisto informacinės sistemos duomenys apie maisto tvarkymo subjektus[^dcat]
- **Portal Title (`@en`):** Food information system[^dcat]
- **Issued (`dct:issued`):** `2023-05-23`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2020-06-10` .. `2023-05-24`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kaupiami duomenys apie maisto tvarkymo subjektus bei informacija apie jų vykdomą (-as) veiklą (-as), taip pat kaupiami šių subjektų kontrolės duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on food business operators and information on their activity (ies) are collected, as well as control data on these entities.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](maisto_tvarkymo_subjektai/Subjektas.md) | Maisto tvarkymo subjektai | `3` | — | — | `15` | — |
| [AsortimentoKlasifikatorius](maisto_tvarkymo_subjektai/AsortimentoKlasifikatorius.md) | Produkto asortimento klasifikatorius pagal VMVT FIS | `4` | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/maisto_tvarkymo_subjektai (https://data.gov.lt/datasets/802/)
