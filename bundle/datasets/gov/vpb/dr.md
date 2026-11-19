---
type: Dataset
title: "Lietuvos Respublikos dizainų duomenys"
description: "Lietuvos Respublikos dizainų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių dizainų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr"
tags: [gov, vpb, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/dr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos Respublikos dizainų duomenys

Lietuvos Respublikos dizainų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių dizainų duomenys. Duomenų rinkinį sudaro nuo 1993 m. kaupiami ir iki šiol atnaujinami duomenys. Bendras rinkinys sudarytas iš keturių lentelių: „Dizainai“, „Dizainams priskirti asmenys“, „Dizainų Lokarno klasifikacijos“ ir „Dizainų atvaizdai“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vpb/dr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3807/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vpb/dr/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos dizainų duomenys[^dcat]
- **Portal Title (`@en`):** Design Data of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2025-03-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-03-24` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos dizainų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių dizainų duomenys. Duomenų rinkinį sudaro nuo 1993 m. kaupiami ir iki šiol atnaujinami duomenys. Bendras rinkinys sudarytas iš keturių lentelių: „Dizainai“, „Dizainams priskirti asmenys“, „Dizainų Lokarno klasifikacijos“ ir „Dizainų atvaizdai“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Register of Designs of the Republic of Lithuania has been collecting and updating data on the designs in force in Lithuania since 2014. The data set has been collecting and updating design data since 1993. The overall set consists of four tables: Design, Design Assigned Persons, Design Locarno Classifications, and Design Images. Data provider shall mean the State Patent Bureau of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dizainas](dr/Dizainas.md) | Dizainai | — | `vda_prime_key` | — | `10` | Lentelė „Dizainai“. Lentelę sudaro: dizaino bylos registracijos ir paraiškos numeriai, pavadinimas, dabartinė būsena su pradžios data, dizaino galiojimo... |
| [Asmuo](dr/Asmuo.md) | Dizainams priskirti asmenys | — | — | — | `8` | Lentelė „Dizainams priskirti asmenys“. |
| [LokarnoKlasifikacija](dr/LokarnoKlasifikacija.md) | Dizainų Lokarno klasifikacijos | — | — | — | `5` | Lentelė „Dizainų Lokarno klasifikacijos“. |
| [Atvaizdas](dr/Atvaizdas.md) | Dizainų atvaizdai | — | — | — | `4` | Lentelė „Dizainų atvaizdai“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/dr (https://data.gov.lt/datasets/3807/)
