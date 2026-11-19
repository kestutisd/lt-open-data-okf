---
type: Table
title: "Application — Projekto paraiška"
description: "Spinta table datasets/gov/finmin/paraiskos/Application (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/Application"
tags: [gov, finmin, application, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2160/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Application — Projekto paraiška

- **Model:** `datasets/gov/finmin/paraiskos/Application`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/Application` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `project`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project` | `ref` | [Project](Project.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos (https://data.gov.lt/datasets/2160/)
