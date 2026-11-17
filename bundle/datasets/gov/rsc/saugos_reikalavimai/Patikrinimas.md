---
type: Table
title: "Patikrinimas — Saugos reikalavimų vykdymo patikrinimai"
description: "Spinta table datasets/gov/rsc/saugos_reikalavimai/Patikrinimas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/saugos_reikalavimai/Patikrinimas"
tags: [gov, rsc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsc/saugos_reikalavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/saugos_reikalavimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patikrinimas — Saugos reikalavimų vykdymo patikrinimai

- **Model:** `datasets/gov/rsc/saugos_reikalavimai/Patikrinimas`[^manifest]
- **Dataset:** [datasets/gov/rsc/saugos_reikalavimai](../saugos_reikalavimai.md) (`datasets/gov/rsc/saugos_reikalavimai`)
- **Manifest CSV:** [datasets/gov/rsc/saugos_reikalavimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/saugos_reikalavimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/saugos_reikalavimai/Patikrinimas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `akto_data` | `date` | `D` | `4` | `open` | — | Patikrinimo akto data | — |
| `skyriaus_id` | `string` | — | `2` | `open` | — | Patikrinimą atlikusio RSC skyriaus identifikatorius | — |
| `akto_nr` | `string` | — | `4` | `open` | — | Patikrinimo akto pilnas numeris | — |
| `tipas` | `string` | — | `2` | `open` | — | Patikrinimo tipas | — |
| `ar_planinis` | `boolean` | — | `4` | `open` | — | Požymis, ar patikrinimas planinis | — |
| `parengta` | `date` | `D` | `4` | `open` | — | Patikrinimo akto parengimo data | — |
| `radiologinis` | `boolean` | — | `4` | `open` | — | Patikrinimo atlikimo su radiologiniais tyrimais požymis | — |
| `veiklos_id` | `string` | — | `2` | `open` | — | Asmens padalinio veiklos identifikatorius | — |
| `rusies_id` | `string` | — | `2` | `open` | — | Asmens padalinio veiklos rūšies identifikatorius | — |
| `sritis` | `string` | — | `3` | `open` | — | Veiklos srities pavadinimas | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `org_pav` | `string` | — | `1` | `open` | — | Juridinio asmens pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Pilnas adresas | — |
| `miesto_pozymis` | `boolean` | — | `4` | `open` | — | Požymis ar miestas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Juridinio asmens koordinatės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `skyriaus_id` | `"33"` | — | — | Vilnius | — |
| `skyriaus_id` | `"34"` | — | — | Kaunas | Aktyvus iki 2019-12-30 |
| `skyriaus_id` | `"35"` | — | — | Klaipėda | Aktyvus iki 2019-12-31 |
| `skyriaus_id` | `"36"` | — | — | Panevėžys | — |
| `skyriaus_id` | `"37"` | — | — | Šiauliai | Aktyvus iki 2019-12-31 |
| `skyriaus_id` | `"38"` | — | — | VATESI | Nebegalioja |
| `skyriaus_id` | `"43"` | — | — | AVMS | Aktyvus nuo 2022-01-01 |
| `tipas` | `"1"` | — | — | Operatyvinis | — |
| `tipas` | `"2"` | — | — | Tikslinis | — |
| `tipas` | `"3"` | — | — | Kompleksinis | — |
| `tipas` | `"10"` | — | — | Planinis - Pranešta | — |
| `tipas` | `"11"` | — | — | Planinis - Nepranešta | — |
| `tipas` | `"12"` | — | — | Neplaninis - Pranešta | — |
| `tipas` | `"13"` | — | — | Neplaninis - Nepranešta | — |
| `veiklos_id` | `"36"` | — | — | Medicina | — |
| `veiklos_id` | `"37"` | — | — | Pramonė | — |
| `veiklos_id` | `"38"` | — | — | Mokslas ir mokymas | — |
| `veiklos_id` | `"39"` | — | — | Kita | — |
| `veiklos_id` | `"40"` | — | — | Mišri | — |
| `veiklos_id` | `"41"` | — | — | Nežinoma | — |
| `rusies_id` | `"74"` | — | — | Rentgenodiagnostika | — |
| `rusies_id` | `"75"` | — | — | Spindulinė terapija | — |
| `rusies_id` | `"76"` | — | — | Branduolinė medicina | — |
| `rusies_id` | `"77"` | — | — | Gamyba | — |
| `rusies_id` | `"78"` | — | — | Radiografija | — |
| `rusies_id` | `"79"` | — | — | Matavimai, bandymai ir tyrimai | — |
| `rusies_id` | `"80"` | — | — | Branduolinė energetika | — |
| `rusies_id` | `"81"` | — | — | Paslaugos | — |
| `rusies_id` | `"82"` | — | — | Kontrolė | — |
| `rusies_id` | `"83"` | — | — | Kita | — |
| `rusies_id` | `"84"` | — | — | Mišri | — |
| `rusies_id` | `"85"` | — | — | Nežinoma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/saugos_reikalavimai.csv
