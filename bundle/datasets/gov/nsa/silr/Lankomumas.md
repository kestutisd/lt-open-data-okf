---
type: Table
title: "Lankomumas — Mokinių lankomumas"
description: "Spinta table datasets/gov/nsa/silr/Lankomumas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/silr/Lankomumas"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lankomumas — Mokinių lankomumas

- **Model:** `datasets/gov/nsa/silr/Lankomumas`[^manifest]
- **Dataset:** [Švietimo įstaigų lankomumo rodikliai](../silr.md) (`datasets/gov/nsa/silr`)
- **Manifest CSV:** [datasets/gov/nsa/silr/silr.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/silr/Lankomumas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `atask_laikotarp` | `date` | `M` | `4` | `open` | — | Mėnesinis ataskaitinis laikotarpis | — |
| `ins_kodas` | `string` | — | `4` | `open` | — | Švietimo įstaigos (mokyklos) kodas Juridinių asmenų registre | — |
| `pad_kodas` | `string` | — | `4` | `open` | — | Švietimo ir mokslo institucijų registro institucijos padalinio kodas | — |
| `srautas` | `integer` | — | `4` | `open` | — | Mokinių srautas (1-12 klasės) | — |
| `mokdal_kodas` | `string` | — | `4` | `open` | — | Mokomojo dalyko kodas | — |
| `dienynas` | `string` | — | `4` | `open` | — | Mokyklos naudojamo elektroninio dienyno pavadinimas (NAŠC arba Tamo) | — |
| `nsa_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių skaičius mokykloje pagal NŠA mokinių registro duomenis ataskaitinio laikotarpio pirmą dieną | — |
| `dienyno_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių skaičius nustatytas pagal dienyno įrašus per ataskaitinį mėnesinį laikotarpį, skaičiuojant unikalius mokinius, kurie gavo bent vieną įrašą dienyne (lankomumo įrašą arba pažymį) | — |
| `pateisintu_del_ligos_sk` | `integer` | — | `4` | `open` | — | Pateisintų, dėl ligos, pamokų skaičius | — |
| `pateisintu_del_kita_sk` | `integer` | — | `4` | `open` | — | Pateisintų, dėl kitos priežasties nei ligos | — |
| `nepateisintu_sk` | `integer` | — | `4` | `open` | — | Nepateisintų pamokų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv
