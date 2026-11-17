---
type: Table
title: "Leidimas — Paraiškos ir leidimai atlikti kasinėjimo, aptvėrimo ir kitus infrastruktūros darbus Vilniaus miesto savivaldybėje"
description: "Spinta table datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/leidimai_darbams.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Paraiškos ir leidimai atlikti kasinėjimo, aptvėrimo ir kitus infrastruktūros darbus Vilniaus miesto savivaldybėje

- **Model:** `datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas`[^manifest]
- **Dataset:** [Paraiškos ir leidimai atlikti kasinėjimo, aptvėrimo ir kitus infrastruktūros darbus Vilniaus miesto savivaldybėje](../leidimai_darbams.md) (`datasets/gov/vilniaus_m_sav/leidimai_darbams`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus lentelės raktas | — |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento identifikatorius | — |
| `dig_permission_id` | `string` | — | `4` | `open` | — | Leidimo identifikatorius | — |
| `dokumento_tipas` | `string` | — | `4` | `open` | — | Dokumento tipas | — |
| `issiusta` | `boolean` | — | `4` | `open` | — | Požymis ar leidimas buvo išsiųstas į Avilio sistemą registracijai | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `darbas` | `string` | — | `4` | `open` | — | Atlikas/planuojamas darbas | — |
| `darbo_atlik_pradz_data` | `date` | `D` | `4` | `open` | — | Darbo atlikimo pradžios data | — |
| `darbo_atlik_pabaig_data` | `date` | `D` | `4` | `open` | — | Darbo atlikimo pabaigos data | — |
| `darbo_vietos_adresas` | `string` | — | `4` | `open` | — | Darbo vietos adresas | — |
| `darbo_vietos_rajonas` | `string` | — | `4` | `open` | — | Rajonas, kuriame atliktas/bus atliekamas darbas | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | Darbo vietos koordinatės ilguma | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Darbo vietos koordinatės platuma | — |
| `geometrija_lks` | `geometry(point, 3346)` | — | `4` | `open` | — | Darbo vietos koordinatė | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Darbo vietos koordinatės ilguma | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Darbo vietos koordinatės platuma | — |
| `geometrija_wgs` | `geometry(point, 4326)` | — | `4` | `open` | — | Darbo vietos koordinatė | — |
| `kaina_be_tarif` | `number` | — | `4` | `open` | — | Bendra kaina už darbus be tarifo | — |
| `kaina_su_tarif` | `number` | — | `4` | `open` | — | Bendra kaina už darbus su tarifu | — |
| `tarifas` | `number` | — | `4` | `open` | — | Taikomas tarifas | — |
| `pareiskejas` | `string` | — | `4` | `open` | — | Prašymą gauti leidimą atlikti darbą pateikęs fizinis/juridinis asmuo | — |
| `uzsakovas` | `string` | — | `4` | `open` | — | Darbo užsakovas | — |
| `rangovas` | `string` | — | `4` | `open` | — | Darbo rangovas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `leidimo_tipas` | `"Aptv_rimams ir Kasinėjimams"` | — | — | Aptvėrimams ir Kasinėjimams | — |
| `leidimo_tipas` | `"Kasinėjimams"` | — | — | Kasinėjimams | — |
| `leidimo_tipas` | `"Aptvėrimams"` | — | — | Aptvėrimams | — |
| `leidimo_tipas` | `"Kita"` | — | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/leidimai_darbams.csv
