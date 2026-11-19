---
type: Dataset
title: "Lietuvai reikšmingas kultūros paveldas, esantis užsienyje"
description: "Valstybinė kultūros paveldo komisija, vykdydama LR Vyriausybės patvirtintame Lietuvos Respublikos teritorijos bendrojo plano įgyvendinimo priemonių plane numatytą priemonę, nuo 2016 m. pradėjo rinkti ir duomenų bazėje U-PAVELDAS kaupti informaciją apie Lietuvai reikšmingą..."
resource: "https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas"
tags: [gov, vkpk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vkpk/kulturos_objektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3814/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vkpk/kulturos_paveldas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvai reikšmingas kultūros paveldas, esantis užsienyje

- **Namespace:** `datasets/gov/vkpk/kulturos_paveldas`[^manifest]
- **Manifest CSV:** [datasets/gov/vkpk/kulturos_objektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas` (`deployed`)[^manifest]
- **Provider:** `vkpk` — Valstybinė kultūros paveldo komisija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3814/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas`[^dcat]
- **Portal Title (`@lt`):** Lietuvai reikšmingas kultūros paveldas, esantis užsienyje[^dcat]
- **Portal Title (`@en`):** Cultural heritage of importance to Lithuania located abroad[^dcat]
- **Issued (`dct:issued`):** `2025-04-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybinė kultūros paveldo komisija, vykdydama LR Vyriausybės patvirtintame Lietuvos Respublikos teritorijos bendrojo plano įgyvendinimo priemonių plane numatytą priemonę, nuo 2016 m. pradėjo rinkti ir duomenų bazėje U-PAVELDAS kaupti informaciją apie Lietuvai reikšmingą kultūros paveldą, dėl susiklosčiusių nepalankių istorinių aplinkybių patekusį į svečias šalis. Duomenų rinkinyje pateikiamas kultūros paveldo objekto pavadinimas, aprašymas, kategorijos, laikotarpis, metai, miestas, šalis, WGS koordinatės, autoriai, susiję asmenys ir interneto svetainės adresas (URL). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The State Cultural Heritage Commission, as part of the measure provided for in the Plan of Measures for the Implementation of the General Plan of the TERRITORY of the REPUBLIC of Lithuania approved by the Government of the Republic of Lithuania, has since 2016 started collecting and collecting information in the U-HERITAGE database about the cultural heritage of importance to Lithuania which has entered the guest countries due to adverse historical circumstances. The dataset shall include the name, description, categories, period, year, city, country, WGS coordinates, authors, related persons and website address (URL) of the cultural heritage object. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KulturosObjektas](kulturos_paveldas/KulturosObjektas.md) | Lietuvai reikšmingas kultūros paveldas, esantis užsienyje | `4` | `id` | — | `13` | Duomenų rinkinyje pateikiamas kultūros paveldo objekto pavadinimas, aprašymas, kategorijos, laikotarpis, metai, miestas, šalis, WGS koordinatės, autoriai... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkpk/kulturos_objektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vkpk/kulturos_paveldas (https://data.gov.lt/datasets/3814/)
