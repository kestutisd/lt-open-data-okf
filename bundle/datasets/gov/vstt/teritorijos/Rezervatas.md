---
type: Table
title: "Rezervatas — Rezervatai"
description: "Spinta table datasets/gov/vstt/teritorijos/Rezervatas (30 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/Rezervatas"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1265"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rezervatas — Rezervatai

- **Model:** `datasets/gov/vstt/teritorijos/Rezervatas`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L1265](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1265)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/Rezervatas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Rezervato pavadinimas | — |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `rezervat_pobud` | `integer` | — | `4` | `open` | — | Rezervato pobūdis | — |
| `reiksme` | `integer` | — | `4` | `open` | — | Objekto reikšmė | Gamtos paveldo objekto reikšmė: valstybės saugomi savivaldybės saugomi |
| `centras` | `geometry(point,4326)` | `m` | `4` | `open` | — | Centro koordinatė | Svorio centro koordinatės LKS’94 koordinačių sistemoje |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `steigejas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas – institucija | — |
| `steigimas` | `date` | `D` | `4` | `open` | — | Steigimo data | — |
| `steig_ta` | `string` | — | `4` | `open` | — | Įsteigimo teisės aktas | — |
| `steig_tikslas` | `string` | — | `4` | `open` | — | Steigimo tikslas | Aprašomoji informacija |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `bendr_reglam` | `integer` | — | `4` | `open` | — | Reglamentas | Bendrieji veiklos reglamentai nuoroda į teisės aktą |
| `spec_reglam` | `string` | — | `4` | `open` | — | Reglamentai | Specialieji / individualieji veiklos reglamentai |
| `saltiniai_lt` | `string` | — | `4` | `open` | — | Duomenų šaltiniai | Nurodomi moksliniai tyrimai ir publikacijos |
| `tarpt_svarba_status` | `integer` | — | `4` | `open` | — | Teritorijos statusas | Saugomai teritorijai arba jos daliai suteiktas tarptautinės svarbos (įskaitant Europos Bendrijų svarbos) teritorijos statusas |
| `tarpt_svarba_apras_lt` | `string` | — | `4` | `open` | — | Aprašas | Saugomai teritorijai arba jos daliai suteiktas tarptautinės svarbos (įskaitant Europos Bendrijų svarbos) teritorijos statuso aprašymas |
| `gamtiniai_kompleksai` | `integer` | — | `4` | `open` | — | Gamtiniai kompleksai | Duomenys apie saugomus gamtinius kompleksus ir jų būklę |
| `duomen_monitor_lt` | `string` | — | `4` | `open` | — | Monitoringas | Aplinkos stebėsenos (monitoringo) duomenys |
| `buf_zona_apras` | `string` | — | `4` | `open` | — | Buferinė zona | Duomenys apie valstybinio parko buferinę apsaugos zoną |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `steigejas_galiojantis` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja saugomos teritorijos riba reglamentai arba šis teisės aktas yra šiuo metu galiojantis saugomos teritorijos teisinis pagrindas |
| `st_id` | `string` | — | `4` | `open` | — | Identifikatorius | Jei gamtos paveldo objektas yra saugomoje teritorijoje pildomas saugomos teritorijos kurioje yra gamtos paveldo objektas identifikatorius |
| `tvarkymo_zona` | `string` | — | `4` | `open` | — | Zona | Duomenys apie kraštovaizdžio tvarkymo zonas |
| `planavimo_dok` | `string` | — | `4` | `open` | — | Planavimo dokumentas | Duomenys apie parengtus planavimo dokumentus |
| `ta_nust_st_dalis` | `string` | — | `4` | `open` | — | Teises aktas | Teisės aktas nustatęs kad rezervatas tapo kompleksinės saugomos teritorijos dalimi |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"nr0"` | — | — | Valstybinis | — |
| `gkodas` | `"nr1"` | — | — | Rezervatinė apyrubė | — |
| `gkodas` | `"nz4"` | — | — | Konservacinio funkcinio prioriteto zona | — |
| `rezervat_pobud` | `1` | — | — | Gamtinis | — |
| `rezervat_pobud` | `2` | — | — | Kultūrinis | — |
| `reiksme` | `1` | — | — | Valstybinis | — |
| `reiksme` | `3` | — | — | Konservacinio prioriteto funkcinė zona – rezervatas | — |
| `bendr_reglam` | `1` | — | — | Rezervatai | — |
| `bendr_reglam` | `2` | — | — | Draustiniai | — |
| `bendr_reglam` | `3` | — | — | Parkai | — |
| `bendr_reglam` | `4` | — | — | Sklypai | — |
| `bendr_reglam` | `5` | — | — | Biosferos Poligonai, Biosferos Rezervatai | — |
| `bendr_reglam` | `6` | — | — | Gamtos paveldo objektai | — |
| `tarpt_svarba_status` | `0` | — | — | Nėra duomenų | — |
| `tarpt_svarba_status` | `1` | — | — | Unesco | — |
| `tarpt_svarba_status` | `2` | — | — | Ramsar | — |
| `tarpt_svarba_status` | `3` | — | — | Buveinių apsaugos | — |
| `tarpt_svarba_status` | `4` | — | — | Paukščių apsaugos | — |
| `tarpt_svarba_status` | `5` | — | — | Helcom | — |
| `tarpt_svarba_status` | `6` | — | — | Paukščių ir buveinių apsaugos | — |
| `gamtiniai_kompleksai` | `0` | — | — | Nėra duomenų | — |
| `gamtiniai_kompleksai` | `1` | — | — | Gera | — |
| `gamtiniai_kompleksai` | `2` | — | — | Patenkinama | — |
| `gamtiniai_kompleksai` | `3` | — | — | Bloga | — |
| `id_vart` | `101` | — | — | Aukštaitijos NP ir Labanoro RP direkcija | — |
| `id_vart` | `102` | — | — | Aukštaitijos saugomų teritorijų direkcija | — |
| `id_vart` | `103` | — | — | Dzūkijos – Suvalkijos saugomų teritorijų direkcija | — |
| `id_vart` | `104` | — | — | Dzūkijos NP ir Čepkelių VGR direkcija | — |
| `id_vart` | `105` | — | — | Kernavės VKRz direkcija | — |
| `id_vart` | `106` | — | — | Kuršių nerijos NP direkcija | — |
| `id_vart` | `107` | — | — | Mažosios Lietuvos saugomų teritorijų direkcija | — |
| `id_vart` | `108` | — | — | Trakų INP direkcija | — |
| `id_vart` | `109` | — | — | Pavinių ir Verkių RP direkcija | — |
| `id_vart` | `110` | — | — | Žemaitijos NP direkcija | — |
| `id_vart` | `111` | — | — | Žemaitijos saugomų teritorijų direkcija | — |
| `id_vart` | `112` | — | — | Vilniaus pilių VKRz direkcija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vieta_lt` | `update("vieta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `saltiniai_lt` | `update("saltiniai_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `tarpt_svarba_apras_lt` | `update("tarpt_svarba_apras_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `duomen_monitor_lt` | `update("duomen_monitor_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv
