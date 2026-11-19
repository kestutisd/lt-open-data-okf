---
type: Dataset
title: "Filmų registras"
description: "Duomenų rinkinys apie Lietuvoje registruotus filmus ir jų metaduomenis"
resource: "https://get.data.gov.lt/datasets/gov/lkc/filmu_registras"
tags: [gov, lkc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkc/filmu_registras.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lkc/filmu_registras.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lkc/filmu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Filmų registras

Duomenų rinkinys apie Lietuvoje registruotus filmus ir jų metaduomenis[^manifest]

- **Namespace:** `datasets/gov/lkc/filmu_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/lkc/filmu_registras.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkc/filmu_registras.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lkc/filmu_registras` (`deployed`)[^manifest]
- **Provider:** `lkc` — Lietuvos Kino Centras prie Kultūros Ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3896/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lkc/filmu_registras`[^dcat]
- **Portal Title (`@lt`):** Filmų registras[^dcat]
- **Portal Title (`@en`):** Film Register, data collection on films registered in Lithuania and their metadata[^dcat]
- **Issued (`dct:issued`):** `2025-09-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2025-09-22` .. `2025-09-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys apima informaciją apie Lietuvoje registruotus filmus ir jų metaduomenis, susijusius su kūrybinėmis komandomis, rodymo teisėmis, subtitrais, gamybos informacija ir autorinėmis teisėmis. Kiekviena lentelės eilutė atitinka vieną filmą. Rinkinys gali būti naudojamas kultūros tyrimams, kino statistikai, filmų duomenų analizei ar autorinių teisių stebėsenai. Duomenų teikėjas – Lietuvos Kino Centras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set includes information about films registered in Lithuania and their metadata related to creative teams, display rights, subtitles, production information and copyright. Each row in the table matches one movie. The kit can be used for cultural research, film statistics, film data analysis or copyright monitoring. Data provider – Lithuanian Cinema Centre. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FilmuRegistras](filmu_registras/FilmuRegistras.md) | Filmų registras | `4` | `id` | — | `31` | Duomenų rinkinys apima informaciją apie Lietuvoje registruotus filmus ir jų metaduomenis, susijusius su kūrybinėmis komandomis, rodymo teisėmis, subtitrais... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lkc/filmu_registras.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkc/filmu_registras.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lkc/filmu_registras (https://data.gov.lt/datasets/3896/)
