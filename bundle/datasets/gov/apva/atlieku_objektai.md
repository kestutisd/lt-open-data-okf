---
type: Dataset
title: "Pabaigtų Atliekų tvarkymo projektų objektų duomenys"
description: "Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai"
tags: [gov, apva, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3869/"
    title: "data.gov.lt DCAT-AP — datasets/gov/apva/atlieku_objektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pabaigtų Atliekų tvarkymo projektų objektų duomenys

Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys. Rinkinyje pateikiama su pasibaigusiais projektais susijusių objektų informacija: projekto informacija – projekto identifikacinis numeris, projekto kodas, programa; objekto informacija – pavadinimas, tipas, nekilnojamo turto numeris, būsena, savivaldybė, plotas, pajėgumai bei koordinatės. Pabrėžiame, kad dalis duomenų į sistemą suvedami ir atnaujinami rankiniu būdu, todėl gali būti neatitikimų. Taip pat rinkinys jungiasi su atvertu rinkiniu „Pabaigtų aplinkosaugos projektų duomenys“ (Lietuvos atvirų duomenų portalas | Pabaigtų aplinkosaugos projektų duomenys), jungiant per projekto identifikacinį numerį arba kodą. Duomenų laiko aprėptis – nuo 2017 m. rugsėjo mėn. Duomenų teikėjas – Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūrą. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/apva/atlieku_objektai`[^manifest]
- **Manifest CSV:** [datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai` (`deployed`)[^manifest]
- **Provider:** `apva` — Aplinkos projektų valdymo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3869/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai`[^dcat]
- **Portal Title (`@lt`):** Pabaigtų atliekų tvarkymo projektų objektų duomenys[^dcat]
- **Portal Title (`@en`):** Data on Completed Waste Management Project Objects[^dcat]
- **Issued (`dct:issued`):** `2025-07-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-07-10` .. `2025-07-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys. Rinkinyje pateikiama su pasibaigusiais projektais susijusių objektų informacija: projekto informacija – projekto identifikacinis numeris, projekto kodas, programa; objekto informacija – pavadinimas, tipas, nekilnojamo turto numeris, būsena, savivaldybė, plotas, pajėgumai bei koordinatės. Pabrėžiame, kad dalis duomenų į sistemą suvedami ir atnaujinami rankiniu būdu, todėl gali būti neatitikimų. Taip pat rinkinys jungiasi su atvertu rinkiniu „Pabaigtų aplinkosaugos projektų duomenys“ (Lietuvos atvirų duomenų portalas | Pabaigtų aplinkosaugos projektų duomenys), jungiant per projekto identifikacinį numerį arba kodą. Duomenų laiko aprėptis – nuo 2017 m. rugsėjo mėn. Duomenų teikėjas – Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The environmental project management agency's project monitoring information system (APVA GIS) collects geographical data on objects. The collection contains information about completed projects: project information – project identification number, project code, application; object information – name, type, real estate number, status, municipality, area, capacity and coordinates. We note that some of the data is collected and updated manually into the system, so there may be discrepancies. The collection also connects to the open collection “Data on finished environmental projects” (Lithuanian Open Data Portal ¦ Data on finished environmental projects) by connecting through the project identification number or code. Data time coverage: from September 2017. Data provider shall mean the Environmental Project Management Agency of the Ministry of Environment of the Republic of Lithuania. Refer to for technical questions or possible errors. atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AtliekuObjektas](atlieku_objektai/AtliekuObjektas.md) | — | — | `vda_prime_key` | — | `16` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/apva/atlieku_objektai (https://data.gov.lt/datasets/3869/)
