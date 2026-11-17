---
type: Table
title: "JaunasisUkininkasInfo — Lietuvos kaimo plėtros programos 2014 - 2020 metų priemonė \"Parama jaunųjų ūkininkų įsikūrimui (19JU) (papildomas finansavimas, LT100)\""
description: "Spinta table datasets/gov/nma/jaunieji_ukininkai_info/JaunasisUkininkasInfo (20 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/jaunieji_ukininkai_info/JaunasisUkininkasInfo"
tags: [gov, nma, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/jaunieji_ukininkai_info.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/jaunieji_ukininkai_info.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# JaunasisUkininkasInfo — Lietuvos kaimo plėtros programos 2014 - 2020 metų priemonė "Parama jaunųjų ūkininkų įsikūrimui (19JU) (papildomas finansavimas, LT100)"

- **Model:** `datasets/gov/nma/jaunieji_ukininkai_info/JaunasisUkininkasInfo`[^manifest]
- **Dataset:** [datasets/gov/nma/jaunieji_ukininkai_info](../jaunieji_ukininkai_info.md) (`datasets/gov/nma/jaunieji_ukininkai_info`)
- **Manifest CSV:** [datasets/gov/nma/jaunieji_ukininkai_info.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/jaunieji_ukininkai_info.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/jaunieji_ukininkai_info/JaunasisUkininkasInfo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priemone` | `string` | — | `4` | `open` | — | Priemonių grupės pavadinimas | — |
| `veiklos_sritis` | `string` | — | `4` | `open` | — | Administravimo proceso pavadinimas | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_gavimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos gavimo data | — |
| `projekto_igyvendinimo_vieta` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo vieta (savialdybė) | — |
| `prasoma_paramos_suma` | `number` | — | `2` | `open` | — | Prašoma paramos suma | — |
| `bylos_etapas` | `string` | — | `4` | `open` | — | Bylos etapas | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Paramos sutarties pasirašymo data | — |
| `skirta_paramos_suma` | `number` | — | `2` | `open` | — | Paramos suma | — |
| `es_paramos_dalis` | `number` | — | `2` | `open` | — | ES dalis suma | — |
| `lt_paramos_dalis` | `number` | — | `2` | `open` | — | LT dalis suma | — |
| `ismoketa_paramos_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma | — |
| `sankciju_suma` | `number` | — | `2` | `open` | — | Bendra (viso projekto lygmeniu) pritaikytų sankcijų suma | — |
| `projekto_pradzia` | `date` | `D` | `4` | `open` | — | Projekto plan. pradžia | — |
| `projekto_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto plan. pabaiga | — |
| `projekto_isip_pabaigos_data` | `date` | `D` | `4` | `open` | — | Projekto įsipareigojimų pabaigos data | — |
| `paraiskos_nutr_data` | `date` | `D` | `4` | `open` | — | Paraiškos nutraukimo data | — |
| `kvietimo_pradzia` | `date` | `D` | `4` | `open` | — | Kvietimo pradžios data nuo | — |
| `kvietimo_pabaiga` | `date` | `D` | `4` | `open` | — | Kvietimo pabaigos data iki | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | — | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | — | — |
| `pareiskejo_lytis` | `"V"` | — | — | — | — |
| `pareiskejo_lytis` | `"M"` | — | — | — | — |
| `bylos_etapas` | `"Išregistravimas"` | — | — | Išregistravimas | — |
| `bylos_etapas` | `"Paramos administravimas"` | — | — | Paramos administravimas | — |
| `bylos_etapas` | `"Atmetimas"` | — | — | Atmetimas | — |
| `bylos_etapas` | `"Vertinimas"` | — | — | Vertinimas | — |
| `bylos_etapas` | `"Sutarties rengimas"` | — | — | Sutarties rengimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_igyvendinimo_vieta` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `prasoma_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `skirta_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `es_paramos_dalis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `lt_paramos_dalis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ismoketa_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sankciju_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/jaunieji_ukininkai_info.csv
