---
type: Dataset
title: "Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje"
description: "\"Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/fenologija"
tags: [gov, lhmt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2851/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lhmt/fenologija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje

"Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą. Viena rinkinio eilutė atitinka tam tikro augalo vieną fenologinio tarpsnio fazę konkrečią dieną. Vienoje eilutėje esančius duomenis sudaro: augalo pavadinimas, fenologinio tarpsnio fazė, stebėjimo data, stebėjimo stoties pavadinimas ir koordinatės, duomenų gavimo į LHMT informacinę sistemą data. Fazės kodo ir fazės stadijos kodo stulpelių pora nurodo konkretų fazės pavadinimą, kuris gaunamas iš fazių klasifikatoriaus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/lhmt/fenologija`[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/augalu_fenologija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/fenologija` (`deployed`)[^manifest]
- **Provider:** `lhmt` — Lietuvos hidrometeorologijos tarnyba (LHMT) *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2851/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lhmt/fenologija`[^dcat]
- **Portal Title (`@lt`):** Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje[^dcat]
- **Portal Title (`@en`):** Phenological stages of flowering plants registered by the Lithuanian Hydrometeorological Service in Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-11-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą. Viena rinkinio eilutė atitinka tam tikro augalo vieną fenologinio tarpsnio fazę konkrečią dieną. Vienoje eilutėje esančius duomenis sudaro: augalo pavadinimas, fenologinio tarpsnio fazė, stebėjimo data, stebėjimo stoties pavadinimas ir koordinatės, duomenų gavimo į LHMT informacinę sistemą data. Fazės kodo ir fazės stadijos kodo stulpelių pora nurodo konkretų fazės pavadinimą, kuris gaunamas iš fazių klasifikatoriaus. Duomenų teikėjas – Lietuvos hidrometeorologijos tarnyba prie Aplinkos ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data of the Lithuanian Hydrometeorological Service (LHMT) on the monitoring of phenological intervals of flourishing plants in Lithuania. One row is recorded as one phase of a phenological phase for a given plant on a specific day. One line consists of the name of the plant, the phase of the phenological phase, the date of observation, the name of the station (where the observation was made), the coordinates of the STATION, and the date on which the data to THE LHMT information system was received during the YEAR. A pair of phase code columns and phase stage code columns indicate a specific phase name that is derived from the phase classifier. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AugaluFenologija](fenologija/AugaluFenologija.md) | LHMT duomenys apie Lietuvoje žydinčių augalų fenologinius tarpsnius | `4` | `vda_pk` | — | `10` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lhmt/fenologija (https://data.gov.lt/datasets/2851/)
