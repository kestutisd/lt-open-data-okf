---
type: Dataset
title: "JRA jaunimo darbuotojų kvalifikacija"
description: "Jaunimo reikalų agentūros Jaunimo darbuotojų sistema kaupia duomenis apie jaunimo darbuotojus."
resource: "https://get.data.gov.lt/datasets/gov/jra/kvalifikacija"
tags: [gov, jra, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/kvalifikacija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/jra/kvalifikacija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2629/"
    title: "data.gov.lt DCAT-AP — datasets/gov/jra/kvalifikacija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# JRA jaunimo darbuotojų kvalifikacija

- **Namespace:** `datasets/gov/jra/kvalifikacija`[^manifest]
- **Manifest CSV:** [datasets/gov/jra/kvalifikacija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/kvalifikacija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/kvalifikacija` (`deployed`)[^manifest]
- **Provider:** `jra` — Jaunimo reikalų agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2629/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/jra/kvalifikacija/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Jaunimo darbuotojų kvalifikacija[^dcat]
- **Portal Title (`@en`):** Qualifications of youth workers of the youth agency[^dcat]
- **Issued (`dct:issued`):** `2024-04-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-04-23` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Jaunimo reikalų agentūros Jaunimo darbuotojų sistema kaupia duomenis apie jaunimo darbuotojus. Teikiami duomenys kaupiami nuo 2018 m., numatyta atnaujinti kasdien. Duomenyse kaupiama darbuotojo šifruotas kodas, išsirinkti kursai, tuometinis etatas, išsilavinimas ir darbovietė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Youth Agency Youth Workers System gathers data about JRA employees. The data reported shall be collected from 2018, scheduled to update daily. Data accumulates employee encrypted code, selected courses, post, education, and workplace.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kvalifikacija](kvalifikacija/Kvalifikacija.md) | JRA jaunimo darbuotojų kvalifikacija | `4` | `vda_id` | — | `6` | Jaunimo reikalų agentūros Jaunimo darbuotojų sistema kaupia duomenis apie JRA dirbančius darbuotojus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/kvalifikacija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/kvalifikacija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/jra/kvalifikacija (https://data.gov.lt/datasets/2629/)
