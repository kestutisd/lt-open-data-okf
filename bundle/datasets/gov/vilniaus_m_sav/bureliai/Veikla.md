---
type: Table
title: "Veikla — Neformaliojo ugdymo veiklos Vilniaus mieste"
description: "Rinkinyje skelbiami duomenys apie Vilniaus mieste vykdytas ir vykdomas neformaliojo ugdymo veiklas nuo 2017 m. iki dabar."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/bureliai/Veikla"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/bureliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/bureliai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Veikla — Neformaliojo ugdymo veiklos Vilniaus mieste

Rinkinyje skelbiami duomenys apie Vilniaus mieste vykdytas ir vykdomas neformaliojo ugdymo veiklas nuo 2017 m. iki dabar. Viena rinkinio lentelės eilutė– yra viena neformaliojo švietimo veikla. Pateikiama informacija apie veiklą organizuojančią įstaigą, užsiėmimų dažnį, veiklos pradžios ir paskutinio įvykusio užsiėmimo datas, mėnesinį mokestį, maksimalų dalyvių skaičių ir amžiaus grupes, kurioms skirtos veiklos.

- **Model:** `datasets/gov/vilniaus_m_sav/bureliai/Veikla`[^manifest]
- **Dataset:** [Neformaliojo ugdymo veiklos Vilniaus mieste](../bureliai.md) (`datasets/gov/vilniaus_m_sav/bureliai`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/bureliai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/bureliai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/bureliai/Veikla`
- **Primary Key (`ref`):** `veiklos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veiklos_id` | `string` | — | `4` | `open` | — | Veiklos identifikatorius | — |
| `institucija` | `string` | — | `4` | `open` | — | Veiklą organizuojančios institucijos pavadinimas | — |
| `informacija_lt` | `string` | — | `2` | `open` | — | Papildoma informacija | — |
| `veiklos_pav_lt` | `string` | — | `2` | `open` | — | Veiklos pavadinimas | — |
| `ar_vyksta` | `boolean` | — | `4` | `open` | — | Požymis, ar neformaliojo ugdymo veikla vykdoma duomenų atnaujinimo momentu | — |
| `veiklos_pradzia` | `date` | `D` | `4` | `open` | — | Veiklos pradžia | — |
| `paskutinis_uzsiemimas` | `date` | `D` | `4` | `open` | — | Paskutinio ligšiol vykusio užsiėmimo data. | — |
| `amzius` | `string` | — | `4` | `open` | — | Amžiaus grupė, kuriai skirta neformaliojo ugdymo veikla | — |
| `daznis` | `string` | — | `4` | `open` | — | Savaitės dienos, kuriomis vyksta užsiėmimai | — |
| `maks_lankytoju` | `integer` | `U` | `4` | `open` | — | Maksimalus užsiėmimo lankytojų skaičius | — |
| `men_mokestis_eur` | `number` | — | `4` | `open` | — | Mėnesinis mokestis eurais | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų apie veiklą atnaujinimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `informacija_lt` | `update(property: "informacija_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `veiklos_pav_lt` | `update(property: "veiklos_pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/bureliai.csv
