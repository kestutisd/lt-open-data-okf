---
type: Dataset
title: "Duomenys apie LT pilietybės suteikimą"
description: "Duomenys apie asmenis, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat vaikus, kuriems buvo konstatuotas Lietuvos Respublikos pilietybės turėjimo faktas..."
resource: "https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe"
tags: [gov, migracija, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1943/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/lt_pilietybe"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie LT pilietybės suteikimą

Duomenys apie asmenis, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat vaikus, kuriems buvo konstatuotas Lietuvos Respublikos pilietybės turėjimo faktas, kurie Lietuvos Respublikos pilietybę įgijo juos įvaikinus arba pasikeitus tėvų pilietybei, neatsižvelgiant į jų gyvenamąją vietą.[^manifest]

- **Namespace:** `datasets/gov/migracija/lt_pilietybe`[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/lt_pilietybe.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1943/`[^dcat]
- **Publisher (`dct:publisher`):** Migracijos departamentas prie Lietuvos Respublikos vidaus reikalų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie LT pilietybės suteikimą[^dcat]
- **Portal Title (`@en`):** Data on granting LT citizenship[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-05-30` .. `2026-06-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie sprendimus asmenims, kuriems Lietuvos Respublikos pilietybė buvo atkurta, suteikta natūralizacijos, supaprastinta ar išimties tvarka, kurie grąžino Lietuvos Respublikos pilietybę, taip pat sprendimus vaikams vaikams, kuriems buvo konstatuotas Lietuvos Respublikos pilietybės turėjimo faktas, kurie Lietuvos Respublikos pilietybę įgijo juos įvaikinus arba pasikeitus tėvų pilietybei, neatsižvelgiant į jų gyvenamąją vietą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on decisions for persons to whom the citizenship of the Republic of Lithuania has been restored, granted by naturalization, simplified or exceptional procedure, who have returned the citizenship of the Republic of Lithuania, as well as decisions for children who have been established to have the citizenship of the Republic of Lithuania, who acquired the citizenship of the Republic of Lithuania after their adoption or change of the citizenship of their parents, regardless of their place of residence.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Prasymas](lt_pilietybe/Prasymas.md) | Prašymai dėl Lietuvos Respublikos pilietybės | `4` | `id` | `open` | `7` | — |
| [Sprendimas](lt_pilietybe/Sprendimas.md) | Sprendimai dėl Lietuvos Respublikos pilietybės suteikimo | `4` | `id` | `open` | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/lt_pilietybe (https://data.gov.lt/datasets/1943/)
