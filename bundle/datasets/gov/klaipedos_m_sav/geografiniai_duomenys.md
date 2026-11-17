---
type: Dataset
title: "Klaipėdos miesto savivaldybės objektų geografiniai duomenys"
description: "Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys"
tags: [gov, klaipedos_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Klaipėdos miesto savivaldybės objektų geografiniai duomenys

Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. Pateikiamos lentelės apie šiuos objektus:

• Prekybos vietos

• Seniūnaitijos

• Sporto vietos

• Žaidimų aikštelės

Pateikiami patys objektai bei jų koordinatės aktualūs šiai dienai. Kiekvienos lentelės viena eilutė atitinką vieną objektą Klaipėdos miesto savivaldybėje.

Duomenų teikėjas: Klaipėdos miesto savivaldybė

- **Namespace:** `datasets/gov/klaipedos_m_sav/geografiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys`
- **Parent Namespace (`ns`):** Klaipėdos miesto savivaldybė (`datasets/gov/klaipedos_m_sav`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PrekybosVieta](geografiniai_duomenys/PrekybosVieta.md) | Klaipėdos miesto savivaldybėje esančios prekybos vietos | `4` | `object_id` | — | 7 | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |
| [Seniunaitija](geografiniai_duomenys/Seniunaitija.md) | Klaipėdos miesto savivaldybės seniūnaitijos | `4` | `object_id` | — | 5 | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |
| [SportoVieta](geografiniai_duomenys/SportoVieta.md) | Klaipėdos miesto savivaldybėje esančios sporto vietos | `4` | `vda_prime_key` | — | 9 | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |
| [ZaidimuAikstele](geografiniai_duomenys/ZaidimuAikstele.md) | Klaipėdos miesto savivaldybėje esančios žaidimų aikštelės | `4` | `object_id` | — | 7 | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv
