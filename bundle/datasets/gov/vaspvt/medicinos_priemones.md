---
type: Dataset
title: "Sveikatos priežiūros įstaigų įsigytos medicininės priemonės"
description: "Duomenų rinkinyje pateikiami įrašai apie sveikatos priežiūros įstaigų įsigytas medicinines priemones."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones"
tags: [gov, vaspvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_priemones.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sveikatos priežiūros įstaigų įsigytos medicininės priemonės

Duomenų rinkinyje pateikiami įrašai apie sveikatos priežiūros įstaigų įsigytas medicinines priemones. Viena eilutė atitinka vieną įsigytą priemonę. Įrašai apie įsigytas medicinines priemones pradėti fiksuoti apytiksliai nuo 2010 m. Rinkinį sudaro: priemonės pavadinimas, modelis, CE (pranc. Conformité Européene) žyma, CE numeris, priemonės savininko JAR kodas ir pavadinimas, priemonės pagaminimo, įsigyjimo, naudojimo pradžios ir nutraukimo datos bei nutraukimo priežastis. Duomenų teikėjas: Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos apsaugos ministerijos.

- **Namespace:** `datasets/gov/vaspvt/medicinos_priemones`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_priemones.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedicininePriemone](medicinos_priemones/MedicininePriemone.md) | Sveikatos priežiūros įstaigų įsigytos medicininės priemonės | `4` | `pri_id` | — | 12 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_priemones.csv
