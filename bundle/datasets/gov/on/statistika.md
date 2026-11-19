---
type: Dataset
title: "Oro Navigacijos skrydžių statistikos duomenys"
description: "Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/on/statistika"
tags: [gov, "on", deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/on/flight_data.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2890/"
    title: "data.gov.lt DCAT-AP — datasets/gov/on/statistika"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Oro Navigacijos skrydžių statistikos duomenys

Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės. Nurodoma su skrydžiais susijusi informacija: skrydžio data, orlaivio tipas, skrydį operavęs oro vežėjas, išvykimo ir atvykimo laikai bei išvykimo ir atvykimo oro uostai. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/on/statistika`[^manifest]
- **Manifest CSV:** [datasets/gov/on/flight_data.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/statistika` (`deployed`)[^manifest]
- **Provider:** `on` — Oro Navigacija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2890/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/on/statistika`[^dcat]
- **Portal Title (`@lt`):** Oro Navigacijos skrydžių statistikos duomenys[^dcat]
- **Portal Title (`@en`):** Air Navigation Flight Statistics[^dcat]
- **Issued (`dct:issued`):** `2024-12-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės. Nurodoma su skrydžiais susijusi informacija: skrydžio data, orlaivio tipas, skrydį operavęs oro vežėjas, išvykimo ir atvykimo laikai bei išvykimo ir atvykimo oro uostai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package shall include data on flights held in Lithuanian airspace from the Air Navigation Flight Statistics Database. The information related to flights shall include: date of flight, type of aircraft, air carrier operating the flight, times of departure and arrival and airports of departure and arrival. If you have any questions about the dataset, please contact the State Data Control Opening Team by e-mail atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Skrydis](statistika/Skrydis.md) | Oro Navigacijos skrydžių statistikos duomenys | `4` | `vda_id` | — | `21` | Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/on/flight_data.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/on/statistika (https://data.gov.lt/datasets/2890/)
