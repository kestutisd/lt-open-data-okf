---
type: Dataset
title: "Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje"
description: "Viena platformos „Tvarkau miestą“ duomenų rinkinio eilutė atitinka vieną vartotojo pranešimą apie problemą Vilniaus miesto savivaldybėje."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/registruotos_problemos"
tags: [gov, vilniaus_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3894/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/registruotos_problemos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje

Viena platformos „Tvarkau miestą“ duomenų rinkinio eilutė atitinka vieną vartotojo pranešimą apie problemą Vilniaus miesto savivaldybėje. Rinkinį sudaro: problemos tipas, statusas ir statuso atnaujinimo data, už problemos sprendimą atsakingas padalinys, problemos registravimo ir išsprendimo datos, transporto priemonės valstybinis numeris ir numerio struktūra (jei problema susijusi su transporto priemone), problemos vietos adresas ir koordinatės. Vilniaus miesto savivaldybę apimantys duomenys renkami nuo 2012 metų ir bus atnaujinami kas mėnesį. Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/registruotos_problemos`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/registruotos_problemos` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3894/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/registruotos_problemos`[^dcat]
- **Portal Title (`@lt`):** Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje[^dcat]
- **Portal Title (`@en`):** Problems registered by users on the “Manage the City” platform in Vilnius City Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-09-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-07-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Viena platformos „Tvarkau miestą“ duomenų rinkinio eilutė atitinka vieną vartotojo pranešimą apie problemą Vilniaus miesto savivaldybėje. Rinkinį sudaro: problemos tipas, statusas ir statuso atnaujinimo data, už problemos sprendimą atsakingas padalinys, problemos registravimo ir išsprendimo datos, transporto priemonės valstybinis numeris ir numerio struktūra (jei problema susijusi su transporto priemone), problemos vietos adresas ir koordinatės. Vilniaus miesto savivaldybę apimantys duomenys renkami nuo 2012 metų ir bus atnaujinami kas mėnesį. Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

One line of the data set of the platform “Manage the City” corresponds to one user report on the problem in Vilnius City Municipality. The kit consists of: type of problem, status and date of renewal of status, department responsible for solving the problem, dates of registration and resolution of the problem, vehicle number and number structure (if the problem relates to the vehicle), address and coordinates of the location of the problem. Data covering Vilnius City Municipality have been collected since 2012 and will be updated monthly. Data provider – Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Problema](registruotos_problemos/Problema.md) | Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje | `4` | `pranesimo_id` | — | `17` | Viena platformos „Tvarkau miestą“ duomenų rinkinio eilutė atitinka vieną vartotojo pranešimą apie problemą Vilniaus miesto savivaldybėje. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/registruotos_problemos (https://data.gov.lt/datasets/3894/)
