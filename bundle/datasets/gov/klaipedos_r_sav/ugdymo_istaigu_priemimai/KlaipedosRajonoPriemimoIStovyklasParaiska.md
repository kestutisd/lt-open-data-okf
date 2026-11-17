---
type: Table
title: "KlaipedosRajonoPriemimoIStovyklasParaiska — Klaipėdos rajono priėmimai į stovyklas"
description: "Informacija apie vaikų priėmimo į Klaipėdos rajono savivaldybės stovyklas pateiktus prašymus"
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIStovyklasParaiska"
tags: [gov, klaipedos_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# KlaipedosRajonoPriemimoIStovyklasParaiska — Klaipėdos rajono priėmimai į stovyklas

Informacija apie vaikų priėmimo į Klaipėdos rajono savivaldybės stovyklas pateiktus prašymus

- **Model:** `datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIStovyklasParaiska`[^manifest]
- **Dataset:** [Priėmimai į Klaipėdos rajono ikimokyklinio ir mokyklinio ugdymo įstaigas](../ugdymo_istaigu_priemimai.md) (`datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai`)
- **Manifest CSV:** [datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIStovyklasParaiska`
- **Primary Key (`ref`):** `registracijos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `registracijos_id` | `string` | — | `4` | `open` | — | Registracijos į stovyklą identifikatorius | — |
| `registracijos_data` | `datetime` | `S` | `4` | `open` | — | Registracijos į stovyklą data | — |
| `vaiko_asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas registruoto vaiko asmens kodas | — |
| `vaiko_lytis` | `string` | — | `4` | `open` | — | Vaiko lytis nustatyta iš asmens kodo | — |
| `vaiko_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Vaiko gimimo metais nustatyti iš asmens kodo | — |
| `stovyklos_kategorija` | `string` | — | `4` | `open` | — | Stovyklos sezono pavadinimas | — |
| `teikejo_stovyklos_id` | `string` | — | `4` | `open` | — | Stovyklos organizatoriaus identifikatorius | — |
| `teikejo_stovyklos_pavadinimas` | `string` | — | `4` | `open` | — | Stovyklos organizatoriaus ir stovyklos pavadinimas | — |
| `stovyklos_adresas` | `string` | — | `4` | `open` | — | Stovyklos adresas | — |
| `stovyklos_koord` | `geometry(point, 3346)` | — | `4` | `open` | — | Stovyklos koordinatės | — |
| `stovyklos_tipas` | `string` | — | `4` | `open` | — | Stovyklos tipas | — |
| `registracijos_pradzia` | `date` | `D` | `4` | `open` | — | Registracijos į stovyklą pradžios data | — |
| `registracijos_pabaiga` | `date` | `D` | `4` | `open` | — | Registracijos į stovyklą pabaigos data | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Stovyklos amžiaus grupė | — |
| `pamainos_id` | `string` | — | `4` | `open` | — | Stovyklos pamainos identifikatorius | — |
| `pamainos_pavadinimas` | `string` | — | `4` | `open` | — | Stovyklos pamainos pavadinimas | — |
| `pamainos_pradzia` | `date` | `D` | `4` | `open` | — | Stovyklos pamainos pradžia | — |
| `pamainos_pabaiga` | `date` | `D` | `4` | `open` | — | Stovyklos pamainos pabaiga | — |
| `uzimtumo_pradzia` | `string` | — | `4` | `open` | — | Vaikų užimtumo stovykloje pradžios laikas | — |
| `uzimtumo_pabaiga` | `string` | — | `4` | `open` | — | Vaikų užimtumo stovykloje pabaigos laikas | — |
| `vietu_sk` | `integer` | — | `4` | `open` | — | Vietų skaičius stovykloje | — |
| `proc40` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, kad 40 proc. stovyklos kainos finansuoja Savivaldybė | Požymis, nurodantis, kad 40 proc. stovyklos kainos finansuoja Savivaldybė, o likusią dalį tėvai, (globėjai, rūpintojai) ar iš kitų finansavimo šaltinių."TRUE" - savivaldybė iš dalies finansuoja vienam vaikui tik vieną pasirinktą stovyklą, nepriklausomai nuo jų tipo, per metus |
| `proc80` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, kad 80 proc. stovyklos kainos finansuoja Savivaldybė | Požymis, nurodantis, kad 80 proc. stovyklos kainos finansuoja Savivaldybė, o likusią dalį tėvai, (globėjai, rūpintojai) ar iš kitų finansavimo šaltinių. "TRUE" - vaikas, esantis jautresnėje socialinėje situacijoje |
| `patvirtinta_registracija` | `boolean` | — | `4` | `open` | — | Patvirtinos registracijos požymis | — |
| `istrinta_registracija` | `boolean` | — | `4` | `open` | — | Vaiko registracijos stovykloje atšaukimo požymis | — |
| `patvirtintos_reigstracijos_data` | `datetime` | `S` | `4` | `open` | — | Patvirtintos registracijos požymio data | — |
| `savivaldybes_kompensacija_eur` | `number` | — | `4` | `open` | — | Savivaldybės kompensacijos dydis eurais | Savivaldybės kompensacijos dydis eurais, kuris yra 40 proc. arba 80 proc. nuo pilnos stovyklos kainos. Kopensacijos dydis nustatomas pagal jautresnės socialinės aplinkos požymį |
| `paslaugos_gavejo_mokestis_eur` | `number` | — | `4` | `open` | — | Kaina tėvams po 40 proc. arba 80 proc. kompensacijos | — |
| `apklausa_issiusta` | `boolean` | — | `4` | `open` | — | Išsiųstos apklausos po stovyklos požymis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv
