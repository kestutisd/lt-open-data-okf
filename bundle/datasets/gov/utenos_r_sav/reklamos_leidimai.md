---
type: Dataset
title: "Reklamos leidimų duomenų rinkinys"
description: "Utenos rajono savivaldybės reklamų leidimai"
resource: "https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai"
tags: [gov, utenos_r_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3824/"
    title: "data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/reklamos_leidimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Reklamos leidimų duomenų rinkinys

Utenos rajono savivaldybės reklamų leidimai[^manifest]

- **Namespace:** `datasets/gov/utenos_r_sav/reklamos_leidimai`[^manifest]
- **Manifest CSV:** [datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai` (`deployed`)[^manifest]
- **Provider:** `utenos_r_sav` — Utenos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3824/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai`[^dcat]
- **Portal Title (`@lt`):** Utenos rajono savivaldybės reklamų leidimai[^dcat]
- **Portal Title (`@en`):** Advertising permits of Utena District Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-04-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-04-07` .. `2026-01-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie Utenos rajone išduotus leidimus reklamai. Jame nurodomi leidimo numeris, išdavimo data, galiojimo laikotarpis, pareiškėjas (fizinis ar juridinis asmuo) ir susijęs kodas. Taip pat pateikiami duomenys apie reklamos įrenginius, įskaitant įrenginio ID, reklamos tipą, zoną, plotą, adresą bei geometriją. Duomenis teikėjas – Utenos rajono savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains information on advertising authorisations issued in the Utena area. It shall indicate the authorisation number, the date of issue, the period of validity, the applicant (natural or legal person) and the associated code. Information on advertising devices including device ID, advertising type, zone, area, address and geometry shall also be provided. Data shall be provided by the municipality of Utena district. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ReklamosLeidimas](reklamos_leidimai/ReklamosLeidimas.md) | Rinkinyje pateikiama informacija apie Utenos rajone išduotus leidimus reklamai. Jame nurodomi leidimo numeris, išdavimo data, galiojimo laikotarpis, pareiškėjas (fizinis ar juridinis asmuo) ir susijęs kodas. Taip pat pateikiami duomenys apie reklamos įrenginius, įskaitant įrenginio ID, reklamos tipą, zoną, plotą, adresą bei geometriją. | `4` | `id` | — | `13` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/reklamos_leidimai (https://data.gov.lt/datasets/3824/)
