---
type: Table
title: "Application — Projekto paraiška"
description: "Spinta table datasets/gov/finmin/paraiskos/Application (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/Application"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# Application — Projekto paraiška

- **Model:** `datasets/gov/finmin/paraiskos/Application`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/Application`
- **Primary Key (`ref`):** `project`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project` | `ref` | [Project](Project.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `project_name` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `receive_date` | `date` | `D` | `4` | `open` | — | Paraiškos gavimo data | — |
| `applicant` | `string` | — | `2` | `open` | — | Pareiškėjo pavadinimas | Nerodomas, jei asmuo yra fizinis arba pavadinime yra fizinio asmens duomenų |
| `applicant_code` | `string` | — | `2` | `open` | — | Pareiškėjo JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `subject_legal_form` | `string` | — | `3` | `open` | — | Subjekto teisinė forma | — |
| `description` | `string` | — | `4` | `open` | — | Projekto santrauka | — |
| `county` | `string` | — | `2` | `open` | — | Apskritis, kuriai tenka didžioji dalis projekto lėšų | — |
| `municipality` | `string` | — | `2` | `open` | — | Savivaldybė, kuriai tenka didžioji dalis projekto lėšų | — |
| `in_another_eu` | `boolean` | — | `4` | `open` | — | Projektas ar jo dalis įgyvendinami kitoje ES valstybėje narėje (ne Lietuvos Respublikoje) | — |
| `outside_eu` | `boolean` | — | `4` | `open` | — | Projektas ar jo dalis įgyvendinami už ES teritorijos ribų | — |
| `duration` | `integer` | `mo` | `4` | `open` | — | Projekto įgyvendinimo trukmė (mėnesiais) | — |
| `principles` | `boolean` | — | `4` | `open` | — | Projekto įgyvendinimo metu bus užtikrintas horizontaliųjų principų laikymasis | — |
| `progress` | `string` | — | `4` | `open` | — | Darnus vystymasis | — |
| `gender_equality` | `string` | — | `4` | `open` | — | Moterų ir vyrų lygybė ir (arba) nediskriminavimas | — |
| `insert_date` | `datetime` | `L` | `4` | `open` | — | Paraiškos įregistravimo data | — |
| `other_municipality` | `string` | — | `2` | `open` | — | Kita(-os) savivaldybė(-ės), kuriai(-ioms) tenka dalis projekto lėšų | Savivaldybės atskirtos kableliais, arba nurodyta "Visos savivaldybės" |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `other_municipality` | `"update(property: ""other_municipality[]"", type: ""array"", source: ""Other_municipality"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv
