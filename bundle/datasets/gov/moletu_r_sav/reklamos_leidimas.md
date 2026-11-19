---
type: Dataset
title: "Reklamos leidimų duomenų rinkinys"
description: "Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų leidimai."
resource: "https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas"
tags: [gov, moletu_r_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3811/"
    title: "data.gov.lt DCAT-AP — datasets/gov/moletu_r_sav/reklamos_leidimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Reklamos leidimų duomenų rinkinys

- **Namespace:** `datasets/gov/moletu_r_sav/reklamos_leidimas`[^manifest]
- **Manifest CSV:** [datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas` (`deployed`)[^manifest]
- **Provider:** `moletu_r_sav` — Molėtų rajono savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3811/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas`[^dcat]
- **Portal Title (`@lt`):** Molėtų rajono savivaldybės reklamų leidimai[^dcat]
- **Portal Title (`@en`):** Advertising permits of the Municipality of Molėtai[^dcat]
- **Issued (`dct:issued`):** `2025-03-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-03-24` .. `2026-10-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų leidimai. Duomenų rinkinį sudaro: įmonės ar fizinio asmens identifikatorius, įrenginio informacija ir koordinatės, tipas, leidimo numeris, leidimo galiojimo terminai ir išdavimo data. Duomenų teikėjas – Molėtų rajono savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes advertisement editions valid since 2017 in the geographical information system of the municipality of Molėtai (GIS). The dataset shall comprise: company or natural person identifier, device information and coordinates, type, authorisation number, authorisation period and date of issue. Data provider: Moletai Municipality. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ReklamosLeidimas](reklamos_leidimas/ReklamosLeidimas.md) | Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų leidimai. Duomenų rinkinį sudaro: įmonės ar fizinio asmens identifikatorius, įrenginio informacija ir koordinatės, tipas, leidimo numeris, leidimo galiojimo terminai ir išdavimo data. | `4` | `id` | — | `12` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/moletu_r_sav/reklamos_leidimas (https://data.gov.lt/datasets/3811/)
