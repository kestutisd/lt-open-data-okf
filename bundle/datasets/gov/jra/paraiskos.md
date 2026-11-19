---
type: Dataset
title: "Savanorių paraiškų statistika pagal priimančias organizacijas"
description: "Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose."
resource: "https://get.data.gov.lt/datasets/gov/jra/paraiskos"
tags: [gov, jra, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/jra/paraiskos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/jra/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Savanorių paraiškų statistika pagal priimančias organizacijas

- **Namespace:** `datasets/gov/jra/paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/jra/paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/paraiskos` (`deployed`)[^manifest]
- **Provider:** `jra` — Jaunimo reikalų agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2630/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/jra/paraiskos/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Savanorių paraiškų statistika pagal priimančias organizacijas[^dcat]
- **Portal Title (`@en`):** Volunteer application statistics by host organisation[^dcat]
- **Issued (`dct:issued`):** `2024-04-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-04-23` .. `2026-07-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose. Įstaiga teikia duomenis, kaupiamus nuo 2018 m. Juos atnaujinti numatyta kasdien. Duomenyse kaupiama priimančios organizacijos pavadinimas ir adresas, savanorystės paraiškos teikimo metai, priimtų, atmestų įprastų paraiškų skaičiai bei jų suma, paraiškų tapti kuratoriumi bei mentoriumi skaičiai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Youth Agency Youth Voluntary Service System accumulates data on youth volunteering in host organisations. The Authority shall provide data to be collected from 2018 and updated. scheduled daily. The data collects host organizations name and address, year of application for volunteering, accepted, number and amount of rejected normal applications, applications for membership numbers as a curator and mentor.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ParaiskuStatistika](paraiskos/ParaiskuStatistika.md) | Savanorių paraiškų statistika pagal priimančias organizacijas | `4` | `vda_id` | — | `9` | Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/paraiskos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/jra/paraiskos (https://data.gov.lt/datasets/2630/)
