---
type: Dataset
title: "Tarmių ribos"
description: "Duomenų rinkinyje pateikiamos lietuvių kalbos tarmių ribų geometrijos (https://maps.lki.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos"
tags: [gov, lki, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lki/tarmiu_ribos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2936/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/tarmiu_ribos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Tarmių ribos

- **Namespace:** `datasets/gov/lki/tarmiu_ribos`[^manifest]
- **Manifest CSV:** [datasets/gov/lki/tarmiu_ribos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2936/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos`[^dcat]
- **Portal Title (`@lt`):** Tarmių ribos[^dcat]
- **Portal Title (`@en`):** Dialect Limits[^dcat]
- **Issued (`dct:issued`):** `2025-02-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2025-02-19` .. `2026-04-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiamos lietuvių kalbos tarmių ribų geometrijos (https://maps.lki.lt/). Rinkinį sudaro: tarmės pavadinimas, trumpinys ir tarmės ribų geometrija, pateikta dvejetainiu, LKS ir WGS84 geometrijos formatais. Šis duomenų rinkinys šiuo metu pateikiamas tik informaciniais tikslais ir negali būti naudojamas moksliniams tyrimams. Jame gali būti preliminarių ar pasenusių duomenų. Atnaujinimas, apie kurį bus pranešta kartu su naujausia versija, planuojamas 2026 m. balandį. Duomenų teikėjas – Lietuvių kalbos institutas (LKI). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set provides geometry of the boundaries of the Lithuanian dialects (https://maps.lki.lt/). The set consists of: dialect name, abbreviation, and dialect boundary geometry, presented in binary, LKS, and WGS84 geometry formats. This dataset is currently only available for informational purposes and cannot be used for research purposes. It may contain preliminary or outdated data. The update, which will be reported along with the latest version, is planned for April 2026. Data provider – Lithuanian Language Institute (LKI). Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TarmesRiba](tarmiu_ribos/TarmesRiba.md) | Tarmių ribos | `4` | `tarmes_riba_id` | — | `4` | Rinkinyje pateikiamos lietuviškų tarmių ribų geometrijos (https://maps.lki.lt/). |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/tarmiu_ribos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/tarmiu_ribos (https://data.gov.lt/datasets/2936/)
