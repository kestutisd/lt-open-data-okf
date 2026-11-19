---
type: Dataset
title: "Transporto priemonių judėjimo pro muitinės postus srautas"
description: "Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/transporto_srautai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2842/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/transporto_srautai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Transporto priemonių judėjimo pro muitinės postus srautas

Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus[^manifest]

- **Namespace:** `datasets/gov/muitine/transporto_srautai`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/transporto_srautai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2842/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/transporto_srautai`[^dcat]
- **Portal Title (`@lt`):** Transporto priemonių judėjimo per muitinės postus srautas[^dcat]
- **Portal Title (`@en`):** Flow of vehicles through customs posts[^dcat]
- **Issued (`dct:issued`):** `2024-10-31`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-31` .. `2026-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama įvairiuose muitinės postuose per dieną vaizdo stebėjimo kameromis užfiksuotų Lietuvos sieną kertančių transporto priemonių ir konteinerių, važiuojančių į Lietuvos teritoriją arba išvykstančių iš jos, srautų informacija. Duomenys renkami nuo 2008 metų. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data collection shall contain information on traffic of vehicles and containers crossing the Lithuanian border travelling to or leaving the territory of Lithuania recorded by video surveillance cameras at various customs posts per day. Data has been collected since 2008. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Srautas](transporto_srautai/Srautas.md) | Transporto priemonių judėjimo pro muitinės postus srautas | `4` | `vda_prime_key` | — | `10` | Duomenys apie pro muitinės postus kameromis užfiksuotus judančius transporto priemonių ir konteinerių srautus |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/transporto_srautai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/transporto_srautai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/transporto_srautai (https://data.gov.lt/datasets/2842/)
