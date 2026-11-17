---
type: Dataset
title: "Pabaigtų Atliekų tvarkymo projektų objektų duomenys"
description: "Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai"
tags: [gov, apva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pabaigtų Atliekų tvarkymo projektų objektų duomenys

Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys. Rinkinyje pateikiama su pasibaigusiais projektais susijusių objektų informacija: projekto informacija – projekto identifikacinis numeris, projekto kodas, programa; objekto informacija – pavadinimas, tipas, nekilnojamo turto numeris, būsena, savivaldybė, plotas, pajėgumai bei koordinatės. Pabrėžiame, kad dalis duomenų į sistemą suvedami ir atnaujinami rankiniu būdu, todėl gali būti neatitikimų. Taip pat rinkinys jungiasi su atvertu rinkiniu „Pabaigtų aplinkosaugos projektų duomenys“ (Lietuvos atvirų duomenų portalas | Pabaigtų aplinkosaugos projektų duomenys), jungiant per projekto identifikacinį numerį arba kodą. Duomenų laiko aprėptis – nuo 2017 m. rugsėjo mėn. Duomenų teikėjas – Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūrą.

- **Namespace:** `datasets/gov/apva/atlieku_objektai`[^manifest]
- **Manifest CSV:** [datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AtliekuObjektas](atlieku_objektai/AtliekuObjektas.md) | — | — | `vda_prime_key` | — | 16 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv
