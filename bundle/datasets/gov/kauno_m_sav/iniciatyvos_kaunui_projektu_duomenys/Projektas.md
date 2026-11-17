---
type: Table
title: "Projektas — Organizacijų bei projektų duomenys"
description: "Spinta table datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projektas — Organizacijų bei projektų duomenys

- **Model:** `datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas`[^manifest]
- **Dataset:** [Projektų pagal programą 'Iniciatyvos Kaunui' duomenys](../iniciatyvos_kaunui_projektu_duomenys.md) (`datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Projektas`
- **Primary Key (`ref`):** `paraiskos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `konkurso_id` | `ref` | [Konkursas[konkurso_id]](Konkursas.md) | `4` | `open` | — | Konkurso identifikatorius | Išorinis raktas į konkurso lentelę |
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

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv
