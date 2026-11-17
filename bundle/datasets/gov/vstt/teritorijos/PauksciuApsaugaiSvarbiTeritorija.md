---
type: Table
title: "PauksciuApsaugaiSvarbiTeritorija — Paukščių apsaugai svarbios teritorijos"
description: "Spinta table datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232"
    last_modified: "2026-11-11T14:39:20Z"
---

# PauksciuApsaugaiSvarbiTeritorija — Paukščių apsaugai svarbios teritorijos

- **Model:** `datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `bast_kodas` | `string` | — | `4` | `open` | — | Vietovės identifikatorius | — |
| `vieta_lt` | `string` | — | `4` | `open` | — | Vieta | Aprašomoji informacija (savivaldybė seniūnija jei miškas – papildomai miškų urėdija girininkija miško kvartalas ir sklypas) |
| `registruota` | `date` | `D` | `4` | `open` | — | Įregistravimo data | Įregistravimo į kadastrą data |
| `isregistruota` | `date` | `D` | `4` | `open` | — | Išregistravimo iš kadastro data | — |
| `isreg_priez_lt` | `string` | — | `4` | `open` | — | Išregistravimo priežastis | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Teritorija | Paukščių apsaugai svarbios teritorijos pavadinimas |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |
| `ilgis` | `number` | `m` | `4` | `open` | — | Ilgis | — |
| `steigimas` | `date` | `D` | `4` | `open` | — | Statuso suteikimo data | — |
| `steig_ta` | `string` | — | `4` | `open` | — | Teises aktas | Paukščių apsaugai svarbios vietovės įsteigimo pagrindas (juridinis aktas) |
| `bendr_reglam` | `string` | — | `4` | `open` | — | Reglamentas | Bendrieji veiklos reglamentai nuoroda į teisės aktą |
| `isreg_ta` | `string` | — | `4` | `open` | — | Išregistravimo | Teisės aktas |
| `steig_tikslas` | `string` | — | `4` | `open` | — | Steigimo tikslas | Aprašomoji informacija |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Ploto geometrija | — |
| `id_vart` | `integer` | — | `4` | `open` | — | Abonento klasifikatorius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
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
| `isreg_priez_lt` | `update("isreg_priez_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv
