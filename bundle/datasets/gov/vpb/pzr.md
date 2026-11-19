---
type: Dataset
title: "Lietuvos Respublikos prekių ženklai"
description: "Lietuvos Respublikos prekių ženklų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių prekių ženklų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr"
tags: [gov, vpb, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3809/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/pzr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos Respublikos prekių ženklai

Lietuvos Respublikos prekių ženklų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių prekių ženklų duomenys. Duomenų rinkinį sudaro nuo 1991 m. kaupiami ir iki šiol atnaujinami prekių ženklų duomenys. Bendras rinkinys sudarytas iš keturių lentelių: „Prekių ženklai“, „Prekių ženklams priskirti asmenys“, „Prekių ženklų Vienos klasifikacijos“ ir „Prekių ženklų Nicos klasifikacijos“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vpb/pzr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3809/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vpb/pzr/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos prekių ženklai[^dcat]
- **Portal Title (`@en`):** Trademarks of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2025-03-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-03-24` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos prekių ženklų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių prekių ženklų duomenys. Duomenų rinkinį sudaro nuo 1991 m. kaupiami ir iki šiol atnaujinami prekių ženklų duomenys. Bendras rinkinys sudarytas iš keturių lentelių: „Prekių ženklai“, „Prekių ženklams priskirti asmenys“, „Prekių ženklų Vienos klasifikacijos“ ir „Prekių ženklų Nicos klasifikacijos“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Register of Trademarks of the Republic of Lithuania has been collecting and updating trademark data valid in Lithuania since 2014. The data set has been collecting and updating trade mark data since 1991. The overall set consists of four tables: “Trade marks”, “Trademark persons”, “Trademark Vienna Classifications” and “Trademark Nice Classifications”. Data provider shall mean the State Patent Bureau of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PrekesZenklas](pzr/PrekesZenklas.md) | Prekių ženklai | — | `vda_prime_key` | — | `12` | Lentelė „Prekių ženklai“. |
| [Asmuo](pzr/Asmuo.md) | Prekių ženklams priskirti asmenys | — | `vda_prime_key` | — | `8` | Lentelė „Prekių ženklams priskirti asmenys“. |
| [VienosKlasifikacija](pzr/VienosKlasifikacija.md) | Prekių ženklų Vienos klasifikacijos | — | `vda_prime_key` | — | `5` | Lentelė „Prekių ženklų Vienos klasifikacijos“. |
| [NicosKlasifikacija](pzr/NicosKlasifikacija.md) | Prekių ženklų Nicos klasifikacijos | — | `vda_prime_key` | — | `5` | Lentelė „Prekių ženklų Nicos klasifikacijos“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/pzr (https://data.gov.lt/datasets/3809/)
