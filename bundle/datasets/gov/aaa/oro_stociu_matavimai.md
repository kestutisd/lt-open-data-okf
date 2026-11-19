---
type: Dataset
title: "Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys"
description: "Lietuvos valstybinio aplinkos oro monitoringo automatinių stočių sistemą sudaro 14 miesto oro kokybės tyrimų stočių, veikiančių Vilniaus, Kauno, Klaipėdos, Šiaulių, Panevėžio, Jonavos, Kėdainių, Naujosios Akmenės ir Mažeikių miestuose ir 3 integruoto monitoringo stotys..."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai"
tags: [gov, aaa, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/500/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys

- **Namespace:** `datasets/gov/aaa/oro_stociu_matavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/500/`[^dcat]
- **Publisher (`dct:publisher`):** Aplinkos apsaugos agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys[^dcat]
- **Portal Title (`@en`):** Air quality data[^dcat]
- **Issued (`dct:issued`):** `2023-06-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-06-22` .. `2026-10-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos valstybinio aplinkos oro monitoringo automatinių stočių sistemą sudaro 14 miesto oro kokybės tyrimų stočių, veikiančių Vilniaus, Kauno, Klaipėdos, Šiaulių, Panevėžio, Jonavos, Kėdainių, Naujosios Akmenės ir Mažeikių miestuose ir 3 integruoto monitoringo stotys, veikiančios Aukštaitijos, Žemaitijos ir Dzūkijos nacionaliniuose parkuose. Automatinėse oro kokybės tyrimų stotyse matuojamos šių teršalų koncentracijos: kietųjų dalelių KD10, smulkesnių kietųjų dalelių KD2,5, azoto oksidų (NO2, NOx, NO), sieros dioksido (SO2), anglies monoksido (CO), ozono (O3), benzeno, gyvsidabrio. Tyrimai atliekami ir matavimų rezultatai pateikiami įgyvendinant Europos Parlamento ir Tarybos direktyvų 2004/107/EB dėl arseno, kadmio, gyvsidabrio, nikelio ir policiklinių aromatinių angliavandenilių aplinkos ore ir 2008/50/EB dėl aplinkos oro kokybės ir švaresnio oro Europoje reikalavimus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The system of automatic state ambient air monitoring stations in Lithuania consists of 14 urban air quality monitoring stations operating in Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys, Jonava, Kėdainiai, Naujoji Akmenė and Mažeikiai and 3 integrated monitoring stations operating in Aukštaitija, Žemaitija and Dzūkija National Parks. Concentrations of the following pollutants are measured at automatic air quality monitoring stations: particulate matter PM10, fine particulate matter PM2.5, nitrogen oxides (NO2, NOx, NO), sulfur dioxide (SO2), carbon monoxide (CO), ozone (O3), benzene, mercury. The tests and measurements shall be carried out in accordance with the requirements of Directives 2004/107/EC of the European Parliament and of the Council relating to arsenic, cadmium, mercury, nickel and polycyclic aromatic hydrocarbons in ambient air and 2008/50/EC on ambient air quality and cleaner air for Europe.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Station](oro_stociu_matavimai/Station.md) | Oro kokybės matavimo stotys | `4` | `stat_num` | — | `3` | — |
| [Units](oro_stociu_matavimai/Units.md) | Matavimo vienetai | `4` | `code_unit` | — | `3` | — |
| [Quantity](oro_stociu_matavimai/Quantity.md) | Teršalai | `4` | `code_quantity` | — | `6` | — |
| [Averages](oro_stociu_matavimai/Averages.md) | Valandiniai oro kokybės matavimai | `4` | `id` | — | `6` | — |
| [QuantityUnits](oro_stociu_matavimai/QuantityUnits.md) | Tarpinė lenta | `4` | `code_combi` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai (https://data.gov.lt/datasets/500/)
