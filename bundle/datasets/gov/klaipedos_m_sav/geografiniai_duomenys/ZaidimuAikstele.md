---
type: Table
title: "ZaidimuAikstele — Klaipėdos miesto savivaldybėje esančios žaidimų aikštelės"
description: "Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys/ZaidimuAikstele"
tags: [gov, klaipedos_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L47"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZaidimuAikstele — Klaipėdos miesto savivaldybėje esančios žaidimų aikštelės

Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. Šioje lentelėje pateikiamos Klaipėdos miesto savivaldybėje esančios žaidimų aikštelės bei jų koordinatės. Duomenys pateikiami aktualūs šiai dienai.

Duomenų teikėjas: Klaipėdos miesto savivaldybė

- **Model:** `datasets/gov/klaipedos_m_sav/geografiniai_duomenys/ZaidimuAikstele`[^manifest]
- **Dataset:** [Klaipėdos miesto savivaldybės objektų geografiniai duomenys](../geografiniai_duomenys.md) (`datasets/gov/klaipedos_m_sav/geografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L47)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys/ZaidimuAikstele`
- **Primary Key (`ref`):** `object_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `object_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas | — |
| `irengta` | `string` | — | `4` | `open` | — | Ar įrengta | — |
| `pastabos` | `string` | — | `3` | `open` | — | Pastabos (įrengimo data) | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 3346)` | — | `3` | `open` | — | Geometrija (lokacija) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv
