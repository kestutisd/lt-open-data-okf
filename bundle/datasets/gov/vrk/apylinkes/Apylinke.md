---
type: Table
title: "Apylinke"
description: "Spinta table datasets/gov/vrk/apylinkes/Apylinke (30 columns)."
tags: [gov, vrk, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/apylinkes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/apylinkes.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apylinke

- **Model:** `datasets/gov/vrk/apylinkes/Apylinke`[^manifest]
- **Dataset:** [datasets/gov/vrk/apylinkes](../apylinkes.md) (`datasets/gov/vrk/apylinkes`)
- **Manifest CSV:** [datasets/gov/vrk/apylinkes.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/apylinkes.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `rink_apyl_id, apyl_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rink_rusies_kodas` | `string` | — | `4` | `open` | — | Rinkimų rūšies kodas | — |
| `rinkimu_id` | `integer` | — | `4` | `open` | — | Rinkimų ID | — |
| `vykd_rink_id` | `integer` | — | `4` | `open` | — | Vykdomųjų rinkimų ID | — |
| `vykd_rink_turo_id` | `integer` | — | `4` | `open` | — | Vykdomųjų rinkimų turo ID | — |
| `vykd_rink_turo_pavad` | `string` | — | `4` | `open` | — | Vykdomųjų rinkimų turo pavadinimas | — |
| `rink_turo_nr` | `integer` | — | `4` | `open` | — | Rinkimų turas | — |
| `rink_turo_id` | `integer` | — | `4` | `open` | — | Rinkimų turo ID | — |
| `rink_turo_pavad` | `string` | — | `4` | `open` | — | Rinkimų turo pavadinimas | — |
| `rink_turo_data` | `datetime` | `D` | `4` | `open` | — | Rinkimų turo data | — |
| `rink_turo_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apygardos ID | — |
| `rink_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų apygardos identifikatorius | — |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |
| `valstybes_kodas` | `string` | — | `4` | `open` | — | Valstybės kodas | — |
| `valstybe` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `rink_turo_apyl_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apylinkės ID | — |
| `rink_apyl_id` | `integer` | — | `4` | `open` | — | Rinkimų apylinkės identifikatorius | — |
| `apyl_id` | `integer` | — | `4` | `open` | — | Apylinkės identifikatorius | — |
| `apyl_unik_nr` | `integer` | — | `4` | `open` | — | Unikalus apylinkės numeris | — |
| `apyl_nr` | `integer` | — | `4` | `open` | — | Apylinkės numeris | — |
| `apyl_pavad` | `string` | — | `4` | `open` | — | Apylinkės pavadinimas | — |
| `bust_adresas` | `string` | — | `4` | `open` | — | Apylinkės būstinės adresas | — |
| `bust_x` | `integer` | — | `4` | `open` | — | Būstinės/balsavimo adreso X koordinatė | — |
| `bust_y` | `integer` | — | `4` | `open` | — | Būstinės/balsavimo adreso Y koordinatė | — |
| `pritaikyta_neigaliesiems` | `string` | — | `4` | `open` | — | Pritaikyta neįgaliems | — |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `rinkeju_sarase` | `integer` | `U` | `4` | `open` | — | Rinkėjų skaičius sąraše | — |
| `rinkeju_skaicius` | `integer` | `U` | `4` | `open` | — | Galutinis rinkėjų skaičius balsų skaičiavimo protokole | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/apylinkes.csv
