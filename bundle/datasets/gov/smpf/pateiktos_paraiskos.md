---
type: Dataset
title: "Švietimo mainų paramos fondo paraiškos ir lektorių programos"
description: "Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų ir lektorių programų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos"
tags: [gov, smpf, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Švietimo mainų paramos fondo paraiškos ir lektorių programos

Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų ir lektorių programų duomenys. Duomenų rinkinį sudaro dvi lentelės, sujungtos „paraiskos_nr“ stulpeliu. Vieną duomenų rinkinio lentelę sudaro į Lietuvoje organizuojamus renginius pateiktų paraiškų duomenys, o kitoje lentelėje pateikiamos Lietuvos dėstytojų / lektorių renginiams siūlomos programos. Viena duomenų rinkinio eilutė atitinka vieną paraišką arba vieną dėstytojo programą.

- **Namespace:** `datasets/gov/smpf/pateiktos_paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/smpf/pateiktos_paraiskos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/smpf/pateiktos_paraiskos.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/smpf/pateiktos_paraiskos`
- **Parent Namespace (`ns`):** VšĮ Švietimo mainų paramos fondas (SMPF) (`datasets/gov/smpf`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paraiska](pateiktos_paraiskos/Paraiska.md) | Švietimo mainų paramos fondo paraiškos | `4` | `vda_prime_key` | — | 16 | Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugomi pateiktų paraiškų duomenys. |
| [LektoriausPrograma](pateiktos_paraiskos/LektoriausPrograma.md) | Švietimo mainų paramos fondo lektorių siūlomos programos | `4` | `vda_prime_key` | `open` | 14 | Rinkinyje pateikiami VšĮ Švietimo mainų paramos fondo nuo 2023 m. kaupiami ir saugom lektorių siūlomų programų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/smpf/pateiktos_paraiskos.csv
