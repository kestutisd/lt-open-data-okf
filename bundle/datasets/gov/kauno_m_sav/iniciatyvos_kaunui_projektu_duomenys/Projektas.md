---
type: Table
title: "Projektas — Organizacijų bei projektų duomenys"
description: "Lentelėse pateikti Kauno miesto savivaldybės programos 'Iniciatyvos Kaunui' projektų, konkursų bei projektų išlaidų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas"
tags: [gov, kauno_m_sav, projektas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projektas — Organizacijų bei projektų duomenys

**Dataset Context:** Lentelėse pateikti Kauno miesto savivaldybės programos 'Iniciatyvos Kaunui' projektų, konkursų bei projektų išlaidų duomenys. Projektų duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Rinkinys sudarytas Valstybės duomenų agentūros. Projektų lentelės viena eilutė atitinka vieną paraišką, konkursų lentelės – tam tikrą konkursą, skirtą projekto finansavimui gauti, o projektų išlaidų lentelės – paraiškos sąmatą. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Duomenys apima Kaune išsidėsčiusias organizacijas. Duomenų laiko aprėptis – nuo 2024 m. gruodžio 1d. Duomenų teikėjas – Kauno miesto savivaldybė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas`[^manifest]
- **Dataset:** [Projektų pagal programą 'Iniciatyvos Kaunui' duomenys](../iniciatyvos_kaunui_projektu_duomenys.md) (`datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `paraiskos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `konkurso_id` | `ref` | [Konkursas](Konkursas.md) (`level=4 UUID` via `Konkursas[konkurso_id]`: `konkurso_id._id`) | `4` | `open` | — | Konkurso identifikatorius | Išorinis raktas į konkurso lentelę |
| `pareiskejas` | `string` | — | `4` | `open` | — | Organizacijos pavadinimas | Pareiškėjo įmonės, viešosios įstaigos, ar kitos organizacijos pavadinimas |
| `paraiskos_pav` | `string` | — | `4` | `open` | — | Paraiškos pavadinimas | — |
| `paraiskos_teikimo_momentas` | `datetime` | `S` | `4` | `open` | — | Paraiškos teikimo momentas | Momentas kada buvo sukurtas įrašas sistemoje |
| `vykdymo_pradzia` | `date` | `D` | `4` | `open` | — | Projekto vykdymo pradžia | — |
| `vykdymo_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto vykdymo pabaiga | — |
| `paraiskos_busena` | `string` | — | `4` | `open` | — | Paraiškos būsena | Būsena nusakanti paraiškos dabartinį statusą |
| `sutarties_busena` | `string` | — | `4` | `open` | — | Sutarties būsena | Būsena nusakanti Sutarties dabartinį statusą (Null => sutartis nesudaryta) |
| `prasoma_suma` | `number` | — | `4` | `open` | — | Projektui įgyvendinti prašoma suma | Paskirtas biudžetas kurį nurodo pareiškėjas |
| `galutine_suma` | `number` | — | `4` | `open` | — | Projektui įgyvendinti skirta suma | Paskirtas biudžetas kuris bus skirtas projekto įgyvendinimui |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paraiskos_busena` | `"Atmesta"` | — | — | Paraiška atmesta | — |
| `paraiskos_busena` | `"Finansuojama"` | — | — | Paraiška finansuojama (galutinė suma) | — |
| `paraiskos_busena` | `"Nefinansuojama"` | — | — | Paraiška nefinansuojama | — |
| `paraiskos_busena` | `"Projektas vykdomas (sutartis sudaryta)"` | — | — | Projektas vykdomas | — |
| `paraiskos_busena` | `"Projektas įvykdytas"` | — | — | Projektas įvykdytas | — |
| `paraiskos_busena` | `"Projektas įvykdytas su lėšų grąžinimu"` | — | — | Projektas įvykdytas su lėšų grąžinimu | — |
| `sutarties_busena` | `"Atsisakė sudaryti sutartį"` | — | — | Pareiškėjas atsisakė sudaryti sutartį | — |
| `sutarties_busena` | `"Vykdoma"` | — | — | Sutartis vykdoma | — |
| `sutarties_busena` | `"Įvykdyta"` | — | — | Sutartis įvykdyta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasoma_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `galutine_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6)
