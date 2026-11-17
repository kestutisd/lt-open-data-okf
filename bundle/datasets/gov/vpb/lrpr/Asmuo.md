---
type: Table
title: "Asmuo — Lietuvoje registruotiems patentams priskirti asmenys"
description: "Lentelė „Lietuvoje registruotiems patentams priskirti asmenys“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr/Asmuo"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# Asmuo — Lietuvoje registruotiems patentams priskirti asmenys

Lentelė „Lietuvoje registruotiems patentams priskirti asmenys“. Lentelę sudaro: patento ir paraiškos numeriai, priskirto juridinio asmens pavadinimas arba fizinio asmens vardas ir pavardė, asmens vaidmuo, kodas, vaidmuo ir tipas patente. Vienas įrašas atitinka vieną unikalią patento numerio, asmens identifikatoriaus ir jo vaidmens patente kombinaciją.

- **Model:** `datasets/gov/vpb/lrpr/Asmuo`[^manifest]
- **Dataset:** [Lietuvos Respublikoje registruoti patentai](../lrpr.md) (`datasets/gov/vpb/lrpr`)
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr/Asmuo`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patento_nr` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Patentui priskirto asmens identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Patentui priskirto fizinio asmens vardas su pavarde arba juridinio asmens pavadinimas | — |
| `asm_kodas` | `string` | — | `4` | `open` | — | Patentui priskirto asmens kodas | — |
| `asmens_vaidmuo_patente` | `string` | — | `4` | `open` | — | Patentui priskirto asmens vaidmuo | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Patentui priskirto asmens tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asmens_vaidmuo_patente` | `"Išradėjas"` | — | — | Išradėjas | — |
| `asmens_vaidmuo_patente` | `"Pareiškėjas"` | — | — | Pareiškėjas | — |
| `asmens_vaidmuo_patente` | `"Savininkas"` | — | — | Savininkas | — |
| `asmens_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `asmens_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv
