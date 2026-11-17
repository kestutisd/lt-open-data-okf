---
type: Table
title: "Leidimas — Prienų raj. sav. Išorinės reklamos, prekybos ir paslaugų teikimo viešosiose vietose leidimų išdavimo duomenys"
description: "Prienų raj."
resource: "https://get.data.gov.lt/datasets/gov/prienu_r_sav/prienu_leidimai/Leidimas"
tags: [gov, prienu_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/prienu_r_sav/prienu_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/prienu_r_sav/prienu_leidimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Prienų raj. sav. Išorinės reklamos, prekybos ir paslaugų teikimo viešosiose vietose leidimų išdavimo duomenys

Prienų raj. sav. Išorinės reklamos, prekybos ir paslaugų teikimo viešosiose vietose leidimų išdavimo sistemos duomenų rinkinį sudaro 1 lentelė – Prienų raj. savivaldybės nuo 2025 m. kovo mėn. pabaigos renkami prekybai, reklamai arba paslaugų teikimui pateiktų paraiškų duomenys ir būsenos. Vienas įrašas lentelėje atitinka vieną juridinio ar fizinio asmens paraišką prekiauti ar teikti paslaugas Prienų raj. savivaldybės teritorijoje. Duomenų teikėjas – Prienų rajono savivaldybė.

- **Model:** `datasets/gov/prienu_r_sav/prienu_leidimai/Leidimas`[^manifest]
- **Dataset:** [Išorinės reklamos, prekybos ir paslaugų teikimo viešosiose vietose leidimų išdavimo sistema](../prienu_leidimai.md) (`datasets/gov/prienu_r_sav/prienu_leidimai`)
- **Manifest CSV:** [datasets/gov/prienu_r_sav/prienu_leidimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/prienu_r_sav/prienu_leidimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/prienu_r_sav/prienu_leidimai/Leidimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Pirminis raktas | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilguma (papildomas VDA stulpelis) | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas vietos, kuriai taikomas leidimas | — |
| `renginio_tipas` | `string` | — | `4` | `open` | — | Požymis, nurodantis, ar renginys, ar mugė | — |
| `seniunijos_el_pastas` | `string` | — | `4` | `open` | — | Seniūnijos el. paštas | — |
| `pardavimo_pavadinimas` | `string` | — | `4` | `open` | — | Pardavimo vietos pavadinimas | — |
| `kasimo_darbu_tipas` | `string` | — | `4` | `open` | — | Kasimo darbų tipas | — |
| `renginys` | `string` | — | `4` | `open` | — | Renginio pavadinimas | — |
| `renginio_pradzia` | `date` | `D` | `4` | `open` | — | Renginio pradžios data | — |
| `paraiskos_pateikimo_data` | `datetime` | `L` | `4` | `open` | — | Paraiškos sukūrimo data | — |
| `reikalingu_vietu_sk` | `integer` | — | `4` | `open` | — | Vietų skaičius | — |
| `renginio_pabaiga` | `date` | `D` | `4` | `open` | — | Data iki | — |
| `renginio_aprasymas` | `string` | — | `4` | `open` | — | Aprašymas | — |
| `kaina` | `number` | — | `4` | `open` | — | Kaina | — |
| `pardavimo_erdves_vietu_sk` | `integer` | — | `4` | `open` | — | Maksimalios vietos | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platuma (papildomas VDA stulpelis) | — |
| `paraiskos_busena` | `string` | — | `4` | `open` | — | Būsenos pavadinimas | — |
| `turinys` | `string` | — | `4` | `open` | — | Rūšis | — |
| `pardavimo_tipo_trumpinys` | `string` | — | `4` | `open` | — | Renginio pavadinimas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `pardavimo_vieta` | `string` | — | `4` | `open` | — | Pardavimo vieta | — |
| `pardavimo_vietos_aprasymas` | `string` | — | `4` | `open` | — | Pardavimo vietos aprašymas | — |
| `leidimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaigos data | — |
| `leidimo_pradzios_data` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžios data | — |
| `pardavimo_tipas` | `string` | — | `4` | `open` | — | Pardavimo tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/prienu_r_sav/prienu_leidimai.csv
