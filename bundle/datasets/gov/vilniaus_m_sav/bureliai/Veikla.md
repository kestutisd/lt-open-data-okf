---
type: Table
title: "Veikla — Neformaliojo ugdymo veiklos Vilniaus mieste"
description: "Rinkinyje skelbiami duomenys apie Vilniaus mieste vykdytas ir vykdomas neformaliojo ugdymo veiklas nuo 2017 m. iki dabar."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/bureliai/Veikla"
tags: [gov, vilniaus_m_sav, veikla, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/bureliai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/bureliai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3875/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/bureliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Veikla — Neformaliojo ugdymo veiklos Vilniaus mieste

Rinkinyje skelbiami duomenys apie Vilniaus mieste vykdytas ir vykdomas neformaliojo ugdymo veiklas nuo 2017 m. iki dabar. Viena rinkinio lentelės eilutė– yra viena neformaliojo švietimo veikla. Pateikiama informacija apie veiklą organizuojančią įstaigą, užsiėmimų dažnį, veiklos pradžios ir paskutinio įvykusio užsiėmimo datas, mėnesinį mokestį, maksimalų dalyvių skaičių ir amžiaus grupes, kurioms skirtos veiklos.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/bureliai/Veikla`[^manifest]
- **Dataset:** [Neformaliojo ugdymo veiklos Vilniaus mieste](../bureliai.md) (`datasets/gov/vilniaus_m_sav/bureliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/bureliai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/bureliai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/bureliai/Veikla` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `veiklos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/bureliai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/bureliai.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/bureliai (https://data.gov.lt/datasets/3875/)
