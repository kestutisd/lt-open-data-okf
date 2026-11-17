---
type: Table
title: "Rusis — Saugojamos rūšys"
description: "Saugojamų augalų, gyvūnų, grybų rūšių duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/rusys/Rusis"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugojamos_rusys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugojamos_rusys.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rusis — Saugojamos rūšys

Saugojamų augalų, gyvūnų, grybų rūšių duomenys

- **Model:** `datasets/gov/vstt/rusys/Rusis`[^manifest]
- **Dataset:** [datasets/gov/vstt/rusys](../rusys.md) (`datasets/gov/vstt/rusys`)
- **Manifest CSV:** [datasets/gov/vstt/saugojamos_rusys.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugojamos_rusys.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/rusys/Rusis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašų identifikatorius | — |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `stebejimas` | `date` | `D` | `4` | `open` | — | Stebėjimo data | — |
| `sukurimas` | `date` | `D` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `komentaras` | `string` | — | `2` | `open` | — | Radavietės būsenos pastabos | — |
| `skaicius` | `integer` | `U` | `4` | `open` | — | Stebėtos rūšies individų skaičius | — |
| `tankumas_ha` | `number` | `U/ha` | `4` | `open` | — | Stebėtos rūšies individų tankumas | — |
| `tankumas_kv` | `number` | `U/m^2` | `4` | `open` | — | Stebėtos rūšies individų tankumas | — |
| `rusiu_stebejimas` | `string` | — | `2` | `open` | — | Rūšių Stebėjimas | Stebėtos rūšies individai: kita (tik augalams ir grybams) |
| `pastabos` | `string` | — | `2` | `open` | — | Stebėtojo pastabos | — |
| `anketos_busena` | `string` | — | `3` | `open` | — | Anketos būsena iš klasifikatorius | — |
| `anketos_statusas` | `string` | — | `4` | `open` | — | Anketos statusas | Anketos (stebėjimo) statusas iš klasifikatorius |
| `biotopas` | `string` | — | `3` | `open` | — | Biotopas | Stebėjimo biotopas (buveinė) ar kita informacija |
| `gyvunu_stebejimas` | `string` | — | `3` | `open` | — | Veiklos požymis | Gyvūno veiklos požymiai iš klasifikatoriaus |
| `evoliucija` | `string` | — | `3` | `open` | — | Vystymosi stadija | Gyvūno ar augalo vystymosi stadija iš klasifikatoriaus |
| `radavietes_busena` | `string` | — | `3` | `open` | — | Radavietės būsena | — |
| `rusis_lot` | `string` | — | `3` | `open` | — | Rūšies pavadinimas lotyniškai | — |
| `rusis_lt` | `string` | — | `3` | `open` | — | Rūšies pavadinimas lietuviškai | — |
| `klase` | `string` | — | `3` | `open` | — | Klasės | — |
| `tipas` | `string` | — | `3` | `open` | — | Tipas | — |
| `karalyste` | `string` | — | `3` | `open` | — | Karalystė | — |
| `cell_id` | `integer` | — | `4` | `open` | — | Gardelės identifikavimo numeris | — |
| `sluoksnis` | `string` | — | `4` | `open` | — | Sluoksnio geometrijos tipas | — |
| `geometrija` | `geometry(3346)` | `m` | `4` | `open` | — | Ploto geometrija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `anketos_statusas` | `"Aktuali"` | — | — | — | — |
| `anketos_statusas` | `"Archyvinė"` | — | — | — | — |
| `sluoksnis` | `"taskas"` | — | — | Taškas | Stebėjimo taškas. Žymimas kada stebimas objektas yra nedidelio ploto, kada fiziškai ploto neįmanoma įbraižyti, pvz. vienas augalas arba keras, vienas individas ar susitelkusi individų grupė. Paprastai tai objektai, kurie neviršija 5-10 m skersmens, |
| `sluoksnis` | `"poligonas"` | — | — | Poligonas | Stebėjimo plotas (plotas hektarais, kvadratiniais metrais ir kt.). Žymimas kada objektas tolygiai išsidėstęs erdvėje ir įmanoma įbraižyti jo plotą. Dažniausiai tai didesni nei 5-10 m skersmens plotai, kuriuose įvairiu tankumu pasiskirstę stebimi objektai, pvz. jei yra pieva su retu augalu, kurioje tas augalas randamas beveik visur, gana tolygiai pasiskirstęs. Tokiu atveju braižomas plotas visai pievai. |
| `sluoksnis` | `"linija"` | — | — | Linija | Stebėjimo linija (ilgis metrais). Žymima kada stebimas objektas yra nedidelio pločio, tačiau išsidriekęs erdvėje į ilgį, pvz. miško pakraštyje ar palei keliuką, išsidriekusi augalų eilė, kurios plotis neviršija 5-10 m, |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugojamos_rusys.csv
