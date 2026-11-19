---
type: Dataset
title: "Atvykstamojo turizmo statistiniai tyrimai"
description: "Statistinio tyrimo tikslas – parengti ir paskelbti statistinę informaciją apie atvykstančių į Lietuvą užsieniečių, jų kelionių ir nakvynių skaičių, kelionės tikslus, naudojamas transporto priemones, apgyvendinimo tipus ir kelionių išlaidas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta"
tags: [gov, lsd, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2079/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/turizmas/atvyksta"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atvykstamojo turizmo statistiniai tyrimai

- **Namespace:** `datasets/gov/lsd/turizmas/atvyksta`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/turizmas/atvyksta.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2079/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta`[^dcat]
- **Portal Title (`@lt`):** Atvykstamojo turizmo statistinio tyrimo duomenys[^dcat]
- **Portal Title (`@en`):** Statistical survey of inbound tourism, 2021[^dcat]
- **Issued (`dct:issued`):** `2022-12-07`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2022-12-07` .. `2024-12-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Statistinio tyrimo tikslas – parengti ir paskelbti statistinę informaciją apie atvykstančių į Lietuvą užsieniečių, jų kelionių ir nakvynių skaičių, kelionės tikslus, naudojamas transporto priemones, apgyvendinimo tipus ir kelionių išlaidas. Atrankinis statistinis tyrimas. Tiriamasis laikotarpis – ketvirtis. Apklausa atliekama 7 dienas per ketvirtį. Apklausą atlieka klausėjai. Pasienio kontrolės punktuose, stotyse ir viešbučiuose apklausiami 15 metų ir vyresni užsieniečiai. Apklausa atliekama TUR-04 protokolu (žr. https://apklausos.stat.gov.lt/statistines-anketos). Apklausiami turistai ir kiti keliautojai, išskyrus tuos, kurie Lietuvoje buvo ilgiau nei 12 mėnesių. Čia pateikiami apklausų duomenys dviejose lentelėse, apimančiose keliones be nakvynės (vienadienes) ir su nakvyne. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The goal of this statistical survey is to prepare and publish statistical information about foreigners inbound to Lithuania, their trips and trip length, modes of transportation used, types of accommodation and travel expenses. Survey consists of samples collected quarterly. The surveys are carried out for 7 days in each quarter. Foreign visitors (15 years or older) are interviewed at border control points, transport stations and hotels. The survey follows protocol TUR-04 (see https://apklausos.stat.gov.lt/statistines-anketos). Survey includes tourists and other travelers, except those who have stayed in Lithuania for more than 12 months. The data is presented here in two tables, separated into day trips and trips without an overnight stay.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KelionesAtvykSuNakv2021](atvyksta/KelionesAtvykSuNakv2021.md) | Atvykusių turistų kelionės su nakvyne 2021 m. | — | `id` | — | `55` | — |
| [KelionesAtvykBeNakv2021](atvyksta/KelionesAtvykBeNakv2021.md) | Atvykusių turistų kelionės be nakvynės 2021 m. | — | `id` | — | `32` | — |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bool` | `1` | — | — | Taip | — |
| `bool` | `0` | — | — | Ne | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/turizmas/atvyksta (https://data.gov.lt/datasets/2079/)
