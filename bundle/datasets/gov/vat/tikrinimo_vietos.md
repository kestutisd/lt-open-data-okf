---
type: Dataset
title: "Informacija apie įvežamų augalų, augalinių produktų ir kitų objektų saugojimo ir muitinio tikrinimo vietas"
description: "Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo tipas ir..."
resource: "https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/tikrinimo_vietos"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Informacija apie įvežamų augalų, augalinių produktų ir kitų objektų saugojimo ir muitinio tikrinimo vietas

Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo tipas ir numeris; sandėlio / terminalo adresas) Pateikiama informacija apie Patikrinimo vietas, pripažintas tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo adresas)[^manifest]

- **Namespace:** `datasets/gov/vat/tikrinimo_vietos`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/tikrinimo_vietos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1857/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos`[^dcat]
- **Portal Title (`@lt`):** Informacija apie įvežamų augalų, augalinių produktų ir kitų objektų saugojimo ir muitinio tikrinimo vietas[^dcat]
- **Portal Title (`@en`):** Information on places of storage and customs inspection of imported plants, plant products and other objects[^dcat]
- **Issued (`dct:issued`):** `2023-06-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-06-06` .. `2023-06-13`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo tipas ir numeris; sandėlio / terminalo adresas) Pateikiama informacija apie Patikrinimo vietas, pripažintas tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo adresas). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Provide information on the places of storage and customs inspection recognized as suitable for the storage of plants, plant products and other related objects (certificate number; date of issue of the certificate; name and number of the warehouse / terminal; address of the warehouse / terminal) , recognized as suitable for phytosanitary inspection for storage of plants, plant products and other objects entering the Republic of Lithuania and the European Union (certificate number; date of issue of the certificate; name of the economic entity; address of the warehouse / terminal)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Muitine](tikrinimo_vietos/Muitine.md) | Prekių saugojimo ir muitinio tikrinimo vietos, pripažintos tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti | `4` | `eil_nr` | `open` | `6` | — |
| [FitosanitarineVieta](tikrinimo_vietos/FitosanitarineVieta.md) | Patikrinimo vietos, pripažintos tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti | — | `eil_nr` | — | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/tikrinimo_vietos (https://data.gov.lt/datasets/1857/)
