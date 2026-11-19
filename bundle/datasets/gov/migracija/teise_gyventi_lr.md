---
type: Dataset
title: "Duomenys apie teisės gyventi Lietuvos Respublikoje suteikimą"
description: "Duomenys apie trečiųjų šalių piliečius"
resource: "https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr"
tags: [gov, migracija, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1942/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/teise_gyventi_lr"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie teisės gyventi Lietuvos Respublikoje suteikimą

Duomenys apie trečiųjų šalių piliečius[^manifest]

- **Namespace:** `datasets/gov/migracija/teise_gyventi_lr`[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/teise_gyventi_lr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1942/`[^dcat]
- **Publisher (`dct:publisher`):** Migracijos departamentas prie Lietuvos Respublikos vidaus reikalų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie teisės gyventi Lietuvos Respublikoje suteikimą[^dcat]
- **Portal Title (`@en`):** Data on granting the right to reside in the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-02-10` .. `2026-06-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie trečiųjų šalių piliečius, kuriems buvo išduoti ar pakeisti leidimai laikinai gyventi Lietuvos Respublikoje, Lietuvos Respublikos ilgalaikio gyventojo leidimai gyventi Europos Sąjungoje, Sąjungos piliečio šeimos nario leidimo laikinai gyventi šalyje kortelės ir Sąjungos piliečio šeimos nario leidimo nuolat gyventi šalyje kortelės. Duomenys apie Europos Sąjungos piliečius ir Europos laisvosios prekybos asociacijos valstybės narės piliečius, kuriems buvo išduoti ar pakeisti teisės laikinai gyventi Lietuvos Respublikoje pažymėjimai ir teisės nuolat gyventi Lietuvos Respublikoje pažymėjimai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on third-country nationals who have been issued or renewed temporary residence permits in the Republic of Lithuania, permits of a long-term resident of the Republic of Lithuania to reside in the European Union, temporary residence cards for a family member of an European Union and permanent residence cards for a family member of an European Union. Data on citizens of the European Union and of a Member State of the European Free Trade Association who have been issued or renewed temporary residence certificates and permanent residence certificates confirming right to reside in the Republic of Lithuania.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Prasymas](teise_gyventi_lr/Prasymas.md) | Duomenys apie trečiųjų šalių piliečių prašymus išduoti ar pakeisti leidimą laikinai gyventi Lietuvos Respublikoje | `4` | `id` | `open` | `9` | — |
| [Sprendimas](teise_gyventi_lr/Sprendimas.md) | Duomenys apie Migracijos departamento sprendimus trečiųjų šalių piliečiams išduoti arba pakeisti leidimą ar pažymėjimą laikinai gyventi Lietuvos Respublikoje | `4` | `id` | `open` | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/teise_gyventi_lr (https://data.gov.lt/datasets/1942/)
