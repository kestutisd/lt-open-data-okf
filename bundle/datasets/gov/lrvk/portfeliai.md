---
type: Dataset
title: "Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys"
description: "Vyriausybės strateginio projektų portfelio duomenų rinkinyje pateikiami duomenys apie įgyvendinamus ir baigtus įgyvendinti Vyriausybės strateginius projektus."
resource: "https://get.data.gov.lt/datasets/gov/lrvk/portfeliai"
tags: [gov, lrvk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys

Vyriausybės strateginio projektų portfelio duomenų rinkinyje pateikiami duomenys apie įgyvendinamus ir baigtus įgyvendinti Vyriausybės strateginius projektus. Atskirai pateikiami duomenys apie projektus, jų teikiamas naudas ir pasiektus rezultatus. Duomenys apima laikotarpį nuo 2011 m. iki šių dienų.

Duomenų teikėjas: Lietuvos Respublikos Vyriausybės Kanceliarija.

- **Namespace:** `datasets/gov/lrvk/portfeliai`[^manifest]
- **Manifest CSV:** [datasets/gov/lrvk/portfeliai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Projektas](portfeliai/Projektas.md) | Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys | `4` | `vda_id` | — | 14 | Lentelės objektas - vienas vykdomas ar baigtas vykdyti projektas. |
| [Nauda](portfeliai/Nauda.md) | Lietuvos Respublikos Vyriausybės strateginio projektų portfelio teikiamų naudų duomenys | `4` | `naudos_id` | — | 12 | Lentelės objektas - projekto teikiama nauda. |
| [Rezultatas](portfeliai/Rezultatas.md) | Lietuvos Respublikos Vyriausybės strateginio projektų portfelio rezultatai | `4` | `vda_id` | — | 12 | Lentelės objektas - projekto rezultatas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv
