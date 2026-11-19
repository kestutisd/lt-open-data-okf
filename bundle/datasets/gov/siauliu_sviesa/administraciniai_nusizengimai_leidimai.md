---
type: Dataset
title: "Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste"
description: "Informacija apie išduotus automobilių stovėjimo leidimus ir užfiksuotus pažeidimus Šiaulių mieste"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai"
tags: [gov, siauliu_sviesa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4037/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste

Informacija apie išduotus automobilių stovėjimo leidimus ir užfiksuotus pažeidimus Šiaulių mieste[^manifest]

- **Namespace:** `datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai`[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai` (`deployed`)[^manifest]
- **Provider:** `siauliu_sviesa` — UAB Šiaulių šviesa *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4037/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai`[^dcat]
- **Portal Title (`@lt`):** Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste[^dcat]
- **Portal Title (`@en`):** Parking permits issued and violations recorded in Šiauliai city[^dcat]
- **Issued (`dct:issued`):** `2026-01-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-01-06` .. `2026-05-30`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie UAB „Šiaulių šviesa“ valdomus ir tvarkomus Šiaulių miesto savivaldybės išduodamus parkavimo leidimus gyventojams ir studentams, leidimų abonementų duomenis (leidimo galiojimo laikotarpis, leidimo gavėjas, automobilio valstybinis numeris ir parkavimo vietos koordinatės) bei Šiaulių miesto savivaldybėje užregistruotų nusižengimų pagal ANK 417 straipsnio 2 dalį ir ANK 418 straipsnį duomenis (pažeidimo data, pažeidimo vieta, automobilio valstybinis numeris, pažeidimo tipas ir būsena). Leidimų duomenys renkami nuo 2014 metų, o administracinių nusižengimų – nuo 2023 metų. Rinkinyje pateikti Valstybės duomenų agentūros nustatyti duomenys (išskyrus koordinates), pavyzdžiui: apmokėjimo būdas, automobilio markė ir kiti, išvesti iš laisvojo teksto duomenų stulpelių. Duomenų teikėjas – UAB „Šiaulių šviesa“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pazeidimas](administraciniai_nusizengimai_leidimai/Pazeidimas.md) | Užfiksuoti pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste | `4` | `pazeidimo_id` | — | `11` | Informacija apie užfiksuotus pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste |
| [Leidimas](administraciniai_nusizengimai_leidimai/Leidimas.md) | Išduoti automobilių parkavimo leidimai Šiaulių mieste | `4` | `leidimo_automobiliui_id` | — | `15` | Informacija apie išduotus automobilių parkavimo leidimus Šiaulių mieste |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai (https://data.gov.lt/datasets/4037/)
