---
type: Table
title: "PauksciuApsaugaiSvarbiTeritorija — Paukščių apsaugai svarbios teritorijos"
description: "Saugomų teritorijų valstybės kadastro duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija"
tags: [gov, vstt, pauksciuapsaugaisvarbiteritorija, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232"
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PauksciuApsaugaiSvarbiTeritorija — Paukščių apsaugai svarbios teritorijos

**Dataset Context:** Saugomų teritorijų valstybės kadastro duomenys[^manifest]

- **Model:** `datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija`[^manifest]
- **Dataset:** [Saugomų teritorijų valstybės kadastro duomenys](../teritorijos.md) (`datasets/gov/vstt/teritorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos/PauksciuApsaugaiSvarbiTeritorija` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L1232)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos (https://data.gov.lt/datasets/789/)
