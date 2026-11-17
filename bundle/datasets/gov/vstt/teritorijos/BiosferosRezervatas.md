---
type: Table
title: "BiosferosRezervatas — Biosferos rezervatai"
description: "Spinta table datasets/gov/vstt/teritorijos/BiosferosRezervatas (31 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/BiosferosRezervatas"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L114"
    last_modified: "2026-11-11T14:39:20Z"
---

# BiosferosRezervatas — Biosferos rezervatai

- **Model:** `datasets/gov/vstt/teritorijos/BiosferosRezervatas`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L114](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L114)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/BiosferosRezervatas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Biosferos rezervato pavadinimas | — |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `steigejas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas – institucija | — |
| `steigimas` | `date` | `D` | `4` | `open` | — | Steigimo data | — |
| `steig_ta` | `string` | — | `4` | `open` | — | Įsteigimo teisės aktas | — |
| `steig_tikslas` | `string` | — | `4` | `open` | — | Steigimo tikslas | Aprašomoji informacija |
| `bendr_reglam` | `integer` | — | `4` | `open` | — | Reglamentas | Bendrieji veiklos reglamentai nuoroda į teisės aktą |
| `spec_reglam` | `string` | — | `4` | `open` | — | įregistravimo į kadastrą data | Specialieji / individualieji veiklos reglamentai |
| `reg_data` | `date` | `D` | `4` | `open` | — | išregistravimo iš kadastro data | — |
| `isreg_data` | `date` | `D` | `4` | `open` | — | išregistravimo priežastis | — |
| `isreg_priez_lt` | `string` | — | `4` | `open` | — | išregistravimo teisės aktas | — |
| `isreg_ta` | `string` | — | `4` | `open` | — | išregistravimo teisės aktas | — |
| `saltiniai_lt` | `string` | — | `4` | `open` | — | Duomenų šaltiniai | Nurodomi moksliniai tyrimai ir publikacijos |
| `tarpt_svarba_status` | `integer` | — | `4` | `open` | — | Teritorijos statusas | Saugomai teritorijai arba jos daliai suteiktas tarptautinės svarbos (įskaitant Europos Bendrijų svarbos) teritorijos statusas |
| `tarpt_svarba_apras_lt` | `string` | — | `4` | `open` | — | Aprašas | Saugomai teritorijai arba jos daliai suteiktas tarptautinės svarbos (įskaitant Europos Bendrijų svarbos) teritorijos statuso aprašymas |
| `duomen_monitor_lt` | `string` | — | `4` | `open` | — | Monitoringas | Aplinkos stebėsenos (monitoringo) duomenys |
| `buf_zona_apras` | `string` | — | `4` | `open` | — | Buferinė zona | Duomenys apie valstybinio parko buferinę apsaugos zoną |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `reiksme` | `integer` | — | `4` | `open` | — | Objekto reikšmė | Gamtos paveldo objekto reikšmė: valstybės saugomi savivaldybės saugomi |
| `steigejas_galiojantis` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja saugomos teritorijos riba reglamentai arba šis teisės aktas yra šiuo metu galiojantis saugomos teritorijos teisinis pagrindas |
| `tvarkymo_zona` | `string` | — | `4` | `open` | — | Zona | Duomenys apie kraštovaizdžio tvarkymo zonas |
| `funkc_prior_zon` | `string` | — | `4` | `open` | — | Prioriteto zona | Duomenys apie biosferos rezervato funkcinio prioriteto zonas |
| `planavimo_dok` | `string` | — | `4` | `open` | — | Planavimo dokumentas | Duomenys apie parengtus planavimo dokumentus |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |
| `centras` | `geometry(point,3346)` | `m` | `4` | `open` | — | Centro koordinatė | Svorio centro koordinatės LKS’94 koordinačių sistemoje |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"nr0"` | — | — | Valstybinis rezervatas | — |
| `gkodas` | `"nr1"` | — | — | Rezervatinė apyrubė | — |
| `gkodas` | `"nd1"` | — | — | Valstybinis draustinis | — |
| `gkodas` | `"nd2"` | — | — | Savivaldybės draustinis | — |
| `gkodas` | `"nk1"` | — | — | Valstybės saugomas gamtos paveldo objektas | — |
| `gkodas` | `"nk2"` | — | — | Savivaldybės saugomas gamtos paveldo objektas | — |
| `gkodas` | `"nr4"` | — | — | Atkuriamasis sklypas | — |
| `gkodas` | `"nr5"` | — | — | Genetinis sklypas | — |
| `gkodas` | `"np1"` | — | — | Nacionalinis parkas | — |
| `gkodas` | `"np2"` | — | — | Regioninis parkas | — |
| `gkodas` | `"np4"` | — | — | Biosferos rezervatas | — |
| `gkodas` | `"np5"` | — | — | Biosferos poligonas | — |
| `gkodas` | `"nz4"` | — | — | Konservacinio funkcinio prioriteto zona - rezervatas | — |
| `gkodas` | `"nz5"` | — | — | Konservacinio funkcinio prioreteto zona - draustinis | — |
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
| `reiksme` | `1` | — | — | Valstybės saugomas | — |
| `reiksme` | `2` | — | — | Savivaldybės saugomas | — |
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
| `isreg_priez_lt` | `update("isreg_priez_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `saltiniai_lt` | `update("saltiniai_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `tarpt_svarba_apras_lt` | `update("tarpt_svarba_apras_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `duomen_monitor_lt` | `update("duomen_monitor_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `vieta_lt` | `update("vieta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv
