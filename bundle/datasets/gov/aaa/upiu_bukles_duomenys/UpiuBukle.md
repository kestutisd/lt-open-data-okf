---
type: Table
title: "UpiuBukle — Aprašymas upių duomenų"
description: "Vandens telkinių ekologinės ir cheminės būklės vertinimas, 2022-2027 m. upių baseinų rajonų valdymo planų ciklui, atliktas vadovaujantis Lietuvos Respublikos vandens įstatymo nuostatomis, į kurias perkelti ir pagrindinio Europos Sąjungos vandens teisinio dokumento – 2000 m...."
resource: "https://get.data.gov.lt/datasets/gov/aaa/upiu_bukles_duomenys/UpiuBukle"
tags: [gov, aaa, upiubukle, deployed, level-4, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upiu_bukles_duomenys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/upiu_bukles_duomenys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/497/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/upiu_bukles_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# UpiuBukle — Aprašymas upių duomenų

Vandens telkinių ekologinės ir cheminės būklės vertinimas, 2022-2027 m. upių baseinų rajonų valdymo planų ciklui, atliktas vadovaujantis Lietuvos Respublikos vandens įstatymo nuostatomis, į kurias perkelti ir pagrindinio Europos Sąjungos vandens teisinio dokumento – 2000 m. spalio 23 d. Europos Parlamento ir Tarybos direktyvos 2000/60/EB, nustatančios Bendrijos veiksmų vandens politikos srityje pagrindus (BVPD) reikalavimus.[^manifest]

- **Model:** `datasets/gov/aaa/upiu_bukles_duomenys/UpiuBukle`[^manifest]
- **Dataset:** [Upių kategorijos vandens telkinių būklės duomenys](../upiu_bukles_duomenys.md) (`datasets/gov/aaa/upiu_bukles_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/upiu_bukles_duomenys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upiu_bukles_duomenys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/upiu_bukles_duomenys/UpiuBukle` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUINQUENNIAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `telkinio_kodas` | `string` | — | `4` | `open` | — | Vandens telkinio kodas | — |
| `telkinio_pav` | `string` | — | `4` | `open` | — | Vandens telkinio pavadinimas | Pagal Bendrąją vandens politikos direktyvą atskiri paviršiniai vandens telkiniai yra upės ar jų atkarpos, kurių baseino plotas didesnis nei 30 kv. kilometrų. |
| `basein_rajon` | `string` | — | `4` | `open` | — | Upių baseinų rajonas | Įsakymu Nr. D1-752 patvirtintas UPIŲ BASEINŲ RAJONŲ KLASIFIKATORIUS https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.361485 |
| `rajono_kodas` | `string` | — | `4` | `open` | — | Upių baseinų rajono kodas | Įsakymu Nr. D1-752 patvirtintas UPIŲ BASEINŲ RAJONŲ KLASIFIKATORIUS https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.361485 |
| `baseinas` | `string` | — | `4` | `open` | — | Baseinas / pabaseinis | — |
| `savivaldybes` | `string` | — | `4` | `open` | — | Savivaldybės | Savivaldybės, per kurių teritoriją teka vandens telkinys |
| `telkinio_pobudis` | `string` | — | `4` | `open` | — | Vandens telkinio pobūdis | — |
| `telkinio_tipas` | `string` | — | `4` | `open` | — | Vandens telkinio tipas | Priskiriamas pagal Lietuvos Respublikos aplinkos ministro 2005 m. gegužės 23 d. Nr. 256 įsakymą "Dėl paviršinių vandens telkinių tipų aprašo ir paviršinių vandens tlekinių tipų etaloninių sąlygų aprašo patvirtinimo" |
| `m_vietos_kodas` | `string` | — | `4` | `open` | — | Monitoringo vietos kodas | Monitoringo vietų kodai, pagal kuriuos buvo atliktas vandens telkinio ekologinės ir cheminės būklės vertinimas |
| `m_vietos_pav` | `string` | — | `4` | `open` | — | Monitoringo vietos pavadinimas | Monitoringo vietų pavadinimai, pagal kuriuos buvo atliktas vandens telkinio ekologinės ir cheminės būklės vertinimas |
| `koord` | `geometry(point, 3346)` | — | `4` | `open` | — | Monitoringo vietų koordinatės LKS (m) | Monitoringo vietų, kuriose vykdomas valstybinis ežerų monitoringas koordinatės |
| `tarptaut_telkinys` | `string` | — | `4` | `open` | — | Tarptautinis vandens telkinys | — |
| `vertinimo_pagrindas` | `string` | — | `4` | `open` | — | Ekologinės būklės vertinimo pagrindas | — |
| `eko_bukle` | `string` | — | `4` | `open` | — | Ekologinė būklė | Pagal Lietuvos Respublikos aplinkos ministro 2007 m. balandžio 12 d. įsakymą Nr. D1-210 „Dėl Paviršinių vandens telkinių būklės nustatymo metodikos patvirtinimo“. |
| `eko_bukles_pasikliovimas` | `string` | — | `4` | `open` | — | Ekologinės būklės pasikliovimo lygis | — |
| `chem_bukle` | `string` | — | `4` | `open` | — | Cheminė būklė | Lietuvos respublikos aplinkos ministro 2006 m. gegužės 17 d. įsakymas Nr. D1-236 "Dėl Nuotekų tvarkymo reglamento patvirtinimo", Lietuvos Respublikos aplinkos ministro 2007 m. balandžio 12 d. įsakymas Nr. D1-210 „Dėl Paviršinių vandens telkinių būklės nustatymo metodikos patvirtinimo“ |
| `chem_bukle_pastabos` | `string` | — | `4` | `open` | — | Cheminė būklė (vertinimo pagrindas, reikalavimų neatitinkantys rodikliai) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `basein_rajon` | `"Nemuno"` | — | — | Nemuno upių baseinų rajonas | — |
| `basein_rajon` | `"Ventos"` | — | — | Ventos upių baseinų rajonas | — |
| `basein_rajon` | `"Lielupės"` | — | — | Lielupės upių baseinų rajonas | — |
| `basein_rajon` | `"Dauguvos"` | — | — | Dauguvos upių baseinų rajonas | — |
| `rajono_kodas` | `"LT1100"` | — | — | Nemuno upių baseinų rajonas | — |
| `rajono_kodas` | `"LT2300"` | — | — | Ventos upių baseinų rajonas | — |
| `rajono_kodas` | `"LT3400"` | — | — | Lielupės upių baseinų rajonas | — |
| `rajono_kodas` | `"LT4500"` | — | — | Dauguvos upių baseinų rajonas | — |
| `telkinio_pobudis` | `"Natūralus"` | — | — | Natūralus | — |
| `telkinio_pobudis` | `"Labai pakeistas"` | — | — | Labai pakeistas | — |
| `telkinio_pobudis` | `"Dirbtinis"` | — | — | Dirbtinis | — |
| `telkinio_tipas` | `"1"` | — | — | Baseino plotas <100 km2 | Baseino plotas 100-1000 ir vidutinis vandens paviršiaus nuolydis >0,7 m/km |
| `telkinio_tipas` | `"2"` | — | — | Baseino plotas 100-1000 ir vidutinis vandens paviršiaus nuolydis <0,7 m/km | — |
| `telkinio_tipas` | `"3"` | — | — | Baseino plotas 100-1000 ir vidutinis vandens paviršiaus nuolydis >0,7 m/km | — |
| `telkinio_tipas` | `"4"` | — | — | Baseino plotas >1000 ir vidutinis vandens paviršiaus nuolydis <0,3 m/km | — |
| `telkinio_tipas` | `"5"` | — | — | Baseino plotas >1000 ir vidutinis vandens paviršiaus nuolydis >0,3 m/km | — |
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
| `chem_bukle` | `"Nežinoma"` | — | — | Nežinoma, ar pasiekta gera cheminė būklė | — |
| `chem_bukle` | `"Nepasiekta"` | — | — | Gera cheminė būklė nepasiekta | — |
| `chem_bukle` | `"Galimai nepasiekta"` | — | — | Gera cheminė būklė galimai nepasiekta | — |
| `chem_bukle` | `"Pasiekta"` | — | — | Gera cheminė būklė pasiekta | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/upiu_bukles_duomenys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/upiu_bukles_duomenys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/upiu_bukles_duomenys (https://data.gov.lt/datasets/497/)
