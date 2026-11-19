---
type: Table
title: "DalyviuSarasas — Dalyvių sąrašas"
description: "Šiame rinkinyje pateiktas 2023 liepos 11-12 d."
resource: "https://get.data.gov.lt/datasets/gov/resc/nato_public_forum_dalyviai/DalyviuSarasas"
tags: [gov, resc, dalyviusarasas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/resc/ato_public_forum_dalyviai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/resc/ato_public_forum_dalyviai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2733/"
    title: "data.gov.lt DCAT-AP — datasets/gov/resc/nato_public_forum_dalyviai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# DalyviuSarasas — Dalyvių sąrašas

Šiame rinkinyje pateiktas 2023 liepos 11-12 d. Vilniuje vykusio NATO viešojo forumo dalyvių sąrašas. Renginį bendrai organizavo NATO, Rytų Europos studijų centras (Lietuva), Atlantic Council (JAV), German Marshall Fund of the United States (JAV) ir Munich Security Conference (Vokietija).[^manifest]

- **Model:** `datasets/gov/resc/nato_public_forum_dalyviai/DalyviuSarasas`[^manifest]
- **Dataset:** [„NATO“ public forum dalyvių registro duomenys](../nato_public_forum_dalyviai.md) (`datasets/gov/resc/nato_public_forum_dalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/resc/ato_public_forum_dalyviai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/resc/ato_public_forum_dalyviai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/resc/nato_public_forum_dalyviai/DalyviuSarasas` (`deployed`)[^manifest]
- **Provider:** `resc` — Rytų Europos studijų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Vyras | — |
| `lytis` | `"F"` | — | — | Moteris | — |
| `dalyvauja` | `"y"` | — | — | Taip | — |
| `dalyvauja` | `"n"` | — | — | Ne | — |
| `dalyvauja` | `"p"` | — | — | Nesulaukta atsakymo | — |
| `atvyk_lektuvu` | `"y"` | — | — | Taip | — |
| `atvyk_lektuvu` | `"n"` | — | — | Ne | — |
| `atvyk_lektuvu` | `"tbp"` | — | — | Nesulaukta atsakymo (tbc - to be confirmed) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/resc/ato_public_forum_dalyviai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/resc/ato_public_forum_dalyviai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/resc/nato_public_forum_dalyviai (https://data.gov.lt/datasets/2733/)
