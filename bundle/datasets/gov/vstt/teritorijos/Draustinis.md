---
type: Table
title: "Draustinis — Draustiniai"
description: "Saugomų teritorijų valstybės kadastro duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/Draustinis"
tags: [gov, vstt, draustinis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L515"
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L515"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Draustinis — Draustiniai

**Dataset Context:** Saugomų teritorijų valstybės kadastro duomenys[^manifest]

- **Model:** `datasets/gov/vstt/teritorijos/Draustinis`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L515](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L515)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/Draustinis` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Draustinio pavadinimas | — |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `reiksme` | `integer` | — | `4` | `open` | — | Objekto reikšmė | Gamtos paveldo objekto reikšmė: valstybės saugomi savivaldybės saugomi |
| `draust_pobud` | `integer` | — | `4` | `open` | — | Draustinio pobūdis | Draustinio pobūdis – gamtinis kultūrinis kompleksinis (subtype) |
| `draust_rus` | `integer` | — | `2` | `open` | — | Draustinio rūšis | Draustinio rūšis (geologinis geomorfologinis t.t.) |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `steigejas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `steigejas._id`) | `4` | `open` | — | Steigėjas – institucija | — |
| `steigimas` | `date` | `D` | `4` | `open` | — | Steigimo data | — |
| `steig_ta` | `string` | — | `4` | `open` | — | Įsteigimo teisės aktas | — |
| `steig_tikslas` | `string` | — | `4` | `open` | — | Steigimo tikslas | Aprašomoji informacija |
| `bendr_reglam` | `integer` | — | `4` | `open` | — | Reglamentas | Bendrieji veiklos reglamentai nuoroda į teisės aktą |
| `spec_reglam` | `string` | — | `4` | `open` | — | Reglamentai | Specialieji / individualieji veiklos reglamentai |
| `saltiniai_lt` | `string` | — | `4` | `open` | — | Duomenų šaltiniai | Nurodomi moksliniai tyrimai ir publikacijos |
| `tarpt_svarba_status` | `integer` | — | `4` | `open` | — | Teritorijos statusas | Saugomai teritorijai arba jos daliai suteiktas tarptautinės svarbos (įskaitant Europos Bendrijų svarbos) teritorijos statusas |
| `tarpt_svarba_apras_lt` | `string` | — | `4` | `open` | — | Aprašas | Saugomai teritorijai arba jos daliai suteiktas tarptautinės svarbos (įskaitant Europos Bendrijų svarbos) teritorijos statuso aprašymas |
| `gamtiniai_kompleksai` | `integer` | — | `4` | `open` | — | Gamtiniai kompleksai | Duomenys apie saugomus gamtinius kompleksus ir jų būklę |
| `duomen_monitor_lt` | `string` | — | `4` | `open` | — | Monitoringas | Aplinkos stebėsenos (monitoringo) duomenys |
| `buf_zona_apras` | `string` | — | `4` | `open` | — | Buferinė zona | Duomenys apie valstybinio parko buferinę apsaugos zoną |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `steigejas_galiojantis` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `steigejas_galiojantis._id`) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja saugomos teritorijos riba reglamentai arba šis teisės aktas yra šiuo metu galiojantis saugomos teritorijos teisinis pagrindas |
| `st_id` | `string` | — | `4` | `open` | — | Identifikatorius | Jei gamtos paveldo objektas yra saugomoje teritorijoje pildomas saugomos teritorijos kurioje yra gamtos paveldo objektas identifikatorius |
| `tvarkymo_zona` | `string` | — | `4` | `open` | — | Zona | Duomenys apie kraštovaizdžio tvarkymo zonas |
| `planavimo_dok` | `string` | — | `4` | `open` | — | Planavimo dokumentas | Duomenys apie parengtus planavimo dokumentus |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `ta_nust_st_dalis` | `string` | — | `4` | `open` | — | Teises aktas | Teisės aktas nustatęs kad rezervatas tapo kompleksinės saugomos teritorijos dalimi |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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
| `reiksme` | `1` | — | — | Valstybinis | — |
| `reiksme` | `2` | — | — | Savivaldybės | — |
| `reiksme` | `3` | — | — | Konservacinio prioriteto funkcinė zona – rezervatas | — |
| `draust_pobud` | `1` | — | — | Gamtinis | — |
| `draust_pobud` | `2` | — | — | Kompleksinis | — |
| `draust_pobud` | `3` | — | — | Kultūrinis | — |
| `draust_rus` | `100` | — | — | Geologinis | — |
| `draust_rus` | `200` | — | — | Geomorfologinis | — |
| `draust_rus` | `300` | — | — | Hidrografinis | — |
| `draust_rus` | `400` | — | — | Pedologinis | — |
| `draust_rus` | `500` | — | — | Botaninis | — |
| `draust_rus` | `601` | — | — | Zoologinis-teriologinis | — |
| `draust_rus` | `602` | — | — | Zoologinis-ornitologinis | — |
| `draust_rus` | `603` | — | — | Zoologinis-herpetologinis | — |
| `draust_rus` | `604` | — | — | Zoologinis-ichtiologinis | — |
| `draust_rus` | `605` | — | — | Zoologinis-entomologinis | — |
| `draust_rus` | `700` | — | — | Botaninis-zoologinis | — |
| `draust_rus` | `800` | — | — | Genetinis | — |
| `draust_rus` | `900` | — | — | Telmologinis | — |
| `draust_rus` | `1000` | — | — | Talasologinis | — |
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
| `saltiniai_lt` | `update("saltiniai_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `tarpt_svarba_apras_lt` | `update("tarpt_svarba_apras_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `duomen_monitor_lt` | `update("duomen_monitor_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `vieta_lt` | `update("vieta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L515 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L515)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos (https://data.gov.lt/datasets/789/)
