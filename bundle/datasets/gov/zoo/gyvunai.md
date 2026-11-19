---
type: Dataset
title: "Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas"
description: "Rinkinyje pateikiami duomenys apie Lietuvos zoologijos sode laikomus gyvūnus einamiesiems metams."
resource: "https://get.data.gov.lt/datasets/gov/zoo/gyvunai"
tags: [gov, zoo, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zoo/gyvunai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/zoo/gyvunai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2734/"
    title: "data.gov.lt DCAT-AP — datasets/gov/zoo/gyvunai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas

Rinkinyje pateikiami duomenys apie Lietuvos zoologijos sode laikomus gyvūnus einamiesiems metams. Rinkinio objektas - individas arba gyvūnų grupė. Nurodoma informacija apie gyvūną (gyvūnų grupę): lotyniškas ir angliškas pavadinimas, lytis, gimimo data, aplinkybės ir vieta, esamas savininkas, aptvaras, kuriame gyvūnas laikomas bei taksonominė gyvūno klasifikacija.[^manifest]

- **Namespace:** `datasets/gov/zoo/gyvunai`[^manifest]
- **Manifest CSV:** [datasets/gov/zoo/gyvunai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zoo/gyvunai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zoo/gyvunai` (`deployed`)[^manifest]
- **Provider:** `zoo` — Lietuvos zoologijos sodas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2734/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/zoo/gyvunai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas[^dcat]
- **Portal Title (`@en`):** List of the Animal Collection of the Lithuanian Zoo[^dcat]
- **Issued (`dct:issued`):** `2024-08-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-08-09` .. `2026-01-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie Lietuvos zoologijos sode laikomus gyvūnus einamiesiems metams. Rinkinio objektas – individas arba gyvūnų grupė. Nurodoma informacija apie gyvūną (gyvūnų grupę): lotyniškas ir angliškas pavadinimas, lytis, gimimo data, aplinkybės ir vieta, esamas savininkas, aptvaras, kuriame gyvūnas laikomas bei taksonominė gyvūno klasifikacija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on animals kept in the Lithuanian zoo for the current year. The object of the kit is an individual or group of animals. Indication of the animal (group of animals): Latin and English name, sex, date of birth, circumstances and place of birth, current owner, enclosure where the animal is kept and taxonomic classification of the animal. For enquiries, contact the State Data Management Team: vdv@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Gyvunas](gyvunai/Gyvunas.md) | Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas | `4` | `vda_id` | — | `21` | Rinkinyje pateikiami duomenys apie Lietuvos zoologijos sode laikomus gyvūnus einamiesiems metams. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/zoo/gyvunai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zoo/gyvunai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/zoo/gyvunai (https://data.gov.lt/datasets/2734/)
