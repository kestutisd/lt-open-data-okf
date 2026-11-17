---
type: Table
title: "BuferineApsaugosZona — Buferinės apsaugos zonos"
description: "Spinta table datasets/gov/vstt/teritorijos/BuferineApsaugosZona (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/BuferineApsaugosZona"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L456"
    last_modified: "2026-11-11T14:39:20Z"
---

# BuferineApsaugosZona — Buferinės apsaugos zonos

- **Model:** `datasets/gov/vstt/teritorijos/BuferineApsaugosZona`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L456](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L456)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/BuferineApsaugosZona`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `st_gkodas` | `string` | — | `4` | `open` | — | Teritorijos kodas | Saugomos teritorijos kuriai priklauso buferinės apsaugos zona tipas – geokodas (visų saugomų teritorijos tipų pagal InGIS standartą klasifikatorius) |
| `st_id` | `string` | — | `4` | `open` | — | Identifikatorius | Jei gamtos paveldo objektas yra saugomoje teritorijoje pildomas saugomos teritorijos kurioje yra gamtos paveldo objektas identifikatorius |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `teisinis_pagrindas` | `string` | — | `4` | `open` | — | Teises aktas | Buferinės apsaugos zonos parengimo teisinis pagrindas |
| `parengimas` | `date` | `D` | `4` | `open` | — | Buferinės apsaugos zonos parengimo data | — |
| `pozymis` | `integer` | — | `4` | `open` | — | Apsaugos zonos pozoniai | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `steigejas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas – institucija | — |
| `steigimas` | `date` | `D` | `4` | `open` | — | Steigimo data | — |
| `steig_ta` | `string` | — | `4` | `open` | — | Įsteigimo teisės aktas | — |
| `steigejas_galiojantis` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja saugomos teritorijos riba reglamentai arba šis teisės aktas yra šiuo metu galiojantis saugomos teritorijos teisinis pagrindas |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `steig_tikslas` | `string` | — | `4` | `open` | — | Steigimo tikslas | Aprašomoji informacija |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

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
| `st_gkodas` | `"nr0"` | — | — | Valstybinis rezervatas | — |
| `st_gkodas` | `"nd1"` | — | — | Valstybinis draustinis | — |
| `st_gkodas` | `"nd2"` | — | — | Savivaldybės draustinis | — |
| `st_gkodas` | `"nk1"` | — | — | Valstybės saugomi gamtos paveldo objektas | — |
| `st_gkodas` | `"nk2"` | — | — | Savivaldybės saugomi gamtos paveldo objektas | — |
| `st_gkodas` | `"np1"` | — | — | Nacionalinis parkas | — |
| `st_gkodas` | `"np2"` | — | — | Regioninis parkas | — |
| `pozymis` | `0` | — | — | Neturi požymio | — |
| `pozymis` | `1` | — | — | Fizinės apsaugos pozonis | — |
| `pozymis` | `2` | — | — | Vizualinės apsaugos pozonis | — |
| `pozymis` | `3` | — | — | Bendrosios ekologinės apsaugos pazonis | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv
