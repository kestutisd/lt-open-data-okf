---
type: Table
title: "SuteiktaPaslauga — Informacija apie suteiktas prekes ir paslaugas"
description: "Informacija apie Viešosios įstaigos Palangos vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientams suteiktas prekes ir paslaugas nuo 2023 metų."
resource: "https://get.data.gov.lt/datasets/gov/palangos_gintaras/suteiktos_paslaugos/SuteiktaPaslauga"
tags: [gov, palangos_gintaras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/palangos_gintaras/suteiktos_paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/suteiktos_paslaugos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# SuteiktaPaslauga — Informacija apie suteiktas prekes ir paslaugas

Informacija apie Viešosios įstaigos Palangos vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientams suteiktas prekes ir paslaugas nuo 2023 metų.

- **Model:** `datasets/gov/palangos_gintaras/suteiktos_paslaugos/SuteiktaPaslauga`[^manifest]
- **Dataset:** [Informacija apie suteiktas prekes ir paslaugas](../suteiktos_paslaugos.md) (`datasets/gov/palangos_gintaras/suteiktos_paslaugos`)
- **Manifest CSV:** [datasets/gov/palangos_gintaras/suteiktos_paslaugos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/suteiktos_paslaugos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/palangos_gintaras/suteiktos_paslaugos/SuteiktaPaslauga`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA sukurtas šifruotas sąskaitos eilutės unikalus numeris | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Iš užšifruotų paciento asmens duomenų sugeneruotas paciento identifikatorius | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `paciento_atstovo_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento atstovo gimimo metai | — |
| `sask_nr` | `string` | — | `4` | `open` | — | Šifruotas sąskaitos numeris | — |
| `saskaitos_israsymo_data` | `date` | `D` | `4` | `open` | — | Sąskaitos išrašymo data | — |
| `saskaita_issiusta` | `string` | — | `4` | `open` | — | Sąskaitos išsiuntimo požymis | — |
| `paslaugos_pavadinimas_lt` | `string` | — | `2` | `open` | — | Paslaugos/prekės pavadinimas | — |
| `kaina_su_pvm` | `number` | — | `4` | `open` | — | Prekės / paslaugos vieneto kaina su PVM | — |
| `kiekis` | `number` | — | `4` | `open` | — | Prekių / paslaugų kiekis | — |
| `mato_vienetas` | `string` | — | `4` | `open` | — | Paslaugos / prekės mato vienetas | — |
| `suma_su_pvm` | `number` | — | `4` | `open` | — | Suma su PVM | — |
| `pvm_procentai` | `number` | — | `4` | `open` | — | PVM procentas, kuris taikomas prekei/paslaugai | — |
| `suma_su_pvm_su_nuolaida` | `number` | — | `4` | `open` | — | Suma su PVM su nuolaida | — |
| `valiuta` | `string` | — | `4` | `open` | — | Valiutos kodas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `saskaita_issiusta` | `"Taip"` | — | — | — | — |
| `saskaita_issiusta` | `"Ne"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_pavadinimas_lt` | `update(property: "paslaugos_pavadinimas_lt", type:"text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/palangos_gintaras/suteiktos_paslaugos.csv
