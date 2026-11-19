---
type: Dataset
title: "Knygomatai"
description: "Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai, jų adresų koordinatės."
resource: "https://get.data.gov.lt/datasets/gov/lnb/knygomatai"
tags: [gov, lnb, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lnb/knygomatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2624/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/knygomatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Knygomatai

- **Namespace:** `datasets/gov/lnb/knygomatai`[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/knygomatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/knygomatai` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2624/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lnb/knygomatai`[^dcat]
- **Portal Title (`@lt`):** Knygomatai[^dcat]
- **Portal Title (`@en`):** Bookmakers[^dcat]
- **Issued (`dct:issued`):** `2024-04-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-11-19` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai, jų adresų koordinatės. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Books administered by the Martynas Mažvydas Library LIBIS, their address coordinates.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Knygomatas](knygomatai/Knygomatas.md) | Knygomatai | `4` | `vda_id` | — | `9` | Martyno Mažvydo bibliotekos LIBIS IS administruojami knygomatai. |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/knygomatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/knygomatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/knygomatai (https://data.gov.lt/datasets/2624/)
