---
type: Table
title: "MedzioMatavimas — Medžių matavimai"
description: "Lentelėje skelbiami medžių matavimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/MedzioMatavimas"
tags: [gov, vmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# MedzioMatavimas — Medžių matavimai

Lentelėje skelbiami medžių matavimų duomenys. Viena eilutė - medžio matavimas trakto barelio sektoriuje vieno penkmečio laikotarpu. Pateikiami medžio lokacijos duomenys barelio centro atžvilgiu, bendros charakteristikos (amžius, skersmuo, aukštis, nulaužtumas) ir medžio pažeidimai.

- **Model:** `datasets/gov/vmt/inventorizacija/MedzioMatavimas`[^manifest]
- **Dataset:** [Nacionalinės miškų inventorizacijos matavimų duomenys](../inventorizacija.md) (`datasets/gov/vmt/inventorizacija`)
- **Manifest CSV:** [datasets/gov/vmt/inventorizacija.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/MedzioMatavimas`
- **Primary Key (`ref`):** `matavimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `matavimo_id` | `string` | — | `4` | `open` | — | Medžio matavimo identifikacinis numeris | — |
| `medzio_id` | `string` | — | `4` | `open` | — | Medžio identifikacinis numeris | — |
| `ankst_medzio_id` | `string` | — | `4` | `open` | — | Medžio identifikacinis numeris ankstesniame matavime | — |
| `penkmetis` | `string` | — | `4` | `open` | — | Medžio matavimo penkmetis | — |
| `trakto_id` | `string` | — | `4` | `open` | — | Trakto identifikacinis numeris | — |
| `barelio_id` | `string` | — | `4` | `open` | — | Barelio identifikacinis numeris | — |
| `barelio_nr` | `string` | — | `4` | `open` | — | Barelio numeris | — |
| `kraftas` | `string` | — | `4` | `open` | — | Krafto klasė | — |
| `sektoriaus_id` | `string` | — | `4` | `open` | — | Sektoriaus identifikacinis numeris | — |
| `buv_sektoriaus_id` | `string` | — | `4` | `open` | — | Ankstesnis sektoriaus numeris | — |
| `ardas` | `string` | — | `4` | `open` | — | Vyraujantis ardas | — |
| `atstumas` | `string` | — | `4` | `open` | — | Atstumas nuo trakto kraštinės | — |
| `atstumas_nuo_centro` | `number` | `m` | — | — | — | Atstumas nuo barelio centro iki medžio (kelmo), nurodytas metrais | — |
| `azimutas` | `number` | `°` | — | — | — | Azimutas | — |
| `rusis_lot` | `string` | — | `4` | `open` | — | Lotyniškas medžio rūšies pavadinimas | — |
| `rusis_lt` | `string` | — | `4` | `open` | — | Lietuviškas rūšies pavadinimas | — |
| `amzius` | `integer` | — | `4` | `open` | — | Medžio amžius | — |
| `rieviu_sk` | `integer` | — | `4` | `open` | — | Medžio rievių skaičius | — |
| `bukle` | `string` | — | `4` | `open` | — | Medžio būklė matavimo metu | — |
| `klaidos_tipas` | `string` | — | `4` | `open` | — | Jei atliekant matavimą įvyko klaida, nurodomas jos tipas | — |
| `skersmuo_kakl_cm` | `number` | `cm` | `4` | `open` | — | Skersmuo šaknies kaklelyje, cm | — |
| `skersmuo_kakl_zv_cm` | `number` | `cm` | `4` | `open` | — | Skersmuo šaknies kaklelyje (su žieve, nuo 2005 m be žievės), nurodytas centimetrais | — |
| `skersmuo_13_cm` | `number` | `cm` | `4` | `open` | — | Skersmuo 1,3 m. aukštyje, nurodytas centimetrais | — |
| `aukstis_m` | `number` | `m` | `4` | `open` | — | Aukštis, nurodytas metrais | — |
| `aukstis_iki_lajos_m` | `number` | `m` | `4` | `open` | — | Aukštis iki lajos, nurodytas metrais | — |
| `nulauzt_proc` | `number` | `%` | `4` | `open` | — | Medžio su nulaužta viršūne aukščio dalis (10 - visas aukštis) | — |
| `vieta_1` | `string` | — | `4` | `open` | — | Pirmojo pažeidimo vieta | — |
| `pazeidimas_1` | `string` | — | `4` | `open` | — | Pirmasis pažeidimas | — |
| `paz_1_intensyv_prc` | `number` | `%` | `4` | `open` | — | Pirmojo pažeidimo intensyvumas, išreikštas procentais | — |
| `vieta_2` | `string` | — | `4` | `open` | — | Antrojo pažeidimo vieta | — |
| `pazeidimas_2` | `string` | — | `4` | `open` | — | Antrasis pažeidimas | — |
| `paz_2_intensyv_prc` | `number` | `%` | `4` | `open` | — | Antrojo pažeidimo intensyvumas, išreikštas procentais | — |
| `vieta_3` | `string` | — | `4` | `open` | — | Trečiojo pažeidimo vieta | — |
| `pazeidimas_3` | `string` | — | `4` | `open` | — | Trečiasis pažeidimas | — |
| `paz_3_intensyv_prc` | `number` | `%` | `4` | `open` | — | Trečiojo pažeidimo intensyvumas, išreikštas procentais | — |
| `vieta_4` | `string` | — | `4` | `open` | — | Ketvirtojo pažeidimo vieta | — |
| `pazeidimas_4` | `string` | — | `4` | `open` | — | Ketvirtasis pažeidimas | — |
| `paz_4_intensyv_prc` | `number` | `%` | `4` | `open` | — | Ketvirtojo pažeidimo intensyvumas, išreikštas procentais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `penkmetis` | `"1998_02t"` | — | — | — | — |
| `penkmetis` | `"2003_07t"` | — | — | — | — |
| `penkmetis` | `"2008_12"` | — | — | — | — |
| `penkmetis` | `"2013_17"` | — | — | — | — |
| `penkmetis` | `"2018-2022"` | — | — | — | — |
| `kraftas` | `"Vyraujantys, bet plonesni, su ne tokiomis galingomis lajomis medžiai. Jų laja užima iki 1/3 aukščio ir pagal nusivalymą nuo šakų bei mažą stiebo nulaibėjimą sudaro vertingiausią medyno dalį"` | — | — | — | — |
| `kraftas` | `"Eiliniai, žymiai smulkesni nei II klasės, bet dar turintys saulės apšviečiamą viršūnę medžiai. Jų lajos suspaustos, retokos, dažnai netaisyklingos"` | — | — | — | — |
| `kraftas` | `"Stelbiami, smulkūs, ploni, įsispraudžiantys į bendrą lajų dangą medžiai, dažniausiai negaunantys tiesioginės saulės šviesos"` | — | — | — | — |
| `kraftas` | `"Dominuojantys, storais ir labai nulaibėjusiais kamienais su galinga, plačiai išskleista laja medžiai (apie 5% visų medžių)"` | — | — | — | — |
| `kraftas` | `"Visiškai užstelbti, džiūstantys medžiai"` | — | — | — | — |
| `atstumas` | `"Atstumas nuo trakto kraštinės pradžios 225 metrai"` | — | — | — | — |
| `atstumas` | `"Atstumas nuo trakto kraštinės pradžios 475 metrai"` | — | — | — | — |
| `klaidos_tipas` | `"Klaidingas rodiklis"` | — | — | — | — |
| `klaidos_tipas` | `"Praleistas medis"` | — | — | — | — |
| `klaidos_tipas` | `"Atmetamas medis"` | — | — | — | — |
| `klaidos_tipas` | `"Pakartotas medis"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv
