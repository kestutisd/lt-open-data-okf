---
type: Dataset
title: "Lietuvos sėklinės miško bazės objektų sąrašai"
description: "Lietuvos miško sėklinės bazės sąvado paskirtis - rinkti, kaupti, apdoroti, sisteminti, saugoti, naudoti ir teikti duomenis apie miško sėklinės bazės objektus."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sekline"
tags: [gov, miskai, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sekline"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lietuvos sėklinės miško bazės objektų sąrašai

- **Namespace:** `datasets/gov/miskai/sekline`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sekline.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sekline` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `10` (10 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/739/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė miškų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/miskai/sekline`[^dcat]
- **Portal Title (`@lt`):** Lietuvos sėklinės miško bazės objektų sąrašai[^dcat]
- **Portal Title (`@en`):** Compilation of Lithuanian forest seed base[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-21` .. `2024-07-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos miško sėklinės bazės sąvado paskirtis - rinkti, kaupti, apdoroti, sisteminti, saugoti, naudoti ir teikti duomenis apie miško sėklinės bazės objektus. Sėklinės miško bazės objektai atrenkami vadovaujantis Valstybinės miškų tarnybos tvirtinama Genetinių miško medžių išteklių atrankos metodika ir Miško dauginamosios medžiagos nuostatais. Sėklinė miško bazė kuriama ir vystoma taikant pažangius selekcijos metodus, vadovaujantis Miško dauginamosios medžiagos nuostatų reikalavimais. Iš jos gauta dauginamoji medžiaga naudojama miškui želdinti, moksliniams tyrimams, miško medžių selekcijos ir sėklininkystės darbams vykdyti.[^dcat]

### Portal Description (`@en`)

The purpose of the Lithuanian Forest Seed Base Compilation is to collect, store, process, systematize, store, use and provide data on forest seed base objects.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MDMCategory](sekline/MDMCategory.md) | Miško dauginamosios medžiagos kategorija | `4` | — | — | `2` | — |
| [MDMDistributionOpportunity](sekline/MDMDistributionOpportunity.md) | Miško dauginamosios medžiagos platinimo galimybė | `4` | — | — | `1` | — |
| [ObjectStatus](sekline/ObjectStatus.md) | Objekto statusas | `4` | — | — | `3` | — |
| [SeedBaseType](sekline/SeedBaseType.md) | Sėklinės bazės tipas | `4` | — | — | `1` | — |
| [TreeTypeGroup](sekline/TreeTypeGroup.md) | Medžių grupė | `4` | — | — | `2` | — |
| [Owner](sekline/Owner.md) | Valdytojas | `4` | — | — | `1` | — |
| [TreeType](sekline/TreeType.md) | Medžio tipas | `4` | — | — | `5` | — |
| [Forestry](sekline/Forestry.md) | Girininkija | `4` | — | — | `2` | — |
| [OriginDistrict](sekline/OriginDistrict.md) | Kilmės rajonas | `4` | — | — | `3` | — |
| [Object](sekline/Object.md) | Sėklinės bazės objektas | `4` | — | — | `17` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sekline.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sekline.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sekline (https://data.gov.lt/datasets/739/)
