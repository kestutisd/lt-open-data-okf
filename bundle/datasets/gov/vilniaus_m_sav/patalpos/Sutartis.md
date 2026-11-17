---
type: Table
title: "Sutartis — Vilniaus miesto savivaldybės patalpų nuomų sutartys"
description: "Spinta table datasets/gov/vilniaus_m_sav/patalpos/Sutartis (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Sutartis"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L32"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — Vilniaus miesto savivaldybės patalpų nuomų sutartys

- **Model:** `datasets/gov/vilniaus_m_sav/patalpos/Sutartis`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys](../patalpos.md) (`datasets/gov/vilniaus_m_sav/patalpos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L32)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Sutartis`
- **Primary Key (`ref`):** `sutarties_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikacinis numeris | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `aprasymas_lt` | `string` | — | `2` | `open` | — | Veiklos aprašymas | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Pasirašytos sutarties tipas | — |
| `statusas` | `string` | — | `4` | `open` | — | Sutarties statusas | — |
| `sudarymas` | `date` | `D` | `4` | `open` | — | Sutarties sudarymo data | — |
| `naudotoju_sk` | `integer` | `U` | `4` | `open` | — | Veikloje dalyvaujančių asmenų skaičius | — |
| `antroji_salis` | `string` | — | `4` | `open` | — | Sutarties antrosios šalies pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Antrosios šalies JAR kodas | — |
| `jar_kodas_validus` | `boolean` | — | `4` | `open` | — | JAR kodo validacijos požymis | — |
| `nuomos_valandu_sk` | `number` | `h` | `4` | `open` | — | Sutartyje nurodytas patalpų nuomos valandų skaičius | — |
| `nutraukimas` | `date` | `D` | `4` | `open` | — | Jei sutartis buvo nutraukta, nurodoma nutraukimo data | — |
| `kaina_reitingas` | `integer` | — | `4` | `open` | — | Sutartyje nurodyta patalpų kaina neatvaizduojama, tačiau ji išreitinguojama pagal visų rinkinyje nurodytų sutarčių sumas | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Sutarties duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sutarties_tipas` | `"Konkursinė sutartis"` | — | — | — | — |
| `sutarties_tipas` | `"Nuomos sutartis"` | — | — | — | — |
| `sutarties_tipas` | `"Aukcionas"` | — | — | — | — |
| `sutarties_tipas` | `"Panaudos sutartis"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv
