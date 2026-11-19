---
type: Dataset
title: "Klaipėdos uosto šiaurinio molo meteo informacija"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys"
tags: [gov, kvjud, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/meteo_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2360/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/meteo_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Klaipėdos uosto šiaurinio molo meteo informacija

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys. Rinkinyje pateikiami nuo 2024 m. gruodžio mėnesio kaupiami šiaurinio molo meteorologiniai duomenys. Šių matavimų metu matuojamas slėgis, rasos taškas, santykinė drėgmė, temperatūra, vėjo kryptis bei greitis. Vienas įrašas atitinka vieną matavimą. Matavimo stotelės koordinatės: 55.73057 21.07975. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/kvjud/meteo_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/meteo_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2360/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys`[^dcat]
- **Portal Title (`@lt`):** Klaipėdos uosto šiaurinio molo meteo informacija[^dcat]
- **Portal Title (`@en`):** Klaipėda port southern clay meteo information[^dcat]
- **Issued (`dct:issued`):** `2023-08-31`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-02-17` .. `2026-10-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys. Rinkinyje pateikiami nuo 2024 m. gruodžio mėnesio kaupiami šiaurinio molo meteorologinių sąlygų matavimo stoties duomenys. Šių matavimų metu matuojamas slėgis, rasos taškas, santykinė drėgmė, temperatūra, matomumas, vėjo kryptis bei greitis. Vienas įrašas atitinka vieną matavimą. Matavimo stotelės koordinatės: 55.73057 21.07975. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information of the meteorological station of the southern clay of Klaipėda port.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Matavimas](meteo_duomenys/Matavimas.md) | Klaipėdos uosto šiaurinio molo meteo informacija | `4` | `matavimo_laikas` | — | `10` | AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/meteo_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/meteo_duomenys (https://data.gov.lt/datasets/2360/)
