---
type: Dataset
title: "Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos"
description: "Šiame rinkinyje pateikiamos Kauno miesto savivaldybės kasimo darbų lokacijos."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/kasimai"
tags: [gov, kauno_m_sav, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/kasimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/kasimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2708/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/kasimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos

- **Namespace:** `datasets/gov/kauno_m_sav/kasimai`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/kasimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/kasimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/kasimai` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2708/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/kasimai`[^dcat]
- **Portal Title (`@lt`):** Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos[^dcat]
- **Portal Title (`@en`):** Location of excavation works carried out in Kaunas City Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-07-19` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateikiamos Kauno miesto savivaldybės kasimo darbų lokacijos. Lokacijos pateikiamos WGS ir LKS koordinačių sistemose. Rinkinys jungiasi su „Kasimai“ rinkiniu https://data.gov.lt/datasets/2078/ per „prasymo_id“ raktą (kasimai.id = kasimoLokacija.prasymo_id). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This kit presents the location of excavation works of Kaunas City Municipality. Locations are presented in WGS and LKS coordinate systems. The kit connects to the Kasimai kit ' https://data.gov.lt/datasets/2078/ “ through the prasymo_id key (kasimai.id = casimoLokacija.prasymo_id).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KasimoLokacija](kasimai/KasimoLokacija.md) | Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos | `4` | `vda_id` | — | `12` | Šiame rinkinyje pateikiamos Kauno miesto savivaldybės kasimo darbų lokacijos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/kasimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/kasimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/kasimai (https://data.gov.lt/datasets/2708/)
