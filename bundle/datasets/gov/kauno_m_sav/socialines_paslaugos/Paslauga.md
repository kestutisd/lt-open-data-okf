---
type: Table
title: "Paslauga — Kauno miesto savivaldybės suteiktos socialinės paslaugos"
description: "Šiame rinkinyje pateikiamos Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje fiksuojamos suteiktos paslaugos."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos/Paslauga"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/socialines_paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga — Kauno miesto savivaldybės suteiktos socialinės paslaugos

Šiame rinkinyje pateikiamos Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje fiksuojamos suteiktos paslaugos. Viena eilutė atitinka vieną suteiktą paslaugą atitinkamam asmeniui.

Duomenys pateikiami nuo 2000m. ir iki dabar. Duomenų apimtis, Kauno miesto savivaldybės gabentojai.

- **Model:** `datasets/gov/kauno_m_sav/socialines_paslaugos/Paslauga`[^manifest]
- **Dataset:** [datasets/gov/kauno_m_sav/socialines_paslaugos](../socialines_paslaugos.md) (`datasets/gov/kauno_m_sav/socialines_paslaugos`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos/Paslauga`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Pradžia | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Pabaiga | — |
| `asmens_pseudo_id` | `string` | — | `4` | `open` | — | Asmens pseudo identifikatorius | Pseudo id sudarytas iš asmens vardo, pavardės ir gimimo datos. Vėliau viskas užšifruota |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Vardas pavardė | Užšifruotas asmens vardas ir pavardė |
| `gimimo_metai` | `date` | `D` | `4` | `open` | — | Gimimo metai | — |
| `gavejo_kategorija` | `string` | — | `4` | `open` | — | Paslaugų gavėjo kategorija | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslauga | — |
| `paslaugos_teikejas` | `string` | — | `4` | `open` | — | Paslaugos tiekėjas | — |
| `pasl_sav_lesos` | `number` | — | `4` | `open` | — | Paslaugos kaina, finansuota savivaldybės lėšomis | — |
| `pasl_vals_lesos` | `number` | — | `4` | `open` | — | Paslaugos kaina, finansuota valstybės lėšomis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/socialines_paslaugos.csv
