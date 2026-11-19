---
type: Table
title: "Leidimas — Paraiškos ir leidimai atlikti kasinėjimo, aptvėrimo ir kitus infrastruktūros darbus Vilniaus miesto savivaldybėje"
description: "Spinta table datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas"
tags: [gov, vilniaus_m_sav, leidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3994/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/leidimai_darbams"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Leidimas — Paraiškos ir leidimai atlikti kasinėjimo, aptvėrimo ir kitus infrastruktūros darbus Vilniaus miesto savivaldybėje

- **Model:** `datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas`[^manifest]
- **Dataset:** [Paraiškos ir leidimai atlikti kasinėjimo, aptvėrimo ir kitus infrastruktūros darbus Vilniaus...](../leidimai_darbams.md) (`datasets/gov/vilniaus_m_sav/leidimai_darbams`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/leidimai_darbams/Leidimas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `leidimo_tipas` | `"Aptv_rimams ir Kasinėjimams"` | — | — | Aptvėrimams ir Kasinėjimams | — |
| `leidimo_tipas` | `"Kasinėjimams"` | — | — | Kasinėjimams | — |
| `leidimo_tipas` | `"Aptvėrimams"` | — | — | Aptvėrimams | — |
| `leidimo_tipas` | `"Kita"` | — | — | Kita | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/leidimai_darbams.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/leidimai_darbams (https://data.gov.lt/datasets/3994/)
