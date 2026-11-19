---
type: Dataset
title: "Lietuvoje įsigalioję Europos patentai"
description: "Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr"
tags: [gov, vpb, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2905/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/espr"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# Lietuvoje įsigalioję Europos patentai

Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys. Duomenų rinkinyje nuo 1994 m. kaupiami ir iki šiol atnaujinami Lietuvoje įsigaliojusių Europos patentų duomenys. Bendras rinkinys sudarytas iš trijų lentelių: „Lietuvoje įsigaliojusių Europos patentų bylos“, „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“ ir „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vpb/espr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2905/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vpb/espr/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Lietuvoje įsigalioję Europos patentai[^dcat]
- **Portal Title (`@en`):** European patents in force in Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-12-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-27`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-09-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys. Duomenų rinkinį sudaro nuo 1994 m. saugomų Lietuvoje įsigaliojusių Europos patentų duomenų lentelės: „Lietuvoje įsigalioję Europos patentai“, „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“ ir „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Republic of Lithuania Patent Register has been collecting and updating data on national and Lithuanian European patents since 2002. The data collection has been collecting and updating the data on European patents which entered into force in Lithuania since 1994. The overall set consists of three tables: “Patent Files”, “Persons assigned to Patents” and “Patent Classifications”. Data provider shall mean the State Patent Bureau of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Byla](espr/Byla.md) | Lietuvoje įsigaliojusių Europos patentų bylos | `4` | `patento_numeris` | — | `8` | Lentelė „Lietuvoje įsigaliojusių Europos patentų bylos“. |
| [Asmuo](espr/Asmuo.md) | Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys | — | `vda_prime_key` | — | `6` | Lentelė „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“. |
| [Klasifikacija](espr/Klasifikacija.md) | Lietuvoje įsigaliojusių Europos patentų klasifikacija | — | `vda_prime_key` | — | `5` | Lentelė „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/espr (https://data.gov.lt/datasets/2905/)
