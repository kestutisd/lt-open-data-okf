---
type: Table
title: "Licencija — Išduotų, sustabdytų, panaikintų licencijų sąrašas"
description: "Įstaigų teikiančių socialinės globos paslaugas licencijuojamos veiklos vykdymo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/sppd/licencijos/Licencija"
tags: [gov, sppd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sppd/soc_globos_licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Licencija — Išduotų, sustabdytų, panaikintų licencijų sąrašas

Įstaigų teikiančių socialinės globos paslaugas licencijuojamos veiklos vykdymo duomenys. Licencijos išduotos nuo 2013 metų iki dabar. Rinkinyje pateikiama įstaigos kodas, pavadinimas, savivaldybė, adresas su koordinatėmis, tipas, licencijos numeris,tipas, statusas, registracijos, sustabdymo,panaikinimo, tikslinimo datos.

- **Model:** `datasets/gov/sppd/licencijos/Licencija`[^manifest]
- **Dataset:** [Išduotų, sustabdytų, panaikintų licencijų sąrašas](../licencijos.md) (`datasets/gov/sppd/licencijos`)
- **Manifest CSV:** [datasets/gov/sppd/soc_globos_licencijos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/licencijos/Licencija`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `licencijos_numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `istaigos_jar` | `string` | — | `4` | `open` | — | Įstaigos JAR kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `istaigos_adresas` | `string` | — | `4` | `open` | — | Įstaigos adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS sistemoje | — |
| `veiklos_rusis` | `string` | — | `4` | `open` | — | Veiklos rūšis | — |
| `licencijos_busena` | `string` | — | `4` | `open` | — | Licencijos būsena: active - aktyvi, removed - panaikinta, restricted - apribota, stopped - sustabdyta, stopped_continued - sustabdyta su pratęsimu, remove - naikinama, warned - įspėtas, warned_continued -įspėtas su pratęsimu | — |
| `licencijos_tipas` | `string` | — | `4` | `open` | — | Licencijos tipas | — |
| `licencijos_isdavimo_data` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `licencijos_tikslinimo_data` | `date` | `D` | `4` | `open` | — | Licencijos tikslinimo data | — |
| `licencijos_sustabdymo_data` | `date` | `D` | `4` | `open` | — | Licencijos sustabdymo data | — |
| `licencijos_sustabdyta_iki` | `date` | `D` | `4` | `open` | — | Licencija sustabdyta iki | — |
| `licencijos_panaikinimo_data` | `date` | `D` | `4` | `open` | — | Licencijos panaikinimo data | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Apjungtos koordinatės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/soc_globos_licencijos.csv
