---
type: Table
title: "Seniunaitijos — Šiaulių miesto savivaldybės seniūnaitijos"
description: "Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys/Seniunaitijos"
tags: [gov, siauliu_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# Seniunaitijos — Šiaulių miesto savivaldybės seniūnaitijos

Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. Rinkinyje pateikiami šiuo metu aktualūs seniūnaitijų ribų duomenys.

Duomenų teikėjas – Šiaulių miesto savivaldybės administracija.

- **Model:** `datasets/gov/siauliu_m_sav/geografiniai_duomenys/Seniunaitijos`[^manifest]
- **Dataset:** [Šiaulių miesto savivaldybės geografiniai duomenys](../geografiniai_duomenys.md) (`datasets/gov/siauliu_m_sav/geografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys/Seniunaitijos`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `nr` | `string` | — | `4` | `open` | — | Numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `informacija` | `string` | — | `4` | `open` | — | Informacija | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Geometrija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv
