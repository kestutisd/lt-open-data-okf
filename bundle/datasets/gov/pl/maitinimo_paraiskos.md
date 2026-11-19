---
type: Dataset
title: "Prienų ligoninės maitinimo paraiškos"
description: "Šiame rinkinyje pateikiamas VšĮ Prienų ligoninės maitinimo paraiškos: dienos patiekalų sąrašas, dietos, dienos maistinė vertė, valgančiųjų kiekis."
resource: "https://get.data.gov.lt/datasets/gov/pl/maitinimo_paraiskos"
tags: [gov, pl, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pl/pl_maitinimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pl/pl_maitinimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2929/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pl/maitinimo_paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Prienų ligoninės maitinimo paraiškos

- **Namespace:** `datasets/gov/pl/maitinimo_paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/pl/pl_maitinimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pl/pl_maitinimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pl/maitinimo_paraiskos` (`deployed`)[^manifest]
- **Provider:** `pl` — VšĮ Prienų ligoninė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2929/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pl/maitinimo_paraiskos`[^dcat]
- **Portal Title (`@lt`):** Gydymo įstaigos pacientų maitinimo paraiškos[^dcat]
- **Portal Title (`@en`):** Medical institution patients' feeding applications[^dcat]
- **Issued (`dct:issued`):** `2025-02-05`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-02-05` .. `2026-10-24`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateikiamas VšĮ Prienų ligoninės maitinimo paraiškos: dienos patiekalų sąrašas, dietos, dienos maistinė vertė, valgančiųjų kiekis. Duomenys pateikiami nuo 2019 metų pabaigos iki dabar. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This kit includes food applications from Prienai Hospital: a list of daily meals, diets, daily nutritional value, and eating amount. The data is provided between the end of 2019 and now. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Maitinimas](maitinimo_paraiskos/Maitinimas.md) | Prienų ligoninės maitinimo paraiškos | `4` | `vda_id` | — | `10` | Šiame rinkinyje pateikiamas Prienų ligoninės maitinimo paraiškos: dienos patiekalų sąrašas, dietos, dienos maistinė vertė, valgančiųjų kiekis. |

[^manifest]: atviriduomenys/manifest — datasets/gov/pl/pl_maitinimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pl/pl_maitinimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pl/maitinimo_paraiskos (https://data.gov.lt/datasets/2929/)
