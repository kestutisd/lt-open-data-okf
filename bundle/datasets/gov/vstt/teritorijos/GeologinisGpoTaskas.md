---
type: Table
title: "GeologinisGpoTaskas — Geologiniai GPO Taškai"
description: "Saugomų teritorijų valstybės kadastro duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/GeologinisGpoTaskas"
tags: [gov, vstt, geologinisgpotaskas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L776"
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L776"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GeologinisGpoTaskas — Geologiniai GPO Taškai

**Dataset Context:** Saugomų teritorijų valstybės kadastro duomenys[^manifest]

- **Model:** `datasets/gov/vstt/teritorijos/GeologinisGpoTaskas`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L776](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L776)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/GeologinisGpoTaskas` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Gamtos paveldo objekto pavadinimas | — |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `reiksme` | `integer` | — | `4` | `open` | — | Objekto reikšmė | Gamtos paveldo objekto reikšmė: valstybės saugomi savivaldybės saugomi |
| `objektu_rusys` | `integer` | — | `4` | `open` | — | Geologinių objektų rūšys | — |
| `kult_paveld_kodas` | `integer` | — | `2` | `open` | — | Kodas | Jeigu gamtos paveldo objektas kartu turi ir kultūros paveldo objekto statusą nurodomas šio objekto kodas iš Nekilnojamųjų kultūros vertybių registro |
| `st_id` | `string` | — | `4` | `open` | — | Identifikatorius | Jei gamtos paveldo objektas yra saugomoje teritorijoje pildomas saugomos teritorijos kurioje yra gamtos paveldo objektas identifikatorius |
| `skelbejas_lt` | `string` | — | `4` | `open` | — | Paskelbusi institucija | Objektą saugomu paskelbė (paskelbusi – institucija) |
| `skelbiama` | `date` | `D` | `4` | `open` | — | Skelbimo data | Objekto paskelbimo saugomu data (metai mėnuo diena) |
| `skelb_ta` | `string` | — | `4` | `open` | — | Teisės aktas | Objekto paskelbimo saugomu teisinis pagrindas |
| `skelb_tikslas` | `string` | — | `4` | `open` | — | Objekto skelbimo saugomu tikslas | Aprašomoji informacija |
| `aukstis` | `number` | `m` | `4` | `open` | — | Aukštis | — |
| `ilgis` | `number` | `m` | `4` | `open` | — | Ilgis | — |
| `plotis` | `number` | `m` | `4` | `open` | — | Plotis | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `perimet` | `number` | `m` | `4` | `open` | — | Perimetras | — |
| `kiti_lt` | `string` | — | `4` | `open` | — | Kiti parametrai | — |
| `adm_hier_kodas` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID` via `Savivaldybe[sav_kodas]`: `adm_hier_kodas._id`) | `4` | `open` | — | Savivaldybės kodas | — |
| `adm_pavadinimas_lt` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `adm_hier_kodas_sen` | `ref` | [Seniunija](../../rc/ar/seniunija/Seniunija.md) (`level=4 UUID` via `Seniunija[sen_kodas]`: `adm_hier_kodas_sen._id`) | `4` | `open` | — | Seniūnijos kodas | — |
| `adm_pavadinimas_sen_lt` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gyv_rej_kodas` | `ref` | [GyvenamojiVietove](../../rc/ar/gyvenamojivietove/GyvenamojiVietove.md) (`level=4 UUID` via `GyvenamojiVietove[gyv_kodas]`: `gyv_rej_kodas._id`) | `4` | `open` | — | Gyvenamosios vietovės rejestro kodas | — |
| `gyv_pavad_v_lt` | `string` | — | `4` | `open` | — | Gyvenamosios vietovės pavadinimas | — |
| `gat_kodas` | `ref` | [Gatve](../../rc/ar/gatve/Gatve.md) (`level=4 UUID` via `Gatve[gat_kodas]`: `gat_kodas._id`) | `4` | `open` | — | Gatvės kodas | — |
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
| `steigejas_galiojantis` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `steigejas_galiojantis._id`) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja gamtos paveldo objekto riba (vieta) reglamentai arba šis teisės aktas yra šiuo metu galiojantis gamtos paveldo objekto teisinis pagrindas |
| `planavimo_dok` | `string` | — | `4` | `open` | — | Planavimo dokumentas | Duomenys apie parengtus planavimo dokumentus |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `obj_status` | `integer` | — | `4` | `open` | — | Objekto būsena | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"nk1"` | — | — | Valstybinis | — |
| `gkodas` | `"nk2"` | — | — | Savivaldybės | — |
| `reiksme` | `1` | — | — | Valstybės saugomas | — |
| `reiksme` | `2` | — | — | Savivaldybės saugomas | — |
| `objektu_rusys` | `1` | — | — | Rieduliai | — |
| `objektu_rusys` | `2` | — | — | Atodangos | — |
| `objektu_rusys` | `3` | — | — | Olos, smegduobės, įgriuvos | — |
| `objektu_rusys` | `4` | — | — | Uolos | — |
| `objektu_rusys` | `5` | — | — | Fosilijų ir mineralų radavietės | — |
| `objektu_rusys` | `6` | — | — | Riedulių ekspozicijos | — |
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
| `kiti_lt` | `update("kiti_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `adm_pavadinimas_lt` | `update("adm_pavadinimas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `adm_pavadinimas_sen_lt` | `update("adm_pavadinimas_sen_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `gyv_pavad_v_lt` | `update("gyv_pavad_v_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `gat_pavadinimas_lt` | `update("gat_pavadinimas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `mu_pavad_lt` | `update("mu_pavad_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `gir_pavad_lt` | `update("gir_pavad_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `saltiniai_lt` | `update("saltiniai_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `vieta_lt` | `update("vieta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L776 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L776)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos (https://data.gov.lt/datasets/789/)
