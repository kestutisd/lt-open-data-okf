---
type: Dataset
title: "Valstybinės veterinarinės kontrolės subjektų duomenys"
description: "Maisto tvarkymo subjektų, viešojo maitinimo įmonių - kavinių, užkandinių ir restoranų - veiklos atitikties higienos reikalavimams vertinimas atliekant planinius patikrinimus."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai"
tags: [gov, vmvt, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1679/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/kontroles_subjektai"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# Valstybinės veterinarinės kontrolės subjektų duomenys

- **Namespace:** `datasets/gov/vmvt/kontroles_subjektai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/kontroles_subjektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1679/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė maisto ir veterinarijos tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai`[^dcat]
- **Portal Title (`@lt`):** Viešojo maitinimo įmonių atitikties higienos reikalavimams vertinimas[^dcat]
- **Portal Title (`@en`):** Hygiene assessment of catering establishments -[^dcat]
- **Issued (`dct:issued`):** `2023-05-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-25`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2022-06-09` .. `2023-05-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Maisto tvarkymo subjektų, viešojo maitinimo įmonių - kavinių, užkandinių ir restoranų - veiklos atitikties higienos reikalavimams vertinimas atliekant planinius patikrinimus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Hygiene assessment of the compliance of food business operators, public catering establishments - cafes, cafeterias and restaurants - with routine inspections.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](kontroles_subjektai/Subjektas.md) | Valstybinės veterinarinės kontrolės subjektai | `4` | `vet_pat_nr` | — | `7` | — |
| [VeiklosKlasifikatorius](kontroles_subjektai/VeiklosKlasifikatorius.md) | VMVT veiklos klasifikatorius | `4` | `kodas` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/kontroles_subjektai (https://data.gov.lt/datasets/1679/)
