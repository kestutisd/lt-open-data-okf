---
type: Table
title: "Remimas"
description: "Spinta table datasets/gov/vrk/remimai/Remimas (18 columns)."
tags: [gov, vrk, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/remimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/remimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Remimas

- **Model:** `datasets/gov/vrk/remimai/Remimas`[^manifest]
- **Dataset:** [datasets/gov/vrk/remimai](../remimai.md) (`datasets/gov/vrk/remimai`)
- **Manifest CSV:** [datasets/gov/vrk/remimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/remimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `remimai_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `remimai_id` | `integer` | — | `4` | `open` | — | — | — |
| `rinkimu_id` | `integer` | — | `2` | `open` | — | Rinkimų identifikatorius | — |
| `rinkimu_pavad` | `string` | — | `2` | `open` | — | Rinkimų pavadinimas | — |
| `apyg_id` | `integer` | — | `2` | `open` | — | Apygardos identifikatorius | Vienmandatės apygardos, kurioje keliamas kandidatas ar kandidatų sąrašas, ID |
| `apyg_nr` | `integer` | — | `2` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `2` | `open` | — | Apygardos pavadinimas | — |
| `p_kamp_dal_id` | `integer` | — | `2` | `open` | — | Politinės kampanijos dalyvio identifikatorius | — |
| `p_kamp_dal_pavad` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio pavardė/pavadinimas | Politinės kampanijos dalyvio pavadinimas |
| `p_kamp_dal_vardas` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio vardas | Politinės kampanijos dalyvio vardas, jei fizinis asmuo (FA) |
| `org_id` | `integer` | — | `2` | `open` | — | Politinės organizacijos indetifikatorius | — |
| `org_ja_kodas` | `string` | — | `2` | `open` | — | Politinės organizacijos juridinio asmens kodas Juridinių asmenų registre | — |
| `reikiamas_parasu_skaicius` | `integer` | `U` | `4` | `open` | — | Reikiamas rinkėjų parašų skaičius | Reikiamas rinkėjų, parėmusių kandidato ir (arba) kandidatų sąrašo iškėlimą arba kandidato išsikėlimą, parašų skaičius |
| `rinkejo_kodas` | `string` | — | `4` | `open` | — | Atsitiktinai sugeneruotas parėmusio asmens kodas | Atsekamumas tik šiame rinkinyje (atsitiktinai sugeneruotas) |
| `lytis` | `string` | — | `4` | `open` | — | Parėmusio asmens lytis | Parėmusio asmens lytis (V/M) |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Parėmusio asmens amžiaus grupė (pasirašymo dieną) | Parėmusio asmens amžiaus grupė intervalais (nuo - iki), kas 5 metai. Amžiaus grupės: 18-24; 25-29; 30-34; 35-39; ....; 75-79; 80 +; |
| `paraso_busenos_kodas` | `string` | — | `4` | `open` | — | Parašo būsenos kodas | Parašo būsenos kodas (R, A) |
| `paraso_busena` | `string` | — | `4` | `open` | — | Parašo būsenos pavadinimas | Parašo būsenos pavadinimas (Galiojantis/Anuliuotas) |
| `paraso_busenos_data` | `date` | `D` | `4` | `open` | — | Parašo būsenos pasikeitimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `amziaus_grupe` | `"18-24"` | — | — | Amžiaus grupė nuo 18 iki 24 metų | — |
| `amziaus_grupe` | `"25-29"` | — | — | Amžiaus grupė nuo 25 iki 29 metų | — |
| `amziaus_grupe` | `"30-34"` | — | — | Amžiaus grupė nuo 30 iki 34 metų | — |
| `amziaus_grupe` | `"35-39"` | — | — | Amžiaus grupė nuo 35 iki 39 metų | — |
| `amziaus_grupe` | `"40-44"` | — | — | Amžiaus grupė nuo 40 iki 44 metų | — |
| `amziaus_grupe` | `"45-49"` | — | — | Amžiaus grupė nuo 45 iki 49 metų | — |
| `amziaus_grupe` | `"50-54"` | — | — | Amžiaus grupė nuo 50 iki 54 metų | — |
| `amziaus_grupe` | `"55-59"` | — | — | Amžiaus grupė nuo 55 iki 59 metų | — |
| `amziaus_grupe` | `"60-64"` | — | — | Amžiaus grupė nuo 60 iki 64 metų | — |
| `amziaus_grupe` | `"65-69"` | — | — | Amžiaus grupė nuo 65 iki 69 metų | — |
| `amziaus_grupe` | `"70-74"` | — | — | Amžiaus grupė nuo 70 iki 74 metų | — |
| `amziaus_grupe` | `"75-79"` | — | — | Amžiaus grupė nuo 75 iki 79 metų | — |
| `amziaus_grupe` | `"80+"` | — | — | Amžiaus grupė nuo 80 metų | — |
| `paraso_busenos_kodas` | `"R"` | — | — | Pasirašytas | — |
| `paraso_busenos_kodas` | `"A"` | — | — | Atšauktas | — |
| `paraso_busena` | `"Pasirašytas"` | — | — | Galiojantis | — |
| `paraso_busena` | `"Atšauktas"` | — | — | Anuliuotas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/remimai.csv
