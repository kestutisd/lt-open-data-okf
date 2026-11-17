---
type: Table
title: "Patikrinimas — Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai."
description: "Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas/Patikrinimas"
tags: [gov, pagd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patikrinimas — Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai.

Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys. Rinkinį sudaro: pranešimo numeris ir data, patikrinimo pradžia ir pabaiga, statinio paskirtis, objekto grupė, apskritis, seniūnija, gyvenvietė bei koordinatės.

- **Model:** `datasets/gov/pagd/statinio_patikrinimas/Patikrinimas`[^manifest]
- **Dataset:** [Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai.](../statinio_patikrinimas.md) (`datasets/gov/pagd/statinio_patikrinimas`)
- **Manifest CSV:** [datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas/Patikrinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pranesimo_nr` | `string` | — | `4` | `open` | — | Pranešimo numeris | — |
| `pranesimo_data` | `date` | `D` | `4` | `open` | — | Pranešimo data | — |
| `patikrinimo_pradzia` | `date` | `D` | `4` | `open` | — | Patikrinimo pradžia | — |
| `patikrinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Patikrinimo pabaiga | — |
| `pakartotinis` | `string` | — | `4` | `open` | — | Požymis, ar tai pakartotinis patikrinimas | — |
| `statinio_paskirtis` | `string` | — | `4` | `open` | — | Statinio paskirtis(-ys), Kadangi statiniai gali turėti kelias paskirtis(teritorijoje daugiau nei viena statinys - paskirčių sąrašas) | — |
| `objekto_grupe` | `string` | — | `4` | `open` | — | Objekto grupė | — |
| `pgt_padalinys` | `string` | — | `4` | `open` | — | PGT padalinys | — |
| `uzbaigimo_akto_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Užbaigimo akto pasirašymo data (jei užpildyta, tiksli statinio užbaigimo data info statyboje) | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskritis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietė | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | x koordinatės LKS sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | y koordinatės LKS sistemoje | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Apjungtos koordinatės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv
