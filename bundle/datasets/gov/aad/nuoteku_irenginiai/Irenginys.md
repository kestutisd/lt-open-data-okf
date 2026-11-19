---
type: Table
title: "Irenginys — Nuotekų valymo įrenginiai bei jų lokacijos"
description: "Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Irenginys"
tags: [gov, aad, irenginys, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2855/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aad/nuoteku_irenginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Irenginys — Nuotekų valymo įrenginiai bei jų lokacijos

Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Šioje lentelėje pateikiami visi užregistruoti nuotekų įrenginiai. Registruojant nuotekų įrenginį (jei vartotojas nurodė), pateikiama tokia informacija kaip įrenginio tipas, gamintojas, modelis, koordinatės ir t.t. Įrenginių lentelėje viena eilutė atitinka vieną įrenginį. Duomenų aprėptis – visa Lietuva. Duomenų teikėjas: Aplinkos apsaugos departamentas prie Aplinkos ministerijos Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/aad/nuoteku_irenginiai/Irenginys`[^manifest]
- **Dataset:** [Nuotekų valymo įrenginiai bei jų kokacijos](../nuoteku_irenginiai.md) (`datasets/gov/aad/nuoteku_irenginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aad/nuoteku_irenginiai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Irenginys` (`deployed`)[^manifest]
- **Provider:** `aad` — Aplinkos apsaugos departamentas prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `irenginio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aad/nuoteku_irenginiai (https://data.gov.lt/datasets/2855/)
