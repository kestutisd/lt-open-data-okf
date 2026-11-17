---
type: Table
title: "Irenginys — Nuotekų valymo įrenginiai bei jų lokacijos"
description: "Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Irenginys"
tags: [gov, aad, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Irenginys — Nuotekų valymo įrenginiai bei jų lokacijos

Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Šioje lentelėje pateikiami visi užregistruoti nuotekų įrenginiai. Registruojant nuotekų įrenginį (jei vartotojas nurodė), pateikiama tokia informacija kaip įrenginio tipas, gamintojas, modelis, koordinatės ir t.t. Įrenginių lentelėje viena eilutė atitinka vieną įrenginį. Duomenų aprėptis – visa Lietuva.

Duomenų teikėjas: Aplinkos apsaugos departamentas prie Aplinkos ministerijos

- **Model:** `datasets/gov/aad/nuoteku_irenginiai/Irenginys`[^manifest]
- **Dataset:** [Nuotekų valymo įrenginiai bei jų kokacijos](../nuoteku_irenginiai.md) (`datasets/gov/aad/nuoteku_irenginiai`)
- **Manifest CSV:** [datasets/gov/aad/nuoteku_irenginiai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Irenginys`
- **Primary Key (`ref`):** `irenginio_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio unikalus identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `busena` | `string` | — | `4` | `open` | — | Įrenginio būsena | — |
| `savivaldybes_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `gamintojas` | `string` | — | `4` | `open` | — | Nuotekų įrenginio gamintojas | — |
| `modelis` | `string` | — | `4` | `open` | — | Nuotekų įrenginio modelis | — |
| `talpa` | `string` | — | `4` | `open` | — | Nuotekų įrenginio talpa kubiniais metrais | — |
| `atstumas_nuo_kelio` | `number` | `m` | `4` | `open` | — | Atstumas nuo nuotekų įrenginio iki kelio | — |
| `pastatymo_data` | `date` | `D` | `4` | `open` | — | Pastatymo data | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Išregistravimo data | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `geometrija_wkt` | `geometry(point, 3346)` | — | `4` | `open` | — | Geometrija (lokacija) | — |
| `isleidimo_budas` | `string` | — | `4` | `open` | — | Nuotekų išleidimo būdas | — |
| `isleid_x_koord_lks` | `integer` | — | `4` | `open` | — | Nuotekų išleidimo vietos X koordinatė LKS-94 koordinačių sistemoje | — |
| `isleid_y_koord_lks` | `integer` | — | `4` | `open` | — | Nuotekų išleidimo vietos Y koordinatė LKS-94 koordinačių sistemoje | — |
| `isleid_geometrija_wkt` | `geometry(point, 3346)` | — | `4` | `open` | — | Nuotekų išleidimo geometrija (lokacija) | — |
| `aglomeracijos_id` | `string` | — | `4` | `open` | — | Aglomeracijos identifikatorius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Nuotekų rezervuaras"` | — | — | Nuotekų rezervuaras | — |
| `tipas` | `"Biologinis nuotekų valymo įrenginys"` | — | — | Biologinis nuotekų valymo įrenginys | — |
| `tipas` | `"Kilnojamas nuotekų rezervuaras"` | — | — | Kilnojamas nuotekų rezervuaras | — |
| `tipas` | `"Septikas"` | — | — | Septikas | — |
| `busena` | `"Preliminarus"` | — | — | Preliminarus | — |
| `busena` | `"Uždarytas"` | — | — | Uždarytas | — |
| `busena` | `"Patvirtintas"` | — | — | Patvirtintas | — |
| `isleidimo_budas` | `"Gruntas"` | — | — | Nuotekų išleidimas į gruntą | — |
| `isleidimo_budas` | `"Vandens telkinys"` | — | — | Nuotekų išleidimas į vandens telkinį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv
