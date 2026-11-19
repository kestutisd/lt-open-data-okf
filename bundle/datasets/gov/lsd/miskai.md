---
type: Dataset
title: "Miškų būklės tyrimo duomenys"
description: "Miškų būklės tyrimo duomenys, parengti pagal projekto „Bandomosios ekosistemų apimties ir miškų būklės sąskaitos“ duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/miskai"
tags: [gov, lsd, deployed, cadence-triennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/misku_bukle.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/misku_bukle.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2066/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/miskai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Miškų būklės tyrimo duomenys

Miškų būklės tyrimo duomenys, parengti pagal projekto „Bandomosios ekosistemų apimties ir miškų būklės sąskaitos“ duomenis. Duomenys siejami su eksperimentės ekosistemų statistikos projekto II-ojo etapo - baziniu miško rodiklių duomenų rinkiniu pagal ekosistemų būklės rodiklių grupes ir klases. Rodikliai apskaičiuoti ir pateikti pagal atitinkamus erdvinius vienetus laikotarpio pradžioje, apie 2000 m. (žymima raide 'x') ir 2021 m. pabaigoje.[^manifest]

- **Namespace:** `datasets/gov/lsd/miskai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/misku_bukle.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/misku_bukle.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/miskai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2066/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/miskai`[^dcat]
- **Portal Title (`@lt`):** Miškų būklės tyrimo duomenys[^dcat]
- **Portal Title (`@en`):** Forest condition survey data[^dcat]
- **Issued (`dct:issued`):** `2022-11-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `TRIENNIAL` (`http://publications.europa.eu/resource/authority/frequency/TRIENNIAL`)[^dcat]
- **Distribution Date Span:** `2022-11-16` .. `2022-11-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Projektą finansuoja Europos Sąjunga. Europos Komisija neprisiima jokios atsakomybės už jame esančios informacijos naudojimą. Parengta pagal projekto „Bandomosios ekosistemų apimties ir miškų būklės sąskaitos“ duomenis. Miškų būklės tyrimo duomenys, parengti pagal projekto „Bandomosios ekosistemų apimties ir miškų būklės sąskaitos“ duomenis, seniūnijų ir gardelių (1x1 km) lygmeniu kaip erdvinis poligonų (Polygon Feature) elementų sluoksnis. Duomenys siejami su eksperimentinės ekosistemų statistikos projekto II-ojo etapo - baziniu miško rodiklių duomenų rinkiniu pagal ekosistemų būklės rodiklių grupes ir klases. Rodikliai apskaičiuoti ir pateikti pagal atitinkamus erdvinius vienetus laikotarpio pradžioje, apie 2000 m. (žymima raide 'x') ir pabaigoje - 2021 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The forest condition survey data, prepared according to the data of the project &quot;Experimental Ecosystem Volume and Forest Condition Account&quot;, at the level of municipalities. The data is linked to the second stage of the experimental ecosystem statistics project - the basic data set of forest indicators according to the groups and classes of indicators of the state of ecosystems. The indicators are calculated and presented according to the relevant spatial units at the beginning of the period, around 2000. (denoted by the letter &#39;x&#39;) and at the end - 2021.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Seniunija](miskai/Seniunija.md) | Miškų būklės tyrimo duomenys seniūnijų lygmeniu | — | — | — | `37` | Miškų būklės tyrimo duomenys, parengti pagal projekto „Bandomosios ekosistemų apimties ir miškų būklės sąskaitos“ duomenis, seniūnijų lygmeniu |
| [Gardele](miskai/Gardele.md) | Miškų būklės tyrimo duomenys gardelių (1x1 km) lygmeniu | — | — | — | `37` | Miškų būklės tyrimo duomenys, parengti pagal projekto „Bandomosios ekosistemų apimties ir miškų būklės sąskaitos“ duomenis, gardelių (1x1 km) lygmeniu. |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/misku_bukle.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/misku_bukle.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/miskai (https://data.gov.lt/datasets/2066/)
