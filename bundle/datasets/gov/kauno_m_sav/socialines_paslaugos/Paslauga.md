---
type: Table
title: "Paslauga — Kauno miesto savivaldybės suteiktos socialinės paslaugos"
description: "Šiame rinkinyje pateikiamos Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje fiksuojamos suteiktos paslaugos."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos/Paslauga"
tags: [gov, kauno_m_sav, paslauga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2773/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/socialines_paslaugos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paslauga — Kauno miesto savivaldybės suteiktos socialinės paslaugos

Šiame rinkinyje pateikiamos Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje fiksuojamos suteiktos paslaugos. Viena eilutė atitinka vieną suteiktą paslaugą atitinkamam asmeniui. Duomenys pateikiami nuo 2000m. ir iki dabar. Duomenų apimtis, Kauno miesto savivaldybės gabentojai. PASITEIRAVIMUI: Valstybės duomenų valdysenos atvėrimo komanda: atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/socialines_paslaugos/Paslauga`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės suteiktos socialinės paslaugos](../socialines_paslaugos.md) (`datasets/gov/kauno_m_sav/socialines_paslaugos`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos/Paslauga` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/socialines_paslaugos (https://data.gov.lt/datasets/2773/)
