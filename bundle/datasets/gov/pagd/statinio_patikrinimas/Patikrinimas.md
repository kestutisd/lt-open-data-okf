---
type: Table
title: "Patikrinimas — Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai."
description: "\"Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas/Patikrinimas"
tags: [gov, pagd, patikrinimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2861/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/statinio_patikrinimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Patikrinimas — Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai.

"Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys. Rinkinį sudaro: pranešimo numeris ir data, patikrinimo pradžia ir pabaiga, statinio paskirtis, objekto grupė, apskritis, seniūnija, gyvenvietė bei koordinatės."[^manifest]

- **Model:** `datasets/gov/pagd/statinio_patikrinimas/Patikrinimas`[^manifest]
- **Dataset:** [Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai.](../statinio_patikrinimas.md) (`datasets/gov/pagd/statinio_patikrinimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas/Patikrinimas` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pranesimo_nr` | `string` | — | `4` | `open` | — | Pranešimo numeris | — |
| `pranesimo_data` | `date` | `D` | `4` | `open` | — | Pranešimo data | — |
| `patikrinimo_pradzia` | `date` | `D` | `4` | `open` | — | Patikrinimo pradžia | — |
| `patikrinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Patikrinimo pabaiga | — |
| `pakartotinis` | `string` | — | `4` | `open` | — | "Požymis, ar tai pakartotinis patikrinimas" | — |
| `statinio_paskirtis` | `string` | — | `4` | `open` | — | "Statinio paskirtis(-ys), Kadangi statiniai gali turėti kelias paskirtis(teritorijoje daugiau nei viena statinys - paskirčių sąrašas)" | — |
| `objekto_grupe` | `string` | — | `4` | `open` | — | Objekto grupė | — |
| `pgt_padalinys` | `string` | — | `4` | `open` | — | PGT padalinys | — |
| `uzbaigimo_akto_pasirasymo_data` | `date` | `D` | `4` | `open` | — | "Užbaigimo akto pasirašymo data (jei užpildyta, tiksli statinio užbaigimo data info statyboje)" | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskritis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietė | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | x koordinatės LKS sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | y koordinatės LKS sistemoje | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Apjungtos koordinatės | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/statinio_patikrinimas (https://data.gov.lt/datasets/2861/)
