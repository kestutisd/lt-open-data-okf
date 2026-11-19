---
type: Dataset
title: "Nacionalinė mokėjimų agentūra"
description: "Rinkinyje skelbiami Automatinės laukų nuolatinio stebėjimo sistemos (ALNSIS) pasėlių heterogeniškumo (netolygumo) vertinimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nma"
tags: [gov, lsd, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3868/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/nma"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nacionalinė mokėjimų agentūra

- **Namespace:** `datasets/gov/lsd/nma`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nma` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3868/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/nma/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Pasėlių heterogeniškumo vertinimų duomenys[^dcat]
- **Portal Title (`@en`):** Data on applications for support for agricultural land and other areas and farmed animals[^dcat]
- **Issued (`dct:issued`):** `2025-07-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2025-07-21` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje skelbiami Automatinės laukų nuolatinio stebėjimo sistemos (ALNSIS) pasėlių heterogeniškumo (netolygumo) vertinimų duomenys. Algoritmas naudoja pikselinę klasifikaciją ir mašininio mokymo metodus, pagrįstus Sentinel-1 ir Sentinel-2 palydovų duomenimis, siekiant identifikuoti skirtingus augalų tipus, augimo fazes ir netolygumus pasėlių laukuose. Analizė padeda nustatyti pasėlių sudėtį bei galimas problemas, tokias kaip piktžolės ar nevienodas augimas. Algoritmo pagalba galima nustatyti, kokia yra reali augalų sudėtis deklaruotame pasėlyje – apskaičiuojamas skirtingų augalų tipų procentinis pasiskirstymas lauko viduje. Taip pat galima įvertinti, kokią dalį ploto faktiškai užima deklaruotas pasėlis, palyginti su kitais augalais ar žemės dangos elementais. Pateikiami duomenys apie pareiškėją, deklaruojamą lauką (žemės ūkio valdos atpažinties kodas, plotas, savivaldybė ir seniūnija) ir algoritmo būdu nustatytus pasėlių plotus, išreikštus procentais nuo viso ploto. Duomenų teikėjas – Nacionalinė mokėjimo agentūra prie Žemės ūkio ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

To be completed at a later date[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracija](nma/Deklaracija.md) | Pasėlių heterogeniškumo vertinimų duomenys | `4` | `paraiskos_id` | — | `21` | Rinkinyje skelbiami Automatinės laukų nuolatinio stebėjimo sistemos (ALNSIS) pasėlių heterogeniškumo (netolygumo) vertinimų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/nma (https://data.gov.lt/datasets/3868/)
