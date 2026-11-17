---
type: Table
title: "EzeruBukle — Aprašymas ežerų duomenų"
description: "Vandens telkinių ekologinės ir cheminės būklės vertinimas, 2022-2027 m. upių baseinų rajonų valdymo planų ciklui, atliktas vadovaujantis Lietuvos Respublikos vandens įstatymo nuostatomis, į kurias perkelti ir pagrindinio Europos..."
resource: "https://get.data.gov.lt/datasets/gov/aaa/ezeru_bukles_duomenys/EzeruBukle"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/ezeru_bukles_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezeru_bukles_duomenys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# EzeruBukle — Aprašymas ežerų duomenų

Vandens telkinių ekologinės ir cheminės būklės vertinimas, 2022-2027 m. upių baseinų rajonų valdymo planų ciklui, atliktas vadovaujantis Lietuvos Respublikos vandens įstatymo nuostatomis, į kurias perkelti ir pagrindinio Europos Sąjungos vandens teisinio dokumento – 2000 m. spalio 23 d. Europos Parlamento ir Tarybos direktyvos 2000/60/EB, nustatančios Bendrijos veiksmų vandens politikos srityje pagrindus (BVPD) reikalavimus.

- **Model:** `datasets/gov/aaa/ezeru_bukles_duomenys/EzeruBukle`[^manifest]
- **Dataset:** [datasets/gov/aaa/ezeru_bukles_duomenys](../ezeru_bukles_duomenys.md) (`datasets/gov/aaa/ezeru_bukles_duomenys`)
- **Manifest CSV:** [datasets/gov/aaa/ezeru_bukles_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezeru_bukles_duomenys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/ezeru_bukles_duomenys/EzeruBukle`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `telkinio_kodas` | `string` | — | `4` | `open` | — | Vandens telkinio kodas | Telkinio, išskirto pagal 2000 m. spalio 23 d. Europos Parlamento ir Tarybos direktyvos 2000/60/EB, nustatančios Bendrijos veiksmų vandens politikos srityje pagrindus (OL 2004 m. specialusis leidimas, 15 skyrius, 5 tomas, p. 275), principus, kodas |
| `telkinio_pav` | `string` | — | `4` | `open` | — | Vandens telkinio pavadinimas | Pagal Bendrąją vandens politikos direktyvą atskiri paviršiniai vandens telkiniai ežerai ir tvenkiniai, kurių plotas didesnis nei 0,5 kv. kilometrų. |
| `rajonas` | `string` | — | `4` | `open` | — | Upių baseinų rajonas | — |
| `rajono_kodas` | `string` | — | `4` | `open` | — | Upių baseinų rajono kodas | Įsakymu Nr. D1-752 patvirtintas UPIŲ BASEINŲ RAJONŲ KLASIFIKATORIUS https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.361485 |
| `baseinas` | `string` | — | `4` | `open` | — | Baseinas / pabaseinis | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskritis | — |
| `savivaldybes` | `string` | — | `4` | `open` | — | Savivaldybės | Savivaldybės, kurių teritorijoje yra vandens telkinys |
| `telkinio_pobudis` | `string` | — | `4` | `open` | — | Vandens telkinio pobūdis | — |
| `telkinio_tipas` | `string` | — | `4` | `open` | — | Vandens telkinio tipas | PAVIRŠINIŲ VANDENS TELKINIŲ APRAŠAS, 3. Ežerų tipai: https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.256896?jfwid=6ar7pe4vy |
| `m_vietos_kodas` | `string` | — | `4` | `open` | — | Monitoringo vietos kodas | Monitoringo vietų kodai, pagal kuriuos buvo atliktas vandens telkinio ekologinės ir cheminės būklės vertinimas |
| `m_vietos_pav` | `string` | — | `4` | `open` | — | Monitoringo vietos pavadinimas | Monitoringo vietų pavadinimai, pagal kuriuos buvo atliktas vandens telkinio ekologinės ir cheminės būklės vertinimas |
| `koord` | `geometry(point, 3346)` | — | `2` | `open` | — | Monitoringo vietų koordinatės LKS (m) | Monitoringo vietų, kuriose vykdomas valstybinis ežerų monitoringas koordinatės |
| `tarptaut_telkinys` | `string` | — | `4` | `open` | — | Tarptautinis vandens telkinys | — |
| `vertinimo_pagrindas` | `string` | — | `4` | `open` | — | Ekologinės būklės vertinimo pagrindas | — |
| `eko_bukle` | `string` | — | `4` | `open` | — | Ekologinė būklė | Lietuvos Respublikos aplinkos ministro 2007 m. balandžio 12 d. įsakymu Nr. D1-210 „Dėl Paviršinių vandens telkinių būklės nustatymo metodikos patvirtinimo“ |
| `eko_bukles_pasikliovimas` | `string` | — | `4` | `open` | — | Ekologinės būklės pasikliovimo lygis | — |
| `chem_bukle_pastabos` | `string` | — | `4` | `open` | — | Cheminė būklė | Lietuvos respublikos aplinkos ministro 2006 m. gegužės 17 d. įsakymas Nr. D1-236 „Dėl Nuotekų tvarkymo reglamento patvirtinimo“; Lietuvos Respublikos aplinkos ministro 2007 m. balandžio 12 d. įsakymas Nr. D1-210 „Dėl Paviršinių vandens telkinių būklės nustatymo metodikos patvirtinimo“ |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rajonas` | `"Nemuno"` | — | — | Nemuno upių baseinų rajonas | — |
| `rajonas` | `"Ventos"` | — | — | Ventos upių baseinų rajonas | — |
| `rajonas` | `"Lielupės"` | — | — | Lielupės upių baseinų rajonas | — |
| `rajonas` | `"Dauguvos"` | — | — | Dauguvos upių baseinų rajonas | — |
| `rajono_kodas` | `"LT1100"` | — | — | Nemuno upių baseinų rajonas | — |
| `rajono_kodas` | `"LT2300"` | — | — | Ventos upių baseinų rajonas | — |
| `rajono_kodas` | `"LT3400"` | — | — | Lielupės upių baseinų rajonas | — |
| `rajono_kodas` | `"LT4500"` | — | — | Dauguvos upių baseinų rajonas | — |
| `telkinio_pobudis` | `"Natūralus"` | — | — | Natūralus | — |
| `telkinio_pobudis` | `"Labai pakeistas"` | — | — | Labai pakeistas | — |
| `telkinio_pobudis` | `"Dirbtinis"` | — | — | Dirbtinis | — |
| `telkinio_tipas` | `"1"` | — | — | Vidutinis gylis ≤ 3 m arba Vidutinis gylis > 3, kai didžiausias gylis <11 m | Priskiriamas pagal Lietuvos Respublikos aplinkos ministro 2005 m. gegužės 23 d. Nr. D1-256 įsakymą "Dėl paviršinių vandens telkinių tipų aprašo ir paviršinių vandens tlekinių tipų etaloninių sąlygų aprašo patvirtinimo". 1 tipo žymėjimu atskiriami ir itin seklūs (pelkėjantys, vidutinis gylis ≤ 3 m) ežerai, tačiau jiems taikomi tokie patys kriterijai, kaip gilesniems (vidutinis gylis >3, kai didžiausias gylis <11 m) ežerams. |
| `telkinio_tipas` | `"2"` | — | — | Vidutinis gylis > 3 m ir didžiausias gylis 11-30 metrų | — |
| `telkinio_tipas` | `"3"` | — | — | Didžiausias gylis >30 m | — |
| `tarptaut_telkinys` | `"su Baltarusija"` | — | — | su Baltarusija | — |
| `tarptaut_telkinys` | `"su Latvija"` | — | — | su Latvija | — |
| `tarptaut_telkinys` | `"su Lenkija"` | — | — | su Lenkija | — |
| `tarptaut_telkinys` | `"su Rusija"` | — | — | su Rusija | — |
| `vertinimo_pagrindas` | `"monitoringas"` | — | — | Monitoringas | — |
| `vertinimo_pagrindas` | `"ekspertinis vertinimas"` | — | — | Ekspertinis vertinimas | — |
| `eko_bukle` | `"Labai gera"` | — | — | Labai gera ekologinė būklė | — |
| `eko_bukle` | `"Gera"` | — | — | Gera ekologinė būklė | — |
| `eko_bukle` | `"Vidutinė"` | — | — | Vidutinė ekologinė būklė | — |
| `eko_bukle` | `"Bloga"` | — | — | Bloga ekologinė būklė | — |
| `eko_bukle` | `"Labai bloga"` | — | — | Labai bloga ekologinė būklė | — |
| `eko_bukles_pasikliovimas` | `"Didelis"` | — | — | Didelis pasikliovimo lygis | — |
| `eko_bukles_pasikliovimas` | `"Vidutinis"` | — | — | Vidutinis pasikliovimo lygis | — |
| `eko_bukles_pasikliovimas` | `"Mažas"` | — | — | Mažas pasikliovimo lygis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `update(base: "/datasets/gov/rc/ar/apskritis/Apskritis", type: "ref", ref: "/datasets/gov/rc/ar/apskritis/Apskritis")` | `base` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/ezeru_bukles_duomenys.csv
