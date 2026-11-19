---
type: Dataset
title: "Išleidžiamų ir perduodamų teršalų duomenys"
description: "Duomenys apie įmonių išleidžiamus ir perduodamus teršalus."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai"
tags: [gov, aaa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Išleidžiamų ir perduodamų teršalų duomenys

- **Namespace:** `datasets/gov/aaa/isleid_perd_tersalai`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `7` (7 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/665/`[^dcat]
- **Publisher (`dct:publisher`):** Aplinkos apsaugos agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai`[^dcat]
- **Portal Title (`@lt`):** Išleidžiamų ir perduodamų teršalų duomenys[^dcat]
- **Portal Title (`@en`):** Data on emissions and transfers[^dcat]
- **Issued (`dct:issued`):** `2023-04-18`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-04-14` .. `2025-01-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie įmonių išleidžiamus ir perduodamus teršalus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on emissions and transfers of pollutants by enterprises[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [EmissionsToAir](isleid_perd_tersalai/EmissionsToAir.md) | Emisijos į orą | `4` | — | — | `5` | Didelių kurą deginančių įrenginių duomenys |
| [EnergyInput](isleid_perd_tersalai/EnergyInput.md) | Energijos sąnaudos | `4` | — | — | `8` | — |
| [OffSitePollutantTransfer](isleid_perd_tersalai/OffSitePollutantTransfer.md) | Teršalų perdavimas už objekto ribų | `4` | — | — | `7` | — |
| [OffsiteWasteTransfer](isleid_perd_tersalai/OffsiteWasteTransfer.md) | Atliekų perdavimas už objekto ribų | `4` | — | — | `10` | — |
| [PollutantRelease](isleid_perd_tersalai/PollutantRelease.md) | Išleidžiamų teršalų duomenys | `4` | — | — | `8` | — |
| [ProductionFacilityReport](isleid_perd_tersalai/ProductionFacilityReport.md) | Gamybos įrengimų kompleksų duomenys | `4` | — | — | `4` | — |
| [ProductionInstallationPartReport](isleid_perd_tersalai/ProductionInstallationPartReport.md) | Gamybos įrengimų duomenys | `4` | — | — | `8` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai (https://data.gov.lt/datasets/665/)
