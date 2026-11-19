---
type: Dataset
title: "Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai"
tags: [gov, kvjud, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2860/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/sroviu_matavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės mėnesio kaupiami vertikaliu arba horizontaliu davikliu atliekamų vandens srovių matavimų duomenys. Šių matavimų metu nustatomas srovių greitis ir kryptis. Vienas įrašas atitinka vienu daviklių atliktą matavimą. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/kvjud/sroviu_matavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/sroviu_matavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2860/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai`[^dcat]
- **Portal Title (`@lt`):** Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys[^dcat]
- **Portal Title (`@en`):** The data for measuring water currents of Klaipėda State Seaport shall be accumulated in the geographical information system PortGIS of the Directorate of the State Seaport of Klaipėda AB. The package provides data on measurements of water currents performed by a vertical or horizontal sensor as of May 2016. These measurements shall determine the rate and direction of currents. One entry corresponds to a measurement performed by one sensor. Data provider – AB Klaipėda State Seaport Authority. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]
- **Issued (`dct:issued`):** `2024-11-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-25` .. `2025-10-19`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės mėnesio kaupiami vertikaliu arba horizontaliu davikliu atliekamų vandens srovių matavimų duomenys. Šių matavimų metu nustatomas srovių greitis ir kryptis. Vienas įrašas atitinka vieno daviklio atliktą matavimą. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The geographical information system PortGIS of AB Klaipėda State Seaport Authority collects geographic data of the seaport. The package provides data on measurements of water currents performed by a vertical or horizontal sensor as of May 2016. These measurements shall determine the rate and direction of currents. One entry corresponds to a measurement performed by one sensor. Data provider – AB Klaipėda State Seaport Authority. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Srove](sroviu_matavimai/Srove.md) | Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys | `4` | `vda_prime_key` | — | `8` | AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. |
| [Daviklis](sroviu_matavimai/Daviklis.md) | Klaipėdos valstybinio jūrų uosto vandens srovių daviklių duomenys | `4` | `vda_id` | — | `6` | AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/sroviu_matavimai (https://data.gov.lt/datasets/2860/)
