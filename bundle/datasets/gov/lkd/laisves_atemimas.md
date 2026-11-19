---
type: Dataset
title: "Nuteistųjų laisvės atėmimo bausme statistika"
description: "Lietuvos kalėjimų tarnyba kaupia asmenų, nuteistų laisvės atėmimo bausme, statistinius duomenis nuo 2021 m., atnaujinamus kasmet, gaunamus iš kalinimo įstaigų."
resource: "https://get.data.gov.lt/datasets/gov/lkd/laisves_atemimas"
tags: [gov, lkd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laisves_atemimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lkd/laisves_atemimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2632/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lkd/laisves_atemimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nuteistųjų laisvės atėmimo bausme statistika

- **Namespace:** `datasets/gov/lkd/laisves_atemimas`[^manifest]
- **Manifest CSV:** [datasets/gov/lkd/laisves_atemimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laisves_atemimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lkd/laisves_atemimas` (`deployed`)[^manifest]
- **Provider:** `lkd` — Lietuvos kalėjimų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2632/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lkd/laisves_atemimas/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Nuteistųjų laisvės atėmimo bausme statistika[^dcat]
- **Portal Title (`@en`):** Statistics on custodial sentences[^dcat]
- **Issued (`dct:issued`):** `2024-04-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-04-23` .. `2025-12-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos kalėjimų tarnyba kaupia asmenų, nuteistų laisvės atėmimo bausme, statistinius duomenis nuo 2021 m., atnaujinamus kasmet, gaunamus iš kalinimo įstaigų. Rinkinys apima punkto numerį, naudojamą atskirti atitinkamus duomenis pagal konkrečius metus. Punkto numeriai gali būti pateikti tiksliau naudojant daugiau skaitmenų, atskirtų taškais. Tarp minėtų duomenų patenka nusikaltimai, išvykimo iš kalinimo įstaigos pobūdžiai, nuteistųjų amžiaus grupės. Rinkinyje minėti duomenys matuojami vienetais nuteistųjų asmenų arba metais, mėnesiais ir dienomis. Patogumo dėlei taip pat naudojami rinkinio eilučių numeriai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Lithuanian Prison Department (LKD) accumulates persons sentenced to freedom the penalty of deprivation, statistics from 2021, updated annually, from prison institutions. Set includes item number used separate the relevant data by specific year. Item numbers can be presented more accurately using more digits separated points. These include offences of departure from prison nature of the institution, age groups of convicted persons. Data mentioned in the collection measured in units of convicted persons or in years, months, and in days. For convenience, the serial numbers of the set are also used.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LaisvesAtemimoStatistika](laisves_atemimas/LaisvesAtemimoStatistika.md) | Nuteistųjų laisvės atėmimo bausme statistika | `4` | `vda_id` | — | `10` | Lietuvos kalėjimų departamentas (LKD) kaupia asmenų, nuteistų laisvės atėmimo bausme, statistinius duomenis nuo 2021 m., atnaujinamus kasmet, gaunamus iš... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lkd/laisves_atemimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laisves_atemimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lkd/laisves_atemimas (https://data.gov.lt/datasets/2632/)
