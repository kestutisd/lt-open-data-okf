---
type: Dataset
title: "Duomenys apie teritorijų planavimo vadovų atestatus (fiziniai asmenys)"
description: "Duomenys apie teritorijų planavimo vadovų atestatus."
resource: "https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai"
tags: [gov, ssva, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1317/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/tpv_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Duomenys apie teritorijų planavimo vadovų atestatus (fiziniai asmenys)

- **Namespace:** `datasets/gov/ssva/tpv_atestatai`[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1317/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ssva/tpv_atestatai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie teritorijų planavimo vadovų atestatus[^dcat]
- **Portal Title (`@en`):** Data on certificates of spatial planning managers[^dcat]
- **Issued (`dct:issued`):** `2023-09-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-04-27` .. `2026-05-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie teritorijų planavimo vadovų atestatus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on certificates of spatial planning managers[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Atestatas](tpv_atestatai/Atestatas.md) | Teritorijų planavimo vadovų atestatai | `4` | `nr` | — | `8` | — |
| [Priemone](tpv_atestatai/Priemone.md) | — | `4` | `vda_id` | `open` | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/teritoriju_planavimo_vadovu_atestatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/tpv_atestatai (https://data.gov.lt/datasets/1317/)
