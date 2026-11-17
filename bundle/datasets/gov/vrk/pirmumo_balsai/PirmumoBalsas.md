---
type: Table
title: "PirmumoBalsas"
description: "Spinta table datasets/gov/vrk/pirmumo_balsai/PirmumoBalsas (28 columns)."
tags: [gov, vrk, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/pirmumo_balsai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/pirmumo_balsai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PirmumoBalsas

- **Model:** `datasets/gov/vrk/pirmumo_balsai/PirmumoBalsas`[^manifest]
- **Dataset:** [datasets/gov/vrk/pirmumo_balsai](../pirmumo_balsai.md) (`datasets/gov/vrk/pirmumo_balsai`)
- **Manifest CSV:** [datasets/gov/vrk/pirmumo_balsai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/pirmumo_balsai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `pirm_balai_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pirm_balai_id` | `integer` | — | `4` | `open` | — | Unikalus ID | — |
| `rink_turo_id` | `integer` | — | `4` | `open` | — | Rinkimų turo identifikatorius | — |
| `rink_turo_pavad` | `string` | — | `4` | `open` | — | Rinkimų turo pavadinimas | — |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |
| `rink_turo_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apygardos identifikatorius | — |
| `rink_turo_apyl_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apylinkės identifikatorius | — |
| `apyl_id` | `integer` | — | `4` | `open` | — | Apylinkės identifikatorius | — |
| `apyl_unik_nr` | `integer` | — | `4` | `open` | — | Unikalus apylinkės numeris | — |
| `apyl_nr` | `integer` | — | `4` | `open` | — | Apylinkės numeris | — |
| `apyl_pavad` | `string` | — | `4` | `open` | — | Apylinkės pavadinimas | — |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `rinkeju_skaicius` | `integer` | `U` | `4` | `open` | — | Galutinis rinkėjų skaičius balsų skaičiavimo protokole | — |
| `viso_dalyvavo` | `integer` | `U` | `4` | `open` | — | Rinkimuose dalyvavusių rinkėjų skaičius | — |
| `saraso_id` | `integer` | — | `4` | `open` | — | Kandidatų sąrašo (rinkimų organizacijos), keliamo daugiamandatėje apygardoje identifikatorius | — |
| `saraso_nr` | `integer` | — | `4` | `open` | — | Kandidatų sąrašo numeris | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, numeris |
| `saraso_pavad` | `string` | — | `4` | `open` | — | Kandidatų sąrašo pavadinimas | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, pavadinimas |
| `saraso_ja_kodas` | `string` | — | `4` | `open` | — | Kandidatų sąrašo juridinio asmens kodas Juridinių asmenų registre | — |
| `balsai` | `integer` | `U` | `4` | `open` | — | Kandidatų sąrašo gautų balsų skaičius | — |
| `mandatai` | `integer` | `U` | `4` | `open` | — | Kandidatų sąrašo gautų mandatų skaičius | — |
| `kand_porink_nr` | `integer` | — | `4` | `open` | — | Kandidato numeris kandidatų sąraše po rinkimų | — |
| `kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius | Kandidato ID |
| `vardas` | `string` | — | `4` | `open` | — | Kandidato vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Kandidato pavardė | — |
| `kand_nr_sarase` | `integer` | — | `4` | `open` | — | Kandidato eilės numeris kandidatų sąraše iki rinkimų | — |
| `pirmumo_balai` | `integer` | — | `4` | `open` | — | Kandidato gautų pirmumo balsų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gpv/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `sav_pavadinimas` | `update(property: "savivaldybe.sav_pavadinimas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/pirmumo_balsai.csv
