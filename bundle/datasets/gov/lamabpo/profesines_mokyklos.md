---
type: Dataset
title: "Priėmimo į profesinio mokymo įstaigas prašymų duomenys"
description: "Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į profesinio mokymo įstaigas Lietuvoje."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos"
tags: [gov, lamabpo, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2913/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lamabpo/profesines_mokyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priėmimo į profesinio mokymo įstaigas prašymų duomenys

Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į profesinio mokymo įstaigas Lietuvoje. Rinkinį sudaro trys komponentai: 1. Profesinio mokymo programų duomenys, 2. Priėmimo prašymų duomenys, 3. Priėmimo prašymus teikusių asmenų duomenys. Duomenų teikėjas: Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO). Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lamabpo/profesines_mokyklos`[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/profesiniu_prasymai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos` (`deployed`)[^manifest]
- **Provider:** `lamabpo` — Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO) *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2913/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos`[^dcat]
- **Portal Title (`@lt`):** Priėmimo prašymų į profesinio mokymo programas duomenys[^dcat]
- **Portal Title (`@en`):** Data on applications for vocational training programmes[^dcat]
- **Issued (`dct:issued`):** `2025-01-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2025-01-22` .. `2026-01-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie 2024 m. pateiktus priėmimo prašymus į profesinio mokymo įstaigas Lietuvoje. Rinkinį sudaro trys komponentai: 1. Profesinio mokymo programų duomenys, 2. Priėmimo prašymų duomenys, 3. Priėmimo prašymus teikusių asmenų duomenys. Duomenų teikėjas – Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on applications for vocational training programmes[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Programa](profesines_mokyklos/Programa.md) | Profesinio mokymo programų duomenys | `4` | `programos_id` | — | `20` | Pateikiami profesinio mokymo programų duomenys Lietuvos profesinio mokymo įstaigose. |
| [Prasymas](profesines_mokyklos/Prasymas.md) | Priėmimo prašymų į profesines mokyklas duomenys | `4` | `prasymo_id` | — | `11` | Lentelėje pateikiami priėmimo į profesinio mokymo įstaigas duomenys. |
| [Profilis](profesines_mokyklos/Profilis.md) | Priėmimo prašymus į profesinio mokymo įstaigas teikusių asmenų profilis | `4` | `asmens_id` | — | `10` | Lentelėje pateikiami demografiniai duomenys apie asmenis, teikusius priėmimo prašymus į profesinio mokymo įstaigas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lamabpo/profesines_mokyklos (https://data.gov.lt/datasets/2913/)
