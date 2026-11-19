---
type: Dataset
title: "Ekonominės veiklos klasifikatorius versija 2.1"
description: "Ekonominės veiklos klasifikatorius versija 2.1"
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/evrk2_1"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk2_1.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/evrk2_1.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2919/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/cl/evrk2_1"
    author: "team:vda"
    last_modified: "2026-02-02T00:00:00Z"
---

# Ekonominės veiklos klasifikatorius versija 2.1

Ekonominės veiklos klasifikatorius versija 2.1[^manifest]

- **Namespace:** `datasets/gov/lsd/cl/evrk2_1`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/cl/evrk2_1.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk2_1.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/evrk2_1` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2919/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/cl/evrk2_1`[^dcat]
- **Portal Title (`@lt`):** Ekonominės veiklos rūšių klasifikatorius (EVRK 2.1 red.)[^dcat]
- **Portal Title (`@en`):** Classification of economic activities (ERDF 2.1)[^dcat]
- **Issued (`dct:issued`):** `2025-01-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-02`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-01-15` .. `2026-05-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Ekonominės veiklos rūšių klasifikatorius (EVRK 2.1 red.) parengtas pagal Europos Sąjungos Statistikos Tarnybos (EUROSTAT) paruoštą klasifikatorių “Nomenclatures des Activities de Communite Europeene” - NACE rev. 2.1 (Statistinis Europos Bendrijos ekonominės veiklos rūšių klasifikatorius - NACE 2.1 red. ). EVRK 2.1 red. nustato atskirų kategorijų veiklos sritis, kodus, pavadinimus, t. y. sekcijas, skyrius, grupes, klases, visoms Europos Sąjungos šalims narėms. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The classification of economic activities (ECEC Rev. 2.1) is based on the classification “Nomenclatures des Activities de Communite Europeene” prepared by the Statistical Office of the European Union (EUROSTAT) - NACE rev. 2.1 (Statistical classification of economic activities of the European Community - NACE Rev. 2.1). Rev. 2.1 of the ECEC defines individual categories of activities, codes, names, i.e. sections, sections, groups, classes, for all Member States of the European Union. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [EkonominesVeiklosRusis](evrk2_1/EkonominesVeiklosRusis.md) | Ekonominės veikos rūšis (EVRK2.1) | `4` | `kodas` | `open` | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/evrk2_1.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk2_1.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/cl/evrk2_1 (https://data.gov.lt/datasets/2919/)
