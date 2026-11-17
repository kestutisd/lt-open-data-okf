---
type: Dataset
title: "Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys"
description: "Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt...."
resource: "https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras"
tags: [gov, vdtat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys

Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., registro duomenys

- **Namespace:** `datasets/gov/vdtat/saugiuju_dokumentu_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras`
- **Parent Namespace (`ns`):** Valstybės dokumentų technologinės apsaugos tarnyba prie FM (`datasets/gov/vdtat`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](saugiuju_dokumentu_registras/Dokumentas.md) | Saugiųjų dokumentų ir saugiųjų dokumentų blankų aprašomieji duomenys | `4` | `vda_prime_key` | — | 18 | Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo... |
| [Pavyzdys](saugiuju_dokumentu_registras/Pavyzdys.md) | Saugiųjų dokumentų ir blankų pavyzdžių sąrašas | — | `vda_prime_key` | — | 6 | Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo... |
| [ApsaugosPriemone](saugiuju_dokumentu_registras/ApsaugosPriemone.md) | Saugiųjų dokumentų ir blankų apsaugos priemonių sąrašas | — | `vda_prime_key` | — | 6 | Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv
