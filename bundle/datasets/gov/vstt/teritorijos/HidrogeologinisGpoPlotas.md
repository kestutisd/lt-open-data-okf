---
type: Table
title: "HidrogeologinisGpoPlotas — Hidrogeologiniai GPO Plotai"
description: "Spinta table datasets/gov/vstt/teritorijos/HidrogeologinisGpoPlotas (54 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/HidrogeologinisGpoPlotas"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L967"
    last_modified: "2026-11-11T14:39:20Z"
---

# HidrogeologinisGpoPlotas — Hidrogeologiniai GPO Plotai

- **Model:** `datasets/gov/vstt/teritorijos/HidrogeologinisGpoPlotas`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L967](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L967)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/HidrogeologinisGpoPlotas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Gamtos paveldo objekto pavadinimas | — |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `reiksme` | `integer` | — | `4` | `open` | — | Objekto reikšmė | Gamtos paveldo objekto reikšmė: valstybės saugomi savivaldybės saugomi |
| `objektu_rusys` | `integer` | — | `4` | `open` | — | Hidrogeologinių objektų rūšys | — |
| `kult_paveld_kodas` | `integer` | — | `2` | `open` | — | Kodas | Jeigu gamtos paveldo objektas kartu turi ir kultūros paveldo objekto statusą nurodomas šio objekto kodas iš Nekilnojamųjų kultūros vertybių registro |
| `st_id` | `string` | — | `4` | `open` | — | Identifikatorius | Jei gamtos paveldo objektas yra saugomoje teritorijoje pildomas saugomos teritorijos kurioje yra gamtos paveldo objektas identifikatorius |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `skelbejas_lt` | `string` | — | `4` | `open` | — | Paskelbusi institucija | Objektą saugomu paskelbė (paskelbusi – institucija) |
| `skelbiama` | `date` | `D` | `4` | `open` | — | Skelbimo data | Objekto paskelbimo saugomu data (metai mėnuo diena) |
| `skelb_ta` | `string` | — | `4` | `open` | — | Teisės aktas | Objekto paskelbimo saugomu teisinis pagrindas |
| `skelb_tikslas` | `string` | — | `4` | `open` | — | Objekto skelbimo saugomu tikslas | Aprašomoji informacija |
| `orograf_padetis` | `string` | — | `4` | `open` | — | Orografinė padėtis | — |
| `uolienos` | `string` | — | `4` | `open` | — | Uolienos iš kurių išteka šaltiniai ir versmės | — |
| `fiz_savyb` | `string` | — | `4` | `open` | — | Vandens fizinės sąvybės | — |
| `chem_savyb_lt` | `string` | — | `4` | `open` | — | Vandens cheminės sąvybės | — |
| `debitas` | `number` | `m^3/s` | `4` | `open` | — | Debitas | — |
| `dujos` | `string` | — | `4` | `open` | — | Dujų išsiskyrimo reiškiniai | — |
| `rezimas` | `string` | — | `4` | `open` | — | Nuosėdos rėžimas | — |
| `kiti_param_lt` | `string` | — | `4` | `open` | — | Kiti parametrai | — |
| `adm_hier_kodas` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[sav_kodas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės kodas | — |
| `adm_pavadinimas_lt` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `adm_hier_kodas_sen` | `ref` | [/datasets/gov/rc/ar/seniunija/Seniunija[sen_kodas]](../../rc/ar/seniunija/Seniunija.md) | `4` | `open` | — | Seniūnijos kodas | — |
| `adm_pavadinimas_sen_lt` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gyv_rej_kodas` | `ref` | [/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove[gyv_kodas]](../../rc/ar/gyvenamojivietove/GyvenamojiVietove.md) | `4` | `open` | — | Gyvenamosios vietovės rejestro kodas | — |
| `gyv_pavad_v_lt` | `string` | — | `4` | `open` | — | Gyvenamosios vietovės pavadinimas | — |
| `gat_kodas` | `ref` | [/datasets/gov/rc/ar/gatve/Gatve[gat_kodas]](../../rc/ar/gatve/Gatve.md) | `4` | `open` | — | Gatvės kodas | — |
| `gat_pavadinimas_lt` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `mu_kod` | `integer` | — | `2` | `open` | — | Miškų urėdijos kodas | — |
| `mu_pavad_lt` | `string` | — | `4` | `open` | — | Miškų urėdijos pavadinimas | — |
| `gir_kod` | `integer` | — | `2` | `open` | — | Miškų girininkijos kodas | — |
| `gir_pavad_lt` | `string` | — | `4` | `open` | — | Miškų girininkijos pavadinimas | — |
| `kv_nr` | `integer` | — | `2` | `open` | — | Miškų kvartalo numeris | — |
| `skl_nr` | `integer` | — | `2` | `open` | — | Miškų sklypo numeris | — |
| `skl_geo` | `string` | — | `2` | `open` | — | Kodas | Unikalus miško sklypo geokodas susidedantis iš urėdijos girininkijos kvartalo sklypo numerio sklypo dalies kodų |
| `gamt_paminkl` | `integer` | — | `4` | `open` | — | Saugojamas gamtos paminklas | Ar saugomas objektas yra gamtos paminklas |
| `gamt_pam_steig_ta` | `string` | — | `4` | `open` | — | Teisės aktas | Paskelbimo gamtos paminklu teisinis pagrindas |
| `gamt_pam_steigimas` | `date` | `D` | `4` | `open` | — | Paskelbimo gamtos paminklu data | — |
| `bendr_reglam` | `integer` | — | `4` | `open` | — | Reglamentas | Bendrieji veiklos reglamentai nuoroda į teisės aktą |
| `spec_reglam` | `string` | — | `4` | `open` | — | Reglamentai | Specialieji / individualieji veiklos reglamentai |
| `saltiniai_lt` | `string` | — | `4` | `open` | — | Duomenų šaltiniai | Nurodomi moksliniai tyrimai ir publikacijos |
| `buf_zona_apras` | `string` | — | `4` | `open` | — | Buferinė zona | Duomenys apie valstybinio parko buferinę apsaugos zoną |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `steigejas_galiojantis` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja gamtos paveldo objekto riba (vieta) reglamentai arba šis teisės aktas yra šiuo metu galiojantis gamtos paveldo objekto teisinis pagrindas |
| `planavimo_dok` | `string` | — | `4` | `open` | — | Planavimo dokumentas | Duomenys apie parengtus planavimo dokumentus |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `mineralizacija` | `number` | `mg/l` | `4` | `open` | — | Mineralizacija | — |
| `vandenskietumas` | `number` | `mg/l` | `4` | `open` | — | Vandens kietumas | — |
| `obj_status` | `integer` | — | `4` | `open` | — | Objekto būsena | — |
| `vandens_tipas_lt` | `string` | — | `4` | `open` | — | Vandens tipas | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"nk1"` | — | — | Valstybinis | — |
| `gkodas` | `"nk2"` | — | — | Savivaldybės | — |
| `reiksme` | `1` | — | — | Valstybės saugomas | — |
| `reiksme` | `2` | — | — | Savivaldybės saugomas | — |
| `objektu_rusys` | `1` | — | — | Šaltiniai, versmės | — |
| `gamt_paminkl` | `0` | — | — | Nepaminklas | — |
| `gamt_paminkl` | `1` | — | — | Paminklas | — |
| `bendr_reglam` | `1` | — | — | Rezervatai | — |
| `bendr_reglam` | `2` | — | — | Draustiniai | — |
| `bendr_reglam` | `3` | — | — | Parkai | — |
| `bendr_reglam` | `4` | — | — | Sklypai | — |
| `bendr_reglam` | `5` | — | — | Biosferos Poligonai, Biosferos Rezervatai | — |
| `bendr_reglam` | `6` | — | — | Gamtos paveldo objektai | — |
| `obj_status` | `1` | — | — | Aktualūs | — |
| `obj_status` | `2` | — | — | Sunykę | — |
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
| `skelbejas_lt` | `update("skelbejas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `chem_savyb_lt` | `update("chem_savyb_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `kiti_param_lt` | `update("kiti_param_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `adm_pavadinimas_lt` | `update("adm_pavadinimas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `adm_pavadinimas_sen_lt` | `update("adm_pavadinimas_sen_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `gyv_pavad_v_lt` | `update("gyv_pavad_v_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `gat_pavadinimas_lt` | `update("gat_pavadinimas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `mu_pavad_lt` | `update("mu_pavad_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `gir_pavad_lt` | `update("gir_pavad_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `saltiniai_lt` | `update("saltiniai_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `vieta_lt` | `update("vieta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `vandens_tipas_lt` | `update("vandens_tipas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv
