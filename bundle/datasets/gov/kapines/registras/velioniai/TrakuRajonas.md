---
type: Table
title: "TrakuRajonas — Trakų rajono savivaldybės kapinėse palaidotų velionių duomenys"
description: "Spinta table datasets/gov/kapines/registras/velioniai/TrakuRajonas (25 columns)."
resource: "https://get.data.gov.lt/datasets/gov/kapines/registras/velioniai/TrakuRajonas"
tags: [gov, kapines, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kapines/velionys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/velionys.csv#L1371"
    last_modified: "2026-11-11T14:39:20Z"
---

# TrakuRajonas — Trakų rajono savivaldybės kapinėse palaidotų velionių duomenys

- **Model:** `datasets/gov/kapines/registras/velioniai/TrakuRajonas`[^manifest]
- **Dataset:** [Duomenys apie velionis, palaidotus savivaldybių kapinėse](../velioniai.md) (`datasets/gov/kapines/registras/velioniai`)
- **Manifest CSV:** [datasets/gov/kapines/velionys.csv#L1371](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/velionys.csv#L1371)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/registras/velioniai/TrakuRajonas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `kapo_id` | `string` | — | `4` | `open` | — | Kapavietės identifikatorius | — |
| `ar_neatpazintas` | `boolean` | — | `4` | `open` | — | Neatpažinto velionio požymis | — |
| `ar_perlaidotas` | `boolean` | — | `4` | `open` | — | Požymis, ar velionis buvo perlaidotas | — |
| `ar_urnoje` | `boolean` | — | `4` | `open` | — | Požymis, ar velionis palaidotas urnoje | — |
| `vardas` | `string` | — | `4` | `open` | — | Velionio vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Velionio pavardė | — |
| `lytis` | `string` | — | `4` | `open` | — | Velionio lytis, išskaičiuota iš asmens kodo. | — |
| `ar_izymybe` | `boolean` | — | `4` | `open` | — | Požymis, ar velionis buvo žinomas asmuo | — |
| `veikla_lt` | `string` | — | `0` | `open` | — | Velionio veiklos duomenys | — |
| `aprasymas_lt` | `string` | — | `0` | `open` | — | Velionio gyvenimo veiklos aprašymas | — |
| `gimimo_data` | `date` | `D` | `4` | `open` | — | Velionio gimimo data | — |
| `mirties_data` | `date` | `D` | `4` | `open` | — | Velionio mirties data | — |
| `laidojimo_data` | `date` | `D` | `4` | `open` | — | Velionio laidojimo data | — |
| `liudijimo_isdavimas` | `date` | `D` | `4` | `open` | — | Velionio mirties liudijimo išdavimo data | — |
| `isdavimo_vieta` | `string` | — | `0` | `open` | — | Velionio mirties liudijimo išdavimo vieta | — |
| `kapo_gylis_m` | `number` | `m` | `4` | `open` | — | Velionio kapo gylis | — |
| `rysys_su_palaidotu` | `string` | — | `0` | `open` | — | Velionio ryšys su kitu kapavietėje palaidotu asmeniu | — |
| `kapa_priziuri` | `string` | — | `0` | — | — | Kapą prižiūrinčio asmens ryšys su velioniu | — |
| `sektorius` | `string` | — | `4` | `open` | — | Velionio kapavietės sektoriaus identifikatorius. Tai yra kapinėse esantis kvartalas, dažnu atveju išskiriamas pagal matomus takus kapinėse arba pagal pateiktą informaciją iš savivaldybių/ seniūnijų. Mažose kapinėse dažniausiai būna tik vienas kvartalas be jokių skirstymų. | — |
| `eile` | `string` | — | `4` | `open` | — | Velionio kapavietės eilė kapinėse, jei ji egzistuoja (ypač naudojama tvarkingo išplanavimo ir naujose kapinėse). Jeigu kapinėse nebuvo naudojamos eilės, tuomet žymima 000. | — |
| `kapaviete` | `string` | — | `4` | `open` | — | Velionio kapavietės numeris kapinėse | — |
| `vieta_kape` | `integer` | — | `4` | `open` | — | Velionio palaidojimo vieta kapavietėje. Pavyzdžiui, 3 vietų kapavietėje per vidurį laidojamam velioniui būtų žymima 2. | — |
| `geometrija` | `geometry(3857)` | — | `4` | `open` | — | Velionio kapavietės koordinatės pagal WGS84 / Pseudo-Mercator koordinačių sistemą. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/velionys.csv
