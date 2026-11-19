---
type: Dataset
title: "Lietuvos Respublikos visuotinio gyventojų ir būstų surašymo rezultatų duomenys"
description: "Pateikiami Lietuvos Respublikos 2011, 2021 metų visuotinio gyventojų ir būstų surašymo rezultatų geoerdviniai duomenys bei 2020 m. atlikto bandomojo gyventojų surašymo rezultatai.2021 m. surašymas buvo atliktas administracinių duomenų pagrindu, naudojant pagrindinių valstybės..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas"
tags: [gov, lsd, deployed, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1911/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# Lietuvos Respublikos visuotinio gyventojų ir būstų surašymo rezultatų duomenys

- **Namespace:** `datasets/gov/lsd/gyventojai_bustas`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gyventojai_bustas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1911/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos visuotinio gyventojų ir būstų surašymo rezultatų duomenys[^dcat]
- **Portal Title (`@en`):** Population and housing censuses[^dcat]
- **Issued (`dct:issued`):** `2022-10-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-25`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DECENNIAL` (`http://publications.europa.eu/resource/authority/frequency/DECENNIAL`)[^dcat]
- **Distribution Date Span:** `2022-04-21` .. `2022-04-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami Lietuvos Respublikos 2011, 2021 metų visuotinio gyventojų ir būstų surašymo rezultatų geoerdviniai duomenys bei 2020 m. atlikto bandomojo gyventojų surašymo rezultatai.2021 m. surašymas buvo atliktas administracinių duomenų pagrindu, naudojant pagrindinių valstybės registrų ir informacinių sistemų duomenis (Lietuvos Respublikos gyventojų registro, Nekilnojamojo turto registro, Adresų registro, SODROS duomenų bazės ir kt.). Lietuvos Respublikos 2020 metų bandomojo gyventojų surašymo rezultatų geoerdviniai duomenys buvo gauti apibendrinus administracinių šaltinių duomenis ir juos lokalizavus teritorijoje. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Geospatial data of the results of the General Population and Housing Census of the Republic of Lithuania for 2011, 2021 and 2020 are presented. Results of a pilot census conducted in The census was conducted on the basis of administrative data, using data from the main state registers and information systems (Register of Residents of the Republic of Lithuania, Register of Real Estate, Register of Addresses, SODRA Database, etc.). The geospatial data of the results of the pilot population census of the Republic of Lithuania in 2020 were obtained by summarizing the data from administrative sources and localizing them in the territory.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyvBustGeoDuom100M2011](gyventojai_bustas/GyvBustGeoDuom100M2011.md) | Gyventojų ir būstų surašymo geoerdviniai duomenys 100x100 gardelėse 2011 m. | — | — | — | `39` | — |
| [GyvBustGeoDuom250M2011](gyventojai_bustas/GyvBustGeoDuom250M2011.md) | Gyventojų ir būstų surašymo geoerdviniai duomenys 250x250 gardelėse 2011 m. | — | — | — | `39` | — |
| [GyvBustGeoDuom500M2011](gyventojai_bustas/GyvBustGeoDuom500M2011.md) | Gyventojų ir būstų surašymo geoerdviniai duomenys 500x500 gardelėse 2011 m. | — | — | — | `39` | — |
| [GyvGeoTer1Km2020](gyventojai_bustas/GyvGeoTer1Km2020.md) | Gyventojų surašymo geoerdviniai duomenys 1x1 km gardelėse 2020 m. | — | — | — | `16` | — |
| [GyvGeoTer2020](gyventojai_bustas/GyvGeoTer2020.md) | Gyventojų surašymo geoerdviniai duomenys 2020 m. | — | — | — | `69` | — |
| [GyvSur100M2021](gyventojai_bustas/GyvSur100M2021.md) | Gyventojų surašymo duomenys 100x100m 2021 m. | — | — | — | `19` | — |
| [GyvSur250M2021](gyventojai_bustas/GyvSur250M2021.md) | Gyventojų surašymo duomenys 250x250m 2021 m. | — | — | — | `19` | — |
| [GyvSur500M2021](gyventojai_bustas/GyvSur500M2021.md) | Gyventojų surašymo duomenys 500x500m 2021 m. | — | — | — | `19` | — |
| [GyvSur1Km2021](gyventojai_bustas/GyvSur1Km2021.md) | Gyventojų surašymo duomenys 1x1km 2021 m. | — | — | — | `45` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas (https://data.gov.lt/datasets/1911/)
