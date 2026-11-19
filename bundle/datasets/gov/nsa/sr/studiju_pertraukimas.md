---
type: Dataset
title: "Studentų studijų pertraukimai ir nutraukimai"
description: "Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš Studentų registro (SR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas"
tags: [gov, nsa, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/sr/studiju_pertraukimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2616/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/sr/studiju_pertraukimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Studentų studijų pertraukimai ir nutraukimai

- **Namespace:** `datasets/gov/nsa/sr/studiju_pertraukimas`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/sr/studiju_pertraukimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2616/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/sr/studiju_pertraukimas`[^dcat]
- **Portal Title (`@lt`):** Studentų studijų pertraukimai ir nutraukimai[^dcat]
- **Portal Title (`@en`):** Interruptions and interruptions of student studies[^dcat]
- **Issued (`dct:issued`):** `2024-04-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2026-04-05` .. `2026-10-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš Studentų registro (SR). Persidengiantys pertraukimai (pvz.: studentas pertraukė studijas 2021-09-04 - 2022-01-30 ir tuomet vėl 2022-01-31 - 2022-09-01) yra sutraukti į vieną laikotarpį. Duomenys kaupiami nuo 2010 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides data on student interruptions/interruptions from the Student Register (SR) by the National Education Agency (NSA). Overlapping interruptions (e.g. student interrupted studies 2021-09-04 - 2022-01-30 and then again 2022-01-31 - 2022-09-01) are drawn into one period. Data shall be collected from 2010 onwards.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pertraukimas](studiju_pertraukimas/Pertraukimas.md) | Studentų studijų pertraukimai ir nutraukimai | `4` | `iraso_id` | — | `16` | Lentelėje pateikti Nacionalinės švietimo agentūros (NŠA) studentų studijų pertraukimų / nutraukimų duomenys iš studentų registro (SR). |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/sr/studiju_pertraukimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/sr/studiju_pertraukimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/sr/studiju_pertraukimas (https://data.gov.lt/datasets/2616/)
