---
type: Table
title: "FunkcinioPrioritetoZona — Funkcinio prioriteto zonos"
description: "Saugomų teritorijų valstybės kadastro duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/FunkcinioPrioritetoZona"
tags: [gov, vstt, funkcinioprioritetozona, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L614"
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L614"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# FunkcinioPrioritetoZona — Funkcinio prioriteto zonos

**Dataset Context:** Saugomų teritorijų valstybės kadastro duomenys[^manifest]

- **Model:** `datasets/gov/vstt/teritorijos/FunkcinioPrioritetoZona`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L614](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L614)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/FunkcinioPrioritetoZona` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `gkodas` | `string` | — | `4` | `open` | — | InGIS geokodas | Saugomos teritorijos tipas |
| `pavadinimas` | `string` | — | `4` | `open` | — | Zonos pavadinimas | — |
| `st_id` | `string` | — | `4` | `open` | — | Identifikatorius | Jei gamtos paveldo objektas yra saugomoje teritorijoje pildomas saugomos teritorijos kurioje yra gamtos paveldo objektas identifikatorius |
| `st_gkodas` | `string` | — | `4` | `open` | — | Teritorijos kodas | Saugomos teritorijos kuriai priklauso buferinės apsaugos zona tipas – geokodas (visų saugomų teritorijos tipų pagal InGIS standartą klasifikatorius) |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `teisinis_pagrindas` | `string` | — | `4` | `open` | — | Teises aktas | Funkcinio prioriteto zonavimo schemos parengimo teisinis pagrindas |
| `schemos_rengejas_lt` | `string` | — | `4` | `open` | — | Institucija | Funkcinio prioriteto zonavimo schemos rengėjas – institucija |
| `parengta` | `date` | `D` | `4` | `open` | — | Parengimo data | Funkcinio prioriteto zonavimo schemos parengimo data |
| `schem_apras` | `string` | — | `4` | `open` | — | Pastabos aprašomoji informacija | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `st_tipas` | `integer` | — | `4` | `open` | — | Zonos tipas | Saugomos teritorijos kurioje yra funkcinio prioriteto zona tipas |
| `pobudis` | `integer` | — | `4` | `open` | — | Funkcinio prioriteto zonos pobūdis | — |
| `centras` | `geometry(point,4326)` | `m` | `4` | `open` | — | Centro koordinatė | Svorio centro koordinatės LKS’94 koordinačių sistemoje |
| `steigejas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `steigejas._id`) | `4` | `open` | — | Steigėjas – institucija | — |
| `steigimas` | `date` | `D` | `4` | `open` | — | Steigimo data | — |
| `steig_ta` | `string` | — | `4` | `open` | — | Įsteigimo teisės aktas | — |
| `steigejas_galiojantis` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `steigejas_galiojantis._id`) | `4` | `open` | — | Steigėjas | Institucija kurios potvarkiu šiuo metu galioja saugoma teritorija arba jos riba |
| `galiojantis` | `date` | `D` | `4` | `open` | — | Steigimo data | Šiuo metu galiojančio saugomos teritorijos steigimo teisės akto data |
| `steig_ta_galiojantis` | `string` | — | `4` | `open` | — | Teisinis statusas | Teisės aktas pagal kurį šiuo metu galioja saugomos teritorijos riba reglamentai arba šis teisės aktas yra šiuo metu galiojantis saugomos teritorijos teisinis pagrindas |
| `steig_tikslas` | `string` | — | `4` | `open` | — | Steigimo tikslas | Aprašomoji informacija |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `reiksme` | `integer` | — | `4` | `open` | — | Objekto reikšmė | Gamtos paveldo objekto reikšmė: valstybės saugomi savivaldybės saugomi |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"nz12"` | — | — | Ekologinės apsaugos prioriteto | — |
| `gkodas` | `"nz6"` | — | — | Rekreacinio prioriteto zona | — |
| `gkodas` | `"nz7"` | — | — | Ūkinio prioriteto zona | — |
| `gkodas` | `"nz8"` | — | — | Miškų ūkio prioriteto zona | — |
| `gkodas` | `"nz9"` | — | — | Žemės ūkio prioriteto zona | — |
| `gkodas` | `"nz10"` | — | — | Vandens ūkio prioriteto zona | — |
| `gkodas` | `"nz11"` | — | — | Kitos paskirties prioriteto zona | — |
| `gkodas` | `"nz13"` | — | — | Gyvenamosios paskirties prioriteto zona | — |
| `gkodas` | `"nz15"` | — | — | Ekosistemų atkūrimo prioriteto zona | — |
| `st_gkodas` | `"np4"` | — | — | Biosferos rezervatas | — |
| `st_gkodas` | `"np5"` | — | — | Biosferos poligonas | — |
| `st_gkodas` | `"np1"` | — | — | Nacionalinis parkas | — |
| `st_gkodas` | `"np2"` | — | — | Regioninis parkas | — |
| `st_tipas` | `1` | — | — | Nacionalinis parkas | — |
| `st_tipas` | `2` | — | — | Regioninis parkas | — |
| `st_tipas` | `4` | — | — | Biosferos rezervatas | — |
| `st_tipas` | `5` | — | — | Biosferos poligonas | — |
| `pobudis` | `100` | — | — | Ekologinės apsaugos prioriteto zona | — |
| `pobudis` | `200` | — | — | Rekreacinio prioriteto zona | — |
| `pobudis` | `300` | — | — | Ūkinio prioriteto zona | — |
| `pobudis` | `301` | — | — | Miškų ūkio prioriteto zona | — |
| `pobudis` | `302` | — | — | Žemės ūkio prioriteto zona | — |
| `pobudis` | `303` | — | — | Vvandens ūkio prioriteto zona | — |
| `pobudis` | `600` | — | — | Kito prioriteto zona | — |
| `pobudis` | `601` | — | — | Gyvenamosios paskirties prioriteto zona | — |
| `pobudis` | `602` | — | — | Visuomeninės paskirties prioriteto zona | — |
| `pobudis` | `603` | — | — | Karinės paskirties prioriteto zona | — |
| `pobudis` | `604` | — | — | Muziejų paskirties prioriteto zona | — |
| `pobudis` | `605` | — | — | Kitos | — |
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
| `schemos_rengejas_lt` | `update("schemos_rengejas_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `vieta_lt` | `update("vieta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L614 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L614)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos (https://data.gov.lt/datasets/789/)
