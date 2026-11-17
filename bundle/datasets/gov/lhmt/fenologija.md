---
type: Dataset
title: "Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje"
description: "Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/fenologija"
tags: [gov, lhmt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje

Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą. Viena rinkinio eilutė atitinka tam tikro augalo vieną fenologinio tarpsnio fazę konkrečią dieną. Vienoje eilutėje esančius duomenis sudaro: augalo pavadinimas, fenologinio tarpsnio fazė, stebėjimo data, stebėjimo stoties pavadinimas ir koordinatės, duomenų gavimo į LHMT informacinę sistemą data. Fazės kodo ir fazės stadijos kodo stulpelių pora nurodo konkretų fazės pavadinimą, kuris gaunamas iš fazių klasifikatoriaus.

- **Namespace:** `datasets/gov/lhmt/fenologija`[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/augalu_fenologija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/fenologija`
- **Parent Namespace (`ns`):** Lietuvos hidrometeorologijos tarnyba (LHMT) (`datasets/gov/lhmt`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AugaluFenologija](fenologija/AugaluFenologija.md) | LHMT duomenys apie Lietuvoje žydinčių augalų fenologinius tarpsnius | `4` | `vda_pk` | — | 10 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv
