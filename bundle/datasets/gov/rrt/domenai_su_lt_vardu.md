---
type: Dataset
title: "Domenai su Lietuvos vardu"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos duomenys apie prašymus registruoti domenus su Lietuvos vardu."
resource: "https://get.data.gov.lt/datasets/gov/rrt/domenai_su_lt_vardu"
tags: [gov, rrt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/domenai_su_lt_vardu.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rrt/domenai_su_lt_vardu.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2724/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rrt/domenai_su_lt_vardu"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Domenai su Lietuvos vardu

- **Namespace:** `datasets/gov/rrt/domenai_su_lt_vardu`[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/domenai_su_lt_vardu.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/domenai_su_lt_vardu.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/domenai_su_lt_vardu` (`deployed`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2724/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rrt/domenai_su_lt_vardu`[^dcat]
- **Portal Title (`@lt`):** Domenai su Lietuvos vardu[^dcat]
- **Portal Title (`@en`):** Domains with Lithuanian name[^dcat]
- **Issued (`dct:issued`):** `2024-07-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-07-30` .. `2026-07-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos duomenys apie prašymus registruoti domenus su Lietuvos vardu. Tai galioja domenams, kurie varduose prieš aukščiausiojo lygio domeną „.lt“ turi Lietuvos vardą. Šiems domenams reikalingas atskiras leidimas. Visos taisyklės yra apibrėžtos Lietuvos Respublikos Vyriausybės nutarime „Dėl Lietuvos vardo vartojimo interneto domenų varduose taisyklių patvirtinimo“. Laiko aprėptis nuo 2009 m. spalio mėn. Fizinių asmenų vardai šifruoti. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table contains data of the Communications Regulatory Authority of the Republic of Lithuania on applications for registration of domains bearing the name of Lithuania. This applies to domains that have a Lithuanian name in their names before the top-level domain. lt. These domains require a separate permission. All rules are defined in the Resolution of the Government of the Republic of Lithuania on the Approval of Rules for the Use of the Lithuanian Name in Internet Domain Names. Time coverage since October 2009. The names of natural persons are anonymised by leaving only initials.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LietuvosVardasDomenas](domenai_su_lt_vardu/LietuvosVardasDomenas.md) | Domenai su Lietuvos vardu | `4` | `iraso_id` | — | `6` | "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos duomenys apie prašymus registruoti domenus su Lietuvos vardu. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/domenai_su_lt_vardu.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/domenai_su_lt_vardu.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rrt/domenai_su_lt_vardu (https://data.gov.lt/datasets/2724/)
