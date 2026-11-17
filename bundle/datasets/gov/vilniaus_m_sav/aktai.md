---
type: Dataset
title: "Vilniaus miesto savivaldybės teisės aktų registras"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto savivaldybės teisės aktų registras

Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai. Duomenys apima laikotarpį nuo 1990 m. Rinkinio objektas – vienas dokumentas. Rinkinyje kaupiami istoriniai duomenys, todėl įtraukti ir nustoję galioti teisės aktai. Skelbiami šie teisės aktų požymiai: pavadinimas, paskelbimo data, potvarkio numeris, aktą paskelbęs savivaldybės subjektas ir akto statusas. Vartotojai taip pat gali analizuoti paskelbtų teisės aktų tarpusavio ryšius – kurie dokumentai susiję, keičia ar yra priedai kitiems teisės aktams (žr. modelį Jungimas).

Duomenų teikėjas – Vilniaus miesto savivaldybės administracija.

- **Namespace:** `datasets/gov/vilniaus_m_sav/aktai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/aktai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](aktai/Dokumentas.md) | Vilniaus miesto savivaldybės teisės aktai | `4` | `dokumento_id` | — | 8 | — |
| [Jungimas](aktai/Jungimas.md) | Vilniaus miesto savivaldybės teisės aktų tarpusavio sąryšiai | `4` | `rysio_id` | — | 4 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv
