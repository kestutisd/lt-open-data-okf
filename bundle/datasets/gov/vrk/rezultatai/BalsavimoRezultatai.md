---
type: Table
title: "BalsavimoRezultatai"
description: "Spinta table datasets/gov/vrk/rezultatai/BalsavimoRezultatai (30 columns)."
tags: [gov, vrk, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rezultatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rezultatai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# BalsavimoRezultatai

- **Model:** `datasets/gov/vrk/rezultatai/BalsavimoRezultatai`[^manifest]
- **Dataset:** [datasets/gov/vrk/rezultatai](../rezultatai.md) (`datasets/gov/vrk/rezultatai`)
- **Manifest CSV:** [datasets/gov/vrk/rezultatai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rezultatai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `kandidato_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `protokolo_id` | `integer` | — | `4` | `open` | — | Protokolo identifikatorius | — |
| `rink_turo_id` | `integer` | — | `4` | `open` | — | Rinkimų turo identifikatorius | — |
| `rink_turo_pavad` | `string` | — | `4` | `open` | — | Rinkimų turo pavadinimas | — |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |
| `rink_turo_apyl_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apylinkės identifikatorius | — |
| `apyl_id` | `integer` | — | `4` | `open` | — | Apylinkės identifikatorius | — |
| `apyl_unik_nr` | `integer` | — | `4` | `open` | — | Unikalus apylinkės numeris | — |
| `apyl_nr` | `integer` | — | `4` | `open` | — | Apylinkės numeris | — |
| `apyl_pavad` | `string` | — | `4` | `open` | — | Apylinkės pavadinimas | — |
| `rinkeju_skaicius` | `integer` | `U` | `4` | `open` | — | Galutinis rinkėjų skaičius balsų skaičiavimo protokole | Rinkėjų skaičius, nurodytas patvirtintame apylinkės balsų skaičiavimo protokole, t. y. pasibaigus balsavimui rinkimų dieną. |
| `viso_dalyvavo` | `integer` | `U` | `4` | `open` | — | Rinkimuose dalyvavusių rinkėjų skaičius | — |
| `balsad_galioj` | `integer` | `U` | `4` | `open` | — | Galiojančių biuletenių skaičius balsadėžėje | — |
| `balsad_negal` | `integer` | `U` | `4` | `open` | — | Negaliojančių biuletenių skaičius balsadėžėje | — |
| `pastu_galioj` | `integer` | `U` | `4` | `open` | — | Galiojančių biuletenių skaičius paštu | — |
| `pastu_negal` | `integer` | `U` | `4` | `open` | — | Negaliojančių biuletenių skaičius paštu | — |
| `kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius | — |
| `rink_kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius rinkimuose | — |
| `vardas` | `string` | — | `4` | `open` | — | Kandidato vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Kandidato pavardė | — |
| `kandidata_iskele` | `string` | — | `4` | `open` | — | Kandidatą vienmandatėje apygardoje iškėlusios (-ių) organizacijos (-ų) pavadinimas (-ai) ir/ar kandidatas išsikėlė pats. | *atskiriama kabliataškiais |
| `saraso_id` | `integer` | — | `4` | `open` | — | Kandidatų sąrašo (rinkimų organizacijos), keliamo daugiamandatėje apygardoje identifikatorius | — |
| `saraso_nr` | `integer` | — | `4` | `open` | — | Kandidatų sąrašo numeris | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje numeris |
| `saraso_pavad` | `string` | — | `4` | `open` | — | Kandidatų sąrašo pavadinimas | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, pavadinimas |
| `balsu_balsad` | `integer` | `U` | `4` | `open` | — | Balsų skaičius balsadėžėje | Kandidato/Kandidatų sąrašo gautų balsų skaičius balsadėžėje |
| `balsu_pastu` | `integer` | `U` | `4` | `open` | — | Balsų, paduotų balsavimo vokais, skaičius | Kandidato/Kandidatų sąrašo gautų balsų skaičius balsavimo vokais (paštu) |
| `balsu_viso` | `integer` | `U` | `4` | `open` | — | Balsų skaičius iš viso | Kandidato/Kandidatų sąrašo gautų balsų skaičius rinkimų apylinkėje iš viso |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gpv/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `sav_pavadinimas` | `update(property: "savivaldybe.sav_pavadinimas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rezultatai.csv
