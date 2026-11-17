---
type: Table
title: "Konkursas — Konkursų skirtų projektams įgyvendinti duomenys"
description: "Spinta table datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# Konkursas — Konkursų skirtų projektams įgyvendinti duomenys

- **Model:** `datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas`[^manifest]
- **Dataset:** [Projektų pagal programą 'Iniciatyvos Kaunui' duomenys](../iniciatyvos_kaunui_projektu_duomenys.md) (`datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas`
- **Primary Key (`ref`):** `konkurso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `konkurso_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Konkurso kodas | Konkurso kodas randamas interneto svetainėje |
| `nuoroda` | `string` | — | `4` | `open` | — | Konkurso URL nuoroda | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Konkurso pavadinimas | — |
| `veiklos` | `string` | — | `4` | `open` | — | Konkurso veiklos | Konkurso veiklos kuriomis siekiamas įgyvendinti uždavinys |
| `prioritetai` | `string` | — | `4` | `open` | — | Konkurso prioritetai | Konkursui skirti prioritetai kuriuos turi įgyvendinti projektas |
| `paskelbimo_data` | `date` | `D` | `4` | `open` | — | Paraiškų teikimo pradžios data | — |
| `paraiskos_pateikimo_terminas` | `date` | `D` | `4` | `open` | — | Paraiškų teikimo pabaigos data | — |
| `procentas_nuosavo_indelio` | `string` | — | `4` | `open` | — | Procentinė dalis išlaidų kurias turi padengti pareiškėjas | — |
| `lesos_igyvendinimui` | `number` | — | `4` | `open` | — | Konkurso paskirtas biudžetas | Paskirtas biudžetas kuris išskirstomas kiekvienam projektui |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lesos_igyvendinimui` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv
