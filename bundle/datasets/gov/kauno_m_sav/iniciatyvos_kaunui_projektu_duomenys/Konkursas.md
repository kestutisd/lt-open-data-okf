---
type: Table
title: "Konkursas — Konkursų skirtų projektams įgyvendinti duomenys"
description: "Lentelėse pateikti Kauno miesto savivaldybės programos 'Iniciatyvos Kaunui' projektų, konkursų bei projektų išlaidų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas"
tags: [gov, kauno_m_sav, konkursas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Konkursas — Konkursų skirtų projektams įgyvendinti duomenys

**Dataset Context:** Lentelėse pateikti Kauno miesto savivaldybės programos 'Iniciatyvos Kaunui' projektų, konkursų bei projektų išlaidų duomenys. Projektų duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Rinkinys sudarytas Valstybės duomenų agentūros. Projektų lentelės viena eilutė atitinka vieną paraišką, konkursų lentelės – tam tikrą konkursą, skirtą projekto finansavimui gauti, o projektų išlaidų lentelės – paraiškos sąmatą. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Duomenys apima Kaune išsidėsčiusias organizacijas. Duomenų laiko aprėptis – nuo 2024 m. gruodžio 1d. Duomenų teikėjas – Kauno miesto savivaldybė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas`[^manifest]
- **Dataset:** [Projektų pagal programą 'Iniciatyvos Kaunui' duomenys](../iniciatyvos_kaunui_projektu_duomenys.md) (`datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys/Konkursas` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `konkurso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/iniciatyvos_kaunui_projektu_duomenys.csv#L30)
