---
type: Table
title: "BiudzetoVykdymoAtaskaita — Biudžeto vykdymo ataskaita"
description: "Valstybės kontrolės biudžeto išlaidų sąmatos vykdymo duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/bva/BiudzetoVykdymoAtaskaita"
tags: [gov, vk, biudzetovykdymoataskaita, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bva.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vk/bva.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1847/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/bva"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# BiudzetoVykdymoAtaskaita — Biudžeto vykdymo ataskaita

Valstybės kontrolės biudžeto išlaidų sąmatos vykdymo duomenys[^manifest]

- **Model:** `datasets/gov/vk/bva/BiudzetoVykdymoAtaskaita`[^manifest]
- **Dataset:** [Valstybės kontrolės biudžeto vykdymo ataskaitų duomenys](../bva.md) (`datasets/gov/vk/bva`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/bva.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bva.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/bva/BiudzetoVykdymoAtaskaita` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `integer` | — | `2` | `open` | — | Metai | Metai |
| `ataskaitinis_ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | Ketvirtis |
| `iekk_i_kodas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos I kodas | Išlaidų ekonominės klasifikacijos I kodas |
| `iekk_i_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos I kodo pavadinimas | Išlaidų ekonominės klasifikacijos I kodo pavadinimas |
| `iekk_ii_kodas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos II kodas | Išlaidų ekonominės klasifikacijos II kodas |
| `iekk_ii_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos II kodo pavadinimas | Išlaidų ekonominės klasifikacijos II kodo pavadinimas |
| `iekk_iii_kodas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos III kodas | Išlaidų ekonominės klasifikacijos III kodas |
| `iekk_iii_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos III kodo pavadinimas | Išlaidų ekonominės klasifikacijos III kodo pavadinimas |
| `iekk_iv_kodas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos IV kodas | Išlaidų ekonominės klasifikacijos IV kodas |
| `iekk_iv_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos IV kodo pavadinimas | Išlaidų ekonominės klasifikacijos IV kodo pavadinimas |
| `iekk_v_kodas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos V kodas | Išlaidų ekonominės klasifikacijos V kodas |
| `iekk_v_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos V kodo pavadinimas | Išlaidų ekonominės klasifikacijos V kodo pavadinimas |
| `iekk_vi_kodas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos VI kodas | Išlaidų ekonominės klasifikacijos VI kodas |
| `iekk_vi_pavadinimas` | `string` | — | `3` | `open` | — | Išlaidų ekonominės klasifikacijos VI kodo pavadinimas | Išlaidų ekonominės klasifikacijos VI kodo pavadinimas |
| `asignavimu_planas_metams` | `number` | — | `2` | `open` | — | Asignavimų planas metams | Asignavimų planas metams |
| `asignavimu_planas_ataskaitiniam_laikotarpiui` | `number` | — | `2` | `open` | — | Asignavimų planas ataskaitiniam laikotarpiui | Asignavimų planas ataskaitiniam laikotarpiui, suma Eur |
| `gauti_asignavimai_kartu_su_iskaitytu_prajusiu_metu_lesu_likuciu` | `number` | — | `2` | `open` | — | Gauti asignavimai kartu su įskaitytu praėjusių metų lėšų likučiu | Gauti asignavimai kartu su įskaitytu praėjusių metų lėšų likučiu, suma Eur |
| `panaudoti_asignavimai` | `number` | — | `2` | `open` | — | Panaudoti asignavimai | Panaudoti asignavimai, suma Eur |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `asignavimu_planas_metams` | `update(type: "money", ref: "EUR")` | `type, ref` | `4` | — | `spinta: 40` | — | — |
| `asignavimu_planas_ataskaitiniam_laikotarpiui` | `update(type: "money", ref: "EUR")` | `type, ref` | `4` | — | `spinta: 40` | — | — |
| `gauti_asignavimai_kartu_su_iskaitytu_prajusiu_metu_lesu_likuciu` | `update(type: "money", ref: "EUR")` | `type, ref` | `4` | — | `spinta: 40` | — | — |
| `panaudoti_asignavimai` | `update(type: "money", ref: "EUR")` | `type, ref` | `4` | — | `spinta: 40` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/bva.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bva.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/bva (https://data.gov.lt/datasets/1847/)
