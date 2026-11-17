---
type: Table
title: "Seniunaitija — Klaipėdos miesto savivaldybės seniūnaitijos"
description: "Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys/Seniunaitija"
tags: [gov, klaipedos_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25"
    last_modified: "2026-11-11T14:39:20Z"
---

# Seniunaitija — Klaipėdos miesto savivaldybės seniūnaitijos

Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. Šioje lentelėje pateikiamos Klaipėdos miesto savivaldybėje esančios seniūnaitojos bei jų teritorijų koordinatės. Duomenys pateikiami aktualūs šiai dienai.

Duomenų teikėjas: Klaipėdos miesto savivaldybė

- **Model:** `datasets/gov/klaipedos_m_sav/geografiniai_duomenys/Seniunaitija`[^manifest]
- **Dataset:** [Klaipėdos miesto savivaldybės objektų geografiniai duomenys](../geografiniai_duomenys.md) (`datasets/gov/klaipedos_m_sav/geografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys/Seniunaitija`
- **Primary Key (`ref`):** `object_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `object_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Seniūnaitijos pavadinimas | — |
| `apygarda` | `string` | — | `4` | `open` | — | Agygarda kuriai priklauso seniūnaitija | — |
| `geometrija` | `geometry(3346)` | — | `3` | `open` | — | Geometrija (teritorija) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv
