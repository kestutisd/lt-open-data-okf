---
type: Dataset
title: "Valstybinio požeminio vandens monitoringo lygio matavimų duomenys"
description: "Požeminio vandens lygis kartą per parą matuojamas 74 gręžiniuose elektroniniais davikliais, 20 gręžinių įrengtos telemetrinės lygio matavimo duomenų perdavimos sistemos Požeminio vandens lygis konkrečioje vietovėje priklauso nuo meteorologinių ir geologinių sąlygų."
resource: "https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys"
tags: [gov, lgt, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lgt/poz_vandens_lygiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1338/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybinio požeminio vandens monitoringo lygio matavimų duomenys

- **Namespace:** `datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/poz_vandens_lygiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1338/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos geologijos tarnyba prie Aplinkos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys`[^dcat]
- **Portal Title (`@lt`):** Valstybinio požeminio vandens monitoringo lygio matavimų duomenys[^dcat]
- **Portal Title (`@en`):** Groundwater level observation data from the state groundwater monitoring[^dcat]
- **Issued (`dct:issued`):** `2022-10-12`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2022-10-12` .. `2026-07-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Požeminio vandens lygis kartą per parą matuojamas 74 gręžiniuose elektroniniais davikliais, 20 gręžinių įrengtos telemetrinės lygio matavimo duomenų perdavimos sistemos Požeminio vandens lygis konkrečioje vietovėje priklauso nuo meteorologinių ir geologinių sąlygų. Greičiausiai į meteorologinių sąlygų pasikeitimus reaguoja negiliai (iki 5 m) slūgsantis, molingose nuogulose besikaupiantis gruntinis vanduo, kurio lygis per metus pakyla ir nusileidžia kelis metrus. Giliau slūgsančiame vandenyje lygio pokytis tesiekia kelis centimetrus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Groundwater level is measured daily in 74 wells with electronic sensors, 20 wells are equipped with telemetric level data transmission systems. Groundwater levels in a given area depend on meteorological and geological conditions. Shallow (up to 5 m) groundwater accumulating in clayey sediments, the level of which rises and falls by several meters during the year, is most likely to react to changes in meteorological conditions. In deeper water, the change in level is only a few centimeters.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PozeminioVandensLygis](valstybinio_pozeminio_vlm_duomenys/PozeminioVandensLygis.md) | Valstybinio požeminio vandens monitoringo matavimų duomenys | `4` | `eiles_nr` | — | `11` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/poz_vandens_lygiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/poz_vandens_lygiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/valstybinio_pozeminio_vlm_duomenys (https://data.gov.lt/datasets/1338/)
