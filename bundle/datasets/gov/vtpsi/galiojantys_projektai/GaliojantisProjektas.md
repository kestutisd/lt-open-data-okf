---
type: Table
title: "GaliojantisProjektas — Galiojantys projektai (VTPSI)"
description: "VTPSI galiojantys statybos projektai"
resource: "https://get.data.gov.lt/datasets/gov/vtpsi/galiojantys_projektai/GaliojantisProjektas"
tags: [gov, vtpsi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtpsi/galiojantys_projektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtpsi/galiojantys_projektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# GaliojantisProjektas — Galiojantys projektai (VTPSI)

VTPSI galiojantys statybos projektai

- **Model:** `datasets/gov/vtpsi/galiojantys_projektai/GaliojantisProjektas`[^manifest]
- **Dataset:** [datasets/gov/vtpsi/galiojantys_projektai](../galiojantys_projektai.md) (`datasets/gov/vtpsi/galiojantys_projektai`)
- **Manifest CSV:** [datasets/gov/vtpsi/galiojantys_projektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtpsi/galiojantys_projektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtpsi/galiojantys_projektai/GaliojantisProjektas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto ID | — |
| `statinio_id` | `string` | — | `4` | `open` | — | Statinio ID | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `projekto_reg_nr` | `string` | — | `4` | `open` | — | Projekto registracijos numeris | — |
| `projekto_metai` | `integer` | — | `2` | `open` | — | Projekto metai | — |
| `unikalus_numeris` | `string` | — | `4` | `open` | — | Unikalus numeris | — |
| `statinio_paskirtis` | `string` | — | `4` | `open` | — | Statinio paskirtis | — |
| `statinio_pakeista_paskirtis` | `string` | — | `4` | `open` | — | Statinio pakeista paskirtis | — |
| `statinio_kategorija` | `string` | — | `4` | `open` | — | Statinio kategorija | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas | — |
| `statybos_rusis` | `string` | — | `4` | `open` | — | Statybos rūšis | — |
| `statinio_pavadinimas` | `string` | — | `4` | `open` | — | Statinio pavadinimas | — |
| `pastatymo_metai` | `integer` | — | `3` | `open` | — | Pastatymo metai | — |
| `kadastro_nr` | `string` | — | `4` | `open` | — | Kadastro numeris | — |
| `ploto_reg_tipas` | `string` | — | `4` | `open` | — | Ploto registracijos tipas | — |
| `sklypo_reg_statusas` | `string` | — | `4` | `open` | — | Sklypo registracijos statusas | — |
| `dokumento_reg_nr` | `string` | — | `4` | `open` | — | Dokumento registracijos numeris | — |
| `dokumento_reg_data` | `date` | `D` | `4` | `open` | — | Dokumento registracijos data | — |
| `iraso_paaiskinimas` | `string` | — | `4` | `open` | — | Įrašo paaiškinimas | — |
| `iraso_data` | `date` | `D` | `4` | `open` | — | Įrašo data | — |
| `dok_statusas` | `string` | — | `4` | `open` | — | Dokumento statusas | — |
| `dok_tipo_kodas` | `string` | — | `4` | `open` | — | Dokumento tipo kodas | — |
| `dokumento_kategorija` | `string` | — | `4` | `open` | — | Dokumento kategorija | — |
| `dok_irasas` | `string` | — | `4` | `open` | — | Dokumento įrašas | — |
| `uuid` | `string` | — | `4` | `open` | — | UUID | — |
| `taskas_lks` | `geometry(3346)` | — | `3` | `open` | — | Taško koordinatės pagal Lietuvos Koordinačių Sistemą (LKS) | — |
| `taskas_wgs` | `geometry(point)` | — | `3` | `open` | — | Taško koordinatės pagal Geografinę Koordinačių Sistemą (WGS) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtpsi/galiojantys_projektai.csv
