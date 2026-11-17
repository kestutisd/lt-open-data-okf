---
type: Dataset
title: "Šiaulių miesto savivaldybės geografiniai duomenys"
description: "Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys"
tags: [gov, siauliu_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Šiaulių miesto savivaldybės geografiniai duomenys

Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. Rinkinyje pateikiami šiuo metu aktualūs seniūnaitijų ribų bei sporto vietų duomenys. Tarp sporto vietų duomenų pateikiami ir atsakingų asmenų kontaktai, kurių pagalba galima rezervuoti aikštę, salę ir kt.

Duomenų teikėjas – Šiaulių miesto savivaldybės administracija.

- **Namespace:** `datasets/gov/siauliu_m_sav/geografiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys`
- **Parent Namespace (`ns`):** Šiaulių miesto savivaldybė (`datasets/gov/siauliu_m_sav`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SportoVieta](geografiniai_duomenys/SportoVieta.md) | Šiaulių miesto savivaldybės sporto vietos | `4` | `vda_prime_key` | — | 13 | Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. |
| [Seniunaitijos](geografiniai_duomenys/Seniunaitijos.md) | Šiaulių miesto savivaldybės seniūnaitijos | `4` | `vda_prime_key` | — | 6 | Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv
