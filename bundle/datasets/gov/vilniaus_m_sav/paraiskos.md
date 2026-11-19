---
type: Dataset
title: "Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys"
description: "Rinkinyje pateikiami duomenys apie Vilniaus miesto savivaldybės skelbiamus ir vykdomus konkursus jaunimo, bendruomenės, sporto, aplinkos, miesto plėtros, socialinės apsaugos, kultūros, sveikatingumo programose bei konkursams teiktas paraiškas."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos"
tags: [gov, vilniaus_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3848/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys

Rinkinyje pateikiami duomenys apie Vilniaus miesto savivaldybės skelbiamus ir vykdomus konkursus jaunimo, bendruomenės, sporto, aplinkos, miesto plėtros, socialinės apsaugos, kultūros, sveikatingumo programose bei konkursams teiktas paraiškas.[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3848/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos`[^dcat]
- **Portal Title (`@lt`):** Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys[^dcat]
- **Portal Title (`@en`):** Data on tenders published by Vilnius City Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-06-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-05` .. `2026-09-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie Vilniaus miesto savivaldybės skelbiamus ir vykdomus jaunimo, bendruomenės, sporto, aplinkos, miesto plėtros, socialinės apsaugos, kultūros bei sveikatingumo programų konkursus ir jiems teiktas paraiškas. Duomenys apima laikotarpį nuo 2022 m. iki dabar. Rinkinį sudaro dvi dalys: Konkursai: pateikiami duomenys apie kiekvieną skelbtą konkursą, tikslus, aprašymą, programą, maksimalią finansavimo sumą, paraiškų teikimo pradžios ir pabaigos datas ir atsakingą savivaldybės skyrių. Paraiškos: aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo. Lentelės objektas – konkursui teikta paraiška. Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on competitions and applications for youth, community, sport, environment, urban development, social security, culture and wellness programmes announced and implemented by Vilnius City Municipality. The data cover the period from 2022 to now. The kit consists of two parts: Calls for tenders: details shall be given of each call for tenders, the objectives, description, programme, maximum amount of funding, the starting and closing dates of the application and the local authority responsible. Applications: a description of the tenders submitted, indicating the status of the tender, the code of the programme, the date of submission and the final assessment of the application after evaluation. The object of the table is the tender submitted to the tender. Data provider – Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Konkursas](paraiskos/Konkursas.md) | Vilniaus miesto savivaldybės administracijos konkursų skelbimai | `4` | `konkurso_id` | — | `11` | Pateikiami duomenys apie kiekvieną skelbtą konkursą, tikslus, aprašymą, programą, maksimalią finansavimo sumą, paraiškų teikimo pradžios ir pabaigos datas... |
| [Paraiska](paraiskos/Paraiska.md) | Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys | `4` | `teikejo_id` | — | `5` | Aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/paraiskos (https://data.gov.lt/datasets/3848/)
