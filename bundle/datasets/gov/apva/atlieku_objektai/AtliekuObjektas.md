---
type: Table
title: "AtliekuObjektas"
description: "Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai/AtliekuObjektas"
tags: [gov, apva, atliekuobjektas, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3869/"
    title: "data.gov.lt DCAT-AP — datasets/gov/apva/atlieku_objektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AtliekuObjektas

**Dataset Context:** Aplinkos projektų valdymo agentūros projektų monitoringo informacinėje sistemoje (APVA GIS) kaupiami geografiniai objektų duomenys. Rinkinyje pateikiama su pasibaigusiais projektais susijusių objektų informacija: projekto informacija – projekto identifikacinis numeris, projekto kodas, programa; objekto informacija – pavadinimas, tipas, nekilnojamo turto numeris, būsena, savivaldybė, plotas, pajėgumai bei koordinatės. Pabrėžiame, kad dalis duomenų į sistemą suvedami ir atnaujinami rankiniu būdu, todėl gali būti neatitikimų. Taip pat rinkinys jungiasi su atvertu rinkiniu „Pabaigtų aplinkosaugos projektų duomenys“ (Lietuvos atvirų duomenų portalas | Pabaigtų aplinkosaugos projektų duomenys), jungiant per projekto identifikacinį numerį arba kodą. Duomenų laiko aprėptis – nuo 2017 m. rugsėjo mėn. Duomenų teikėjas – Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūrą. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/apva/atlieku_objektai/AtliekuObjektas`[^manifest]
- **Dataset:** [Pabaigtų Atliekų tvarkymo projektų objektų duomenys](../atlieku_objektai.md) (`datasets/gov/apva/atlieku_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai/AtliekuObjektas` (`deployed`)[^manifest]
- **Provider:** `apva` — Aplinkos projektų valdymo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `prj_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius | — |
| `prj_kodas` | `string` | — | `4` | `open` | — | Unikalus projekto kodas | — |
| `programa` | `string` | — | `4` | `open` | — | Programos pavadinimas kurios metu buvo pradėtas vykdyti projektas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `nt_nr` | `string` | — | `4` | `open` | — | Nekilnojamo turto numeris | — |
| `busena` | `string` | — | `4` | `open` | — | Objekto būsena | — |
| `plotas` | `number` | — | `4` | `open` | — | Objekto plotas išreikštas hektarais (ha) | — |
| `pajegumas` | `number` | — | `4` | `open` | — | Objekto pajegumas išreikštas tonomis per metus (t/m) | — |
| `pajegumas_projektinis` | `number` | — | `4` | `open` | — | Objekto numatomas pajegumas išreikštas tonomis per metus (t/m) | — |
| `komentaras` | `string` | — | `4` | `open` | — | Komentaras | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Objekto savivaldybė | — |
| `vda_sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės reikšmė į kurią patenka objekto koordinatės | — |
| `shape_wkt_wgs` | `geometry(4326)` | — | `4` | `open` | — | Objekto wgs-84 koordinatės (wkt reprezentacija) | — |
| `irenginiai` | `string` | — | `4` | `open` | — | Objekte esantys įrenginiai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Įrengtas"` | — | — | — | — |
| `busena` | `"Esamas"` | — | — | — | — |
| `busena` | `"Planuojamas"` | — | — | — | — |
| `busena` | `"Įrengiamas"` | — | — | — | — |
| `busena` | `"Neįrengtas"` | — | — | — | — |
| `busena` | `"Nepajungtas"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/apva/atlieku_objektai (https://data.gov.lt/datasets/3869/)
