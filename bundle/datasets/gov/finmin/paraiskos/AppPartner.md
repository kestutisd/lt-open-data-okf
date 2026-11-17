---
type: Table
title: "AppPartner — Paraiškos partneriai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppPartner (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppPartner"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L50"
    last_modified: "2026-11-11T14:39:20Z"
---

# AppPartner — Paraiškos partneriai

- **Model:** `datasets/gov/finmin/paraiskos/AppPartner`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L50](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L50)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppPartner`
- **Primary Key (`ref`):** `app_partner_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_partner_id` | `string` | — | `4` | `open` | — | Paraiškos partnerio identifikatorius | — |
| `project` | `ref` | [Project](Project.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `partner` | `string` | — | `2` | `open` | — | Partnerio pavadinimas | Nerodomas, jei asmuo yra fizinis arba pavadinime yra fizinio asmens duomenų |
| `code` | `string` | — | `2` | `open` | — | Partnerio JAR kodas | Užsienio partneriams nurodyti analogiškų užsienio registrų kodai |
| `city_district` | `string` | — | `2` | `open` | — | Partnerio miestas / rajonas | — |
| `legal_form` | `string` | — | `3` | `open` | — | Partnerio teisinė forma | — |
| `legal_status` | `string` | — | `3` | `open` | — | Partnerio teisinis statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv
