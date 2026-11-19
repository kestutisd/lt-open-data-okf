---
type: Dataset
title: "Projekto „Mokykis visą gyvenimą!“ dalyvių ir kursų duomenys"
description: "\"Rinkinyje pateikiama informacija apie projekto „Mokykis visą gyvenimą!“ (MVG) dalyvius ir vykdomas kursų programas."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa"
tags: [gov, lamabpo, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2915/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lamabpo/mvg_programa"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Projekto „Mokykis visą gyvenimą!“ dalyvių ir kursų duomenys

"Rinkinyje pateikiama informacija apie projekto „Mokykis visą gyvenimą!“ (MVG) dalyvius ir vykdomas kursų programas. Rinkinį sudaro dvi lentelės – „MVG dalyvių duomenys“ ir „MVG kursų duomenys“. Duomenų teikėjas – Lietuvos aukštųjų mokyklų asociacija bendram priėmimui organizuoti (LAMA BPO). Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/lamabpo/mvg_programa`[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/mvg_programa.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa` (`deployed`)[^manifest]
- **Provider:** `lamabpo` — Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO) *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2915/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa`[^dcat]
- **Portal Title (`@lt`):** LAMBA BPO programos „Mokykis visą gyvenimą“ duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** LAMBA BPO Lifelong Learning Data Set[^dcat]
- **Issued (`dct:issued`):** `2025-02-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-06-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie projekto „Mokykis visą gyvenimą!“ (MVG) dalyvius ir vykdomas kursų programas. Rinkinį sudaro dvi lentelės – „MVG dalyvių duomenys“ ir „MVG kursų duomenys“. Duomenų teikėjas – Lietuvos aukštųjų mokyklų asociacija bendram priėmimui organizuoti (LAMA BPO). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

LAMBA BPO Lifelong Learning Data Set[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KursoDalyvis](mvg_programa/KursoDalyvis.md) | MVG dalyvių duomenys | `4` | `vda_prime_key` | — | `10` | "Lentelėje pateikiami MVG programoje dalyvaujančių ar praeityje dalyvavusių dalyvių duomenys. |
| [KursoGrupe](mvg_programa/KursoGrupe.md) | MVG kursų duomenys | `4` | `kursu_grupes_id` | — | `22` | "Lentelėje pateikiami projekte „Mokykis visą gyvenimą!“ (MVG) vykdomus kursus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lamabpo/mvg_programa (https://data.gov.lt/datasets/2915/)
