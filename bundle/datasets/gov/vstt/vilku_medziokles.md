---
type: Dataset
title: "Sumedžioti vilkai Lietuvoje"
description: "Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles"
tags: [gov, vstt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sumedžioti vilkai Lietuvoje

Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. Rinkinio objektas – vienas sumedžiotas vilkas. Rinkinyje nurodomas medžioklės laikas, vieta, būdas, duomenys apie vilką (amžius, lytis, sveikatos būklė) ir gaują (jauniklių ir suaugusių vilkų skaičius). Atskirai pateikiama ir sumedžiotų vilkų statistika savivaldybės ir datos tikslumu.

Duomenų teikėjas – Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos.

- **Namespace:** `datasets/gov/vstt/vilku_medziokles`[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/medziokles.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SavivaldybeDiena](vilku_medziokles/SavivaldybeDiena.md) | Statistika apie sumedžiotus vilkus Lietuvos savivaldybėse | `4` | `vda_id` | — | 4 | Pateikiama sumedžiotų vilkų statistika savivaldybės ir datos tikslumu. |
| [Vilkas](vilku_medziokles/Vilkas.md) | Duomenys apie sumedžiotus vilkus | `4` | `vda_id` | — | 14 | Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv
