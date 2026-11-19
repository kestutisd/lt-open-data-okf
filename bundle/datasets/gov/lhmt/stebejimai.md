---
type: Dataset
title: "Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys."
description: "Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/stebejimai"
tags: [gov, lhmt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lhmt/stebejimai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3872/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lhmt/stebejimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys.

- **Namespace:** `datasets/gov/lhmt/stebejimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/stebejimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/stebejimai` (`deployed`)[^manifest]
- **Provider:** `lhmt` — Lietuvos hidrometeorologijos tarnyba (LHMT) *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3872/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lhmt/stebejimai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys[^dcat]
- **Portal Title (`@en`):** Meteorological observations of Lithuanian meteorological stations[^dcat]
- **Issued (`dct:issued`):** `2025-07-18`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-07-18` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys. Viena eilutė atitinka vieną matavimą. Duomenų rinkinį sudaro stoties pavadinimas ir kodas, stoties lokacijos koordinatės, stebėjimo laikas, reali ir juntamoji oro temperatūra, vėjo greitis, vėjo gūsis, vėjo kryptis, debesuotumas, slėgis jūros lygmenyje, santykinė oro drėgmė, kritulių kiekis ir oro sąlygos. Duomenų aprėptis – visi sukaupti duomenys nuo 2013 m. Duomenis numatyta atnaujinti kasdien. Duomenų teikėjas – Lietuvos hidrometeorologijos tarnyba (LHMT). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The set contains meteorological observations of the Lithuanian meteorological stations. One line corresponds to one measurement. The dataset consists of the station name and code, station location coordinates, observation time, real and sensory air temperature, wind speed, wind gust, wind direction, cloudiness, sea level pressure, relative air humidity, rainfall and weather conditions. Data coverage: All data collected since 2013. The data is scheduled to be updated daily. Data provider – Lithuanian Hydrometeorological Service (LHMT). Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Matavimas](stebejimai/Matavimas.md) | Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys. | `4` | `vda_prime_key` | — | `16` | Duomenų rinkinį sudaro stoties pavadinimas ir kodas, stoties lokacijos koordinatės, stebėjimo laikas, reali ir juntamoji oro temperatūra stebėjimo metu... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/stebejimai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lhmt/stebejimai (https://data.gov.lt/datasets/3872/)
