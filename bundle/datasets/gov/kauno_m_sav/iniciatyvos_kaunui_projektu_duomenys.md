---
type: Dataset
title: "Projektų pagal programą 'Iniciatyvos Kaunui' duomenys"
description: "Lentelėse pateikti Kauno miesto savivaldybės programos 'Iniciatyvos Kaunui' projektų, konkursų bei projektų išlaidų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys"
tags: [gov, kauno_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projektų pagal programą 'Iniciatyvos Kaunui' duomenys

Lentelėse pateikti Kauno miesto savivaldybės programos 'Iniciatyvos Kaunui' projektų, konkursų bei projektų išlaidų duomenys. Projektų duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Rinkinys sudarytas Valstybės duomenų agentūros. Projektų lentelės viena eilutė atitinka vieną paraišką, konkursų lentelės – tam tikrą konkursą, skirtą projekto finansavimui gauti, o projektų išlaidų lentelės – paraiškos sąmatą. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Duomenys apima Kaune išsidėsčiusias organizacijas. Duomenų laiko aprėptis – nuo 2024 m. gruodžio 1d. Duomenų teikėjas – Kauno miesto savivaldybė.

- **Namespace:** `datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Projektas](iniciatyvos_kaunui_projektu_duomenys/Projektas.md) | Organizacijų bei projektų duomenys | `4` | `paraiskos_id` | — | 11 | — |
| [Konkursas](iniciatyvos_kaunui_projektu_duomenys/Konkursas.md) | Konkursų skirtų projektams įgyvendinti duomenys | `4` | `konkurso_id` | — | 10 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv
