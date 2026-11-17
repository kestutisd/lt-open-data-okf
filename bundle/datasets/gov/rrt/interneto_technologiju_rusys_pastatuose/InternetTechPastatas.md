---
type: Table
title: "InternetTechPastatas — Fiksuotojo ryšio tinklų geografinis ir technologinis Išvystymas Lietuvoje"
description: "Rinkinyje pateikiami Lietuvos Respublikos Ryšių reguliavimo tarnybai Viešųjų fiksuotojo ryšio tinklų teikėjų pateikti fiksuotojo ryšio tinklų geografinio ir technologinio išvystymo pastatuose duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose/InternetTechPastatas"
tags: [gov, rrt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# InternetTechPastatas — Fiksuotojo ryšio tinklų geografinis ir technologinis Išvystymas Lietuvoje

Rinkinyje pateikiami Lietuvos Respublikos Ryšių reguliavimo tarnybai Viešųjų fiksuotojo ryšio tinklų teikėjų pateikti fiksuotojo ryšio tinklų geografinio ir technologinio išvystymo pastatuose duomenys. Pastatų adresai pateikiami 1km dydžio stačiakampėmis gardelėmis. Vienoje eilutėje atvaizduojama viena interneto technologija pastate per vienerius metus. Duomenys pateikiami nuo 2023 metų ir atnaujinami kiekvienų metų balandžio mėn.

- **Model:** `datasets/gov/rrt/interneto_technologiju_rusys_pastatuose/InternetTechPastatas`[^manifest]
- **Dataset:** [Fiksuotojo ryšio tinklų geografinis ir technologinis Išvystymas Lietuvoje](../interneto_technologiju_rusys_pastatuose.md) (`datasets/gov/rrt/interneto_technologiju_rusys_pastatuose`)
- **Manifest CSV:** [datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose/InternetTechPastatas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `iraso_sukurimo_data` | `date` | `D` | `4` | `open` | — | Metai, už kuriuos pateikti duomenys | — |
| `pastato_id` | `string` | — | `4` | `open` | — | Pastato identifikavimo kodas | — |
| `interneto_technologija` | `string` | — | `4` | `open` | — | Pastate esanti interneto technologija | — |
| `grid_id` | `ref` | [/datasets/gov/lsd/grid/Grid1KmSq](../../lsd/grid/Grid1KmSq.md) | `4` | `open` | — | 1x1 km stačiakampės pastato adreso gardelės identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje yra pastatas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `interneto_technologija` | `"Varinės linijos su VSDL"` | — | — | Varinės linijos su VSDL | — |
| `interneto_technologija` | `"Varinės linijos be VSDL"` | — | — | Varinės linijos be VSDL | — |
| `interneto_technologija` | `"Pasyvios šviesolaidinės linijos"` | — | — | Pasyvios šviesolaidinės linijos | — |
| `interneto_technologija` | `"Aktyvios šviesolaidinės linijos"` | — | — | Aktyvios šviesolaidinės linijos | — |
| `interneto_technologija` | `"Bendraašio kabelio linijos su DOCSIS3 ir vėlesniu"` | — | — | Bendraašio kabelio linijos su DOCSIS3 ir vėlesniu | — |
| `interneto_technologija` | `"Bendraašio kabelio linijos be DOCSIS3 ir vėlesnio"` | — | — | Bendraašio kabelio linijos be DOCSIS3 ir vėlesnio | — |
| `interneto_technologija` | `"FWA"` | — | — | FWA | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv
