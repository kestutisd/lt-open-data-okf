---
type: Dataset
title: "datasets/gov/ivpk/adp/catalog"
description: "Lithuanian open data dataset datasets/gov/ivpk/adp/catalog (24 lentelės)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/ivpk/adp/catalog

- **Namespace:** `datasets/gov/ivpk/adp/catalog`[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `24` (24 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Category](catalog/Category.md) | Kategorija | — | — | — | `11` | — |
| [Comment](catalog/Comment.md) | Komentarai | — | — | — | `8` | — |
| [ExternalSite](catalog/ExternalSite.md) | Išorinis atvirų duomenų katalogas | — | — | — | `8` | — |
| [Format](catalog/Format.md) | Duomenų formatai | — | — | — | `8` | — |
| [Frequency](catalog/Frequency.md) | Periodiškumas | — | — | — | `7` | Duomenų atnaujinimo periodiškumas |
| [Licence](catalog/Licence.md) | Licencija | — | — | — | `8` | — |
| [Municipality](catalog/Municipality.md) | Savivaldybė | — | — | — | `5` | — |
| [OpenDataGovLtEntry](catalog/OpenDataGovLtEntry.md) | Informacijos rinkmenų sąrašas | — | — | — | `21` | Duomenys perkelti iš senojo opendata.gov.lt atvirų duomenų katalogo. |
| [Organization](catalog/Organization.md) | Organizacija | — | — | — | `15` | Organizacija teikianti atvirus duomenis. |
| [Region](catalog/Region.md) | Apskritys | — | — | — | `5` | — |
| [RequestStructure](catalog/RequestStructure.md) | Pageidaujamos duomenų struktūros laukas | — | — | — | `9` | Teikiant prašymus gauti duomenis yra galimybė pateikti kokių konkrečių duomenų laukų reikia arba trūksta duomenų rinkinyje. |
| [UserLike](catalog/UserLike.md) | Poreikio „patinka“ paspaudimai | — | — | — | `5` | — |
| [Catalog](catalog/Catalog.md) | Atvirų duomenų katalogas | — | — | — | `10` | Atvirų duomenų katalogas, kuris yra sinchronizuojamas su Lietuvos atvirų duomenų katalogu. |
| [Dataset](catalog/Dataset.md) | — | — | — | — | `32` | — |
| [DatasetEvent](catalog/DatasetEvent.md) | — | — | — | — | `7` | — |
| [Request](catalog/Request.md) | — | — | — | — | `19` | — |
| [Usecase](catalog/Usecase.md) | — | — | — | — | `12` | — |
| [DatasetDistribution](catalog/DatasetDistribution.md) | — | — | — | — | `22` | — |
| [DatasetStructure](catalog/DatasetStructure.md) | Duomenų struktūros aprašas | — | — | — | `10` | — |
| [DatasetVisit](catalog/DatasetVisit.md) | Duomenų rinkinio peržiūros | — | — | — | `7` | Šiuo metu duomenų rinkinio peržiūros fiksuojamos visiems puslapio atidarymo atvejams, greičiauisiai didžiąją dalį peržiūrų sugeneruoja paieškos botai, todėl... |
| [RequestEvent](catalog/RequestEvent.md) | — | — | — | — | `9` | — |
| [UsecaseDataset](catalog/UsecaseDataset.md) | — | — | — | — | `2` | — |
| [UserDatasetSubscription](catalog/UserDatasetSubscription.md) | — | — | — | — | `6` | — |
| [UserVote](catalog/UserVote.md) | — | — | — | — | `5` | — |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `Status` | `'INVENTORED'` | — | — | Atlikta inventorizacija | — |
| `Status` | `'PRIORITIZED'` | — | — | Numatitas prioritetas | — |
| `Status` | `'FINANCING'` | — | — | Skirtas finansavimas | — |
| `Status` | `'METADATA'` | — | — | Pateikti metaduomenys | — |
| `Status` | `'HAS_DATA'` | — | — | Atverti duomenys | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `adms` | `https://www.w3.org/ns/adms#` |
| `dc` | `http://purl.org/dc/elements/1.1/` |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |
| `dctype` | `http://purl.org/dc/dcmitype/` |
| `dqv` | `http://www.w3.org/ns/dqv#` |
| `earl` | `http://www.w3.org/ns/earl#` |
| `foaf` | `http://xmlns.com/foaf/0.1/` |
| `geosparql` | `http://www.opengis.net/ont/geosparql#` |
| `locn` | `http://www.w3.org/ns/locn#` |
| `oa` | `http://www.w3.org/ns/oa#` |
| `odrl` | `http://www.w3.org/ns/odrl/2/` |
| `org` | `http://www.w3.org/ns/org#` |
| `owl` | `http://www.w3.org/2002/07/owl#` |
| `prov` | `http://www.w3.org/ns/prov#` |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `sdmx-attribute` | `http://purl.org/linked-data/sdmx/2009/attribute#` |
| `sdo` | `https://schema.org/` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `time` | `http://www.w3.org/2006/time#` |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` |
| `w3cgeo` | `http://www.w3.org/2003/01/geo/wgs84_pos#` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L2)
