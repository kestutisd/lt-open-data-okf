---
type: Table
title: "TersaluKiekis — Nuotekų kiekiai pagal rodiklius po valymo"
description: "Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ Nuotekų valymo registre kaupiamos užterštumo rodiklių reikšmės po valymo."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_po_valymo/TersaluKiekis"
tags: [gov, simno_komun, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/nvr_po.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nvr_po.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TersaluKiekis — Nuotekų kiekiai pagal rodiklius po valymo

Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ Nuotekų valymo registre kaupiamos užterštumo rodiklių reikšmės po valymo. Duomenų rinkinys laikinai apima tik 2023 m., tačiau yra numatyta įtraukti ir nuo 2018 m. sukauptus duomenis ir atnaujinti rinkinį kas 6 mėnesius. Duomenų rinkinį sudaro: valymo įrenginio pavadinimas, užterštumo rodiklių pavadinimai ir rodiklių reikšmės bei pirmųjų pusmečių dienų datos, kada buvo matuotas užterštumas. Duomenų rinkinys yra ilgo formato, todėl vieno valymo įrenginio duomenys išdėstyti vertikaliai.

- **Model:** `datasets/gov/simno_komun/tersalai_po_valymo/TersaluKiekis`[^manifest]
- **Dataset:** [Nuotekų kiekiai pagal rodiklius po valymo](../tersalai_po_valymo.md) (`datasets/gov/simno_komun/tersalai_po_valymo`)
- **Manifest CSV:** [datasets/gov/simno_komun/nvr_po.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nvr_po.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_po_valymo/TersaluKiekis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `irenginys` | `string` | — | `4` | `open` | — | Valymo įrenginys | — |
| `rodiklis` | `string` | — | `4` | `open` | — | Matuojamas rodiklis | — |
| `data` | `date` | `D` | `4` | `open` | — | Pusmečio pirmoji diena | — |
| `reiksme` | `number` | — | `4` | `open` | — | Rodiklio užfiksuota reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/nvr_po.csv
