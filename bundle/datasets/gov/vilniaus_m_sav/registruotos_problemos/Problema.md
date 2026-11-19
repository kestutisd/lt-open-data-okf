---
type: Table
title: "Problema — Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje"
description: "Viena platformos „Tvarkau miestą“ duomenų rinkinio eilutė atitinka vieną vartotojo pranešimą apie problemą Vilniaus miesto savivaldybėje."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/registruotos_problemos/Problema"
tags: [gov, vilniaus_m_sav, problema, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3894/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/registruotos_problemos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Problema — Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje

Viena platformos „Tvarkau miestą“ duomenų rinkinio eilutė atitinka vieną vartotojo pranešimą apie problemą Vilniaus miesto savivaldybėje. Rinkinį sudaro: problemos tipas, statusas ir statuso atnaujinimo data, už problemos sprendimą atsakingas padalinys, problemos registravimo ir išsprendimo datos, transporto priemonės valstybinis numeris ir numerio struktūra (jei problema susijusi su transporto priemone), problemos vietos adresas ir koordinatės. Vilniaus miesto savivaldybę apimantys duomenys renkami nuo 2012 metų ir bus atnaujinami kas mėnesį. Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/registruotos_problemos/Problema`[^manifest]
- **Dataset:** [Platformoje „Tvarkau miestą“ vartotojų užregistruotos problemos Vilniaus miesto savivaldybėje](../registruotos_problemos.md) (`datasets/gov/vilniaus_m_sav/registruotos_problemos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/registruotos_problemos/Problema` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pranesimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pranesimo_id` | `string` | — | `4` | `open` | — | Unikalus pirminis raktas | — |
| `problemos_tipas` | `string` | — | `4` | `open` | — | Vartotojo registruotos problemos tipas | — |
| `problemos_statusas` | `string` | — | `4` | `open` | — | Problemos statusas | — |
| `statuso_atnaujinimo_data` | `datetime` | `L` | `4` | `open` | — | Problemos statuso atnaujinimo data | — |
| `atsak_padal` | `string` | — | `4` | `open` | — | Už problemos sprendimą atsakingas padalinys | — |
| `problem_pirmenybe` | `string` | — | `4` | `open` | — | Problemos sprendimo pirmenybė | — |
| `problem_reg_data` | `date` | `D` | `4` | `open` | — | Problemos registravimo data | — |
| `problem_issprend_data` | `date` | `D` | `4` | `open` | — | Problemos išsprendimo data | — |
| `valstybinis_nr` | `string` | — | `4` | `open` | — | Automobilio valstybinis numeris | — |
| `valst_nr_struktura` | `string` | — | `4` | `open` | — | Automobilio valstybinio numerio struktūra | — |
| `problem_viet_adresas` | `string` | — | `4` | `open` | — | Problemos vietos adresas | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Problemos vietos lgumos koordinatė wgs | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Problemos vietos platumos koordinatė wgs | — |
| `geometrija_wgs` | `geometry(point, 4326)` | — | `4` | `open` | — | Problemos vietos taško koordinatės wgs | — |
| `ilguma_lks` | `integer` | — | `4` | `open` | — | Problemos vietos ilgumos koordinatė lks | — |
| `platuma_lks` | `integer` | — | `4` | `open` | — | Problemos vietos platumos koordinatė lks | — |
| `geometrija_lks` | `geometry(point, 3346)` | — | `4` | `open` | — | Problemos vietos taško koordinatės lks | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `problemos_statusas` | `"Išnagrinėta"` | — | — | Išnagrinėta | — |
| `problemos_statusas` | `"Registruota"` | — | — | Registruota | — |
| `problemos_statusas` | `"Nagrinėjama"` | — | — | Nagrinėjama | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/registruotos_problemos.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/registruotos_problemos (https://data.gov.lt/datasets/3894/)
