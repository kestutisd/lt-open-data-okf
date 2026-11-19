---
type: Dataset
title: "Lietuvos Respublikoje registruoti patentai"
description: "Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr"
tags: [gov, vpb, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Lietuvos Respublikoje registruoti patentai

Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys. Duomenų rinkinį sudaro nuo 1992 m. kaupiami ir iki šiol atnaujinami nacionalinių patentų duomenys. Bendras rinkinys sudarytas iš trijų lentelių: „Lietuvoje registruoti patentai“, „Lietuvoje registruotiems patentams priskirti asmenys“ ir „Lietuvoje registruotų patentų klasifikacija“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vpb/lrpr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3808/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vpb/lrpr/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikoje registruoti patentai[^dcat]
- **Portal Title (`@en`):** Patents registered in the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2025-03-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-03-21` .. `2026-09-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys. Duomenų rinkinį sudaro nuo 1992 m. kaupiami ir iki šiol atnaujinami nacionalinių patentų duomenys. Bendras rinkinys sudarytas iš trijų lentelių: „Lietuvoje registruoti patentai“, „Lietuvoje registruotiems patentams priskirti asmenys“ ir „Lietuvoje registruotų patentų klasifikacija“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Republic of Lithuania Patent Register has been collecting and updating data on national and Lithuanian European patents since 2002. The data collection has been collecting and updating national patent data since 1992. The overall set consists of three tables: “patents registered in Lithuania”, “Persons attributed to patents registered in Lithuania” and “Classification of patents registered in Lithuania”. Data provider shall mean the State Patent Bureau of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Byla](lrpr/Byla.md) | Lietuvoje registruoti patentai | `4` | `patento_nr` | — | `12` | Lentelė „Lietuvoje registruoti patentai“. |
| [Asmuo](lrpr/Asmuo.md) | Lietuvoje registruotiems patentams priskirti asmenys | — | `vda_prime_key` | — | `8` | Lentelė „Lietuvoje registruotiems patentams priskirti asmenys“. |
| [Klasifikacija](lrpr/Klasifikacija.md) | Lietuvoje registruotų patentų klasifikacija | — | `vda_prime_key` | — | `6` | Lentelė „Lietuvoje registruotų patentų klasifikacija“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr (https://data.gov.lt/datasets/3808/)
