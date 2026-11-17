---
type: Table
title: "DalyviuSarasas — Dalyvių sąrašas"
description: "Šiame rinkinyje pateiktas 2023 liepos 11-12 d. Vilniuje vykusio NATO viešojo forumo dalyvių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/resc/nato_public_forum_dalyviai/DalyviuSarasas"
tags: [gov, resc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/resc/ato_public_forum_dalyviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/resc/ato_public_forum_dalyviai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# DalyviuSarasas — Dalyvių sąrašas

Šiame rinkinyje pateiktas 2023 liepos 11-12 d. Vilniuje vykusio NATO viešojo forumo dalyvių sąrašas. Renginį bendrai organizavo NATO, Rytų Europos studijų centras (Lietuva), Atlantic Council (JAV), German Marshall Fund of the United States (JAV) ir Munich Security Conference (Vokietija).

- **Model:** `datasets/gov/resc/nato_public_forum_dalyviai/DalyviuSarasas`[^manifest]
- **Dataset:** [datasets/gov/resc/nato_public_forum_dalyviai](../nato_public_forum_dalyviai.md) (`datasets/gov/resc/nato_public_forum_dalyviai`)
- **Manifest CSV:** [datasets/gov/resc/ato_public_forum_dalyviai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/resc/ato_public_forum_dalyviai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/resc/nato_public_forum_dalyviai/DalyviuSarasas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `dalyvavimo_statusas` | `string` | — | `4` | `open` | — | Dalyvio statusas - techninis personalas / žiūrovas | — |
| `salis` | `string` | — | `4` | `open` | — | Atvykstanti šalis | — |
| `vardas` | `string` | — | `4` | `open` | — | Vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Pavardė | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `atstovaujama` | `string` | — | `4` | `open` | — | Atstovaujama įstaiga | — |
| `dalyvauja` | `string` | — | `4` | `open` | — | Dalyvauja / nedalyvauja / laukiama atsakymo | Reikšmės: y - taip, n - ne, p - nesulaukta atsakymo |
| `atvyk_lektuvu` | `string` | — | `4` | `open` | — | Ar Rytų Europos studijų centras perka bilietus lėktuvui. | Reikšmės: y - taip, n - ne, TBC - nesulaukta atsakymo |
| `viesbutis` | `string` | — | `4` | `open` | — | Rytų Europos studijų centro rezervuotas viešbutis dalyviui | — |
| `nefin_viesbutis` | `string` | — | `4` | `open` | — | Dalyvio savarankiškai apmokamas apgyvendinimo viešbutis | — |
| `akreditacija` | `boolean` | — | `4` | `open` | — | Ar surinkti visi duomenys akreditacijai | — |
| `issiusta_akreditacija` | `boolean` | — | `4` | `open` | — | Akreditacija išsiųsta saugumo patikrai | — |
| `kvietimas_isiustas` | `date` | `D` | `4` | `open` | — | Pakvietimas į forumą išsiųstas | — |
| `atvykimo_data` | `date` | `D` | `4` | `open` | — | Atvykimo data | — |
| `isvykimo_data` | `date` | `D` | `4` | `open` | — | Išvykimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Vyras | — |
| `lytis` | `"F"` | — | — | Moteris | — |
| `dalyvauja` | `"y"` | — | — | Taip | — |
| `dalyvauja` | `"n"` | — | — | Ne | — |
| `dalyvauja` | `"p"` | — | — | Nesulaukta atsakymo | — |
| `atvyk_lektuvu` | `"y"` | — | — | Taip | — |
| `atvyk_lektuvu` | `"n"` | — | — | Ne | — |
| `atvyk_lektuvu` | `"tbp"` | — | — | Nesulaukta atsakymo (tbc - to be confirmed) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/resc/ato_public_forum_dalyviai.csv
