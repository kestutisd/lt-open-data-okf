---
type: Dataset
title: "Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius"
description: "Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas"
resource: "https://get.data.gov.lt/datasets/gov/pagd/pranesimai"
tags: [gov, pagd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pagd/pranesimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2939/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/pranesimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius

Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas[^manifest]

- **Namespace:** `datasets/gov/pagd/pranesimai`[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/pranesimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/pranesimai` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2939/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pagd/pranesimai`[^dcat]
- **Portal Title (`@lt`):** Trumposios žinutės informuojančios gyventojus apie grėsmę keliančius įvykius[^dcat]
- **Portal Title (`@en`):** Information on message-informing residents about threats and their areas[^dcat]
- **Issued (`dct:issued`):** `2025-02-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-10-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie Priešgaisrinės apsaugos ir gelbėjimo departamento gyventojams siunčiamas trumpąsias žinutes, informuojančias apie grėsmę keliančius įvykius ir jų zonas. Informacija renkama nuo 2012 metų. Duomenų teikėjas – Priešgaisrinės apsaugos ir gelbėjimo departamentas prie Vidaus reikalų ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall contain information on short messages sent to the residents of the Fire and Rescue Department informing them of the events posing a threat and their zones. Information has been gathering since 2012. Data provider shall mean the Fire and Rescue Department under the Ministry of Internal Affairs of the Interior. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pranesimas](pranesimai/Pranesimas.md) | Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius | `4` | `issiustu_pranesimu_id` | — | `7` | Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/pranesimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/pranesimai (https://data.gov.lt/datasets/2939/)
