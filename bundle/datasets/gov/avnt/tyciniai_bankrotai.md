---
type: Dataset
title: "Duomenys apie tyčinius bankrotus"
description: "Įmonių sąrašas, kurioms bankrotas pripažintas tyčiniu (duomenys apie įmonę, procedūrų datos)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai"
tags: [gov, avnt, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/avnt/tyciniai_bankrotai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1334/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/tyciniai_bankrotai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie tyčinius bankrotus

- **Namespace:** `datasets/gov/avnt/tyciniai_bankrotai`[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/tyciniai_bankrotai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1334/`[^dcat]
- **Publisher (`dct:publisher`):** Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba prie Lietuvos Respublikos finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie tyčinius bankrotus[^dcat]
- **Portal Title (`@en`):** Data on intentional bankruptcies[^dcat]
- **Issued (`dct:issued`):** `2022-04-29`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2022-04-29` .. `2025-11-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Įmonių sąrašas, kurioms bankrotas pripažintas tyčiniu (duomenys apie įmonę, procedūrų datos). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

List of companies for which bankruptcy has been declared intentional (company data, procedural dates)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TycinisBankrotas](tyciniai_bankrotai/TycinisBankrotas.md) | Duomenys apie tyčinius bankrotus | — | — | — | `9` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/tyciniai_bankrotai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/tyciniai_bankrotai (https://data.gov.lt/datasets/1334/)
