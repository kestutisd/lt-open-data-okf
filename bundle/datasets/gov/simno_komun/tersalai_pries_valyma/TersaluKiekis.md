---
type: Table
title: "TersaluKiekis — Teršalų, išleidžiamų su nuotekomis, metinis kiekis"
description: "Lentelėje pateikti metiniai skirtingų nuotekų valymo įrenginių teršalų koncentracijų prieš valymą duomenys iš Alytaus rajono SĮ „Simno komunalininkas“ Nuotekų prieš valymą registro."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_pries_valyma/TersaluKiekis"
tags: [gov, simno_komun, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/tersalai_pries_valyma.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/tersalai_pries_valyma.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TersaluKiekis — Teršalų, išleidžiamų su nuotekomis, metinis kiekis

Lentelėje pateikti metiniai skirtingų nuotekų valymo įrenginių teršalų koncentracijų prieš valymą duomenys iš Alytaus rajono SĮ „Simno komunalininkas“ Nuotekų prieš valymą registro. Duomenys renkami nuo 2018 m. ir yra atnaujinami kas metus.

- **Model:** `datasets/gov/simno_komun/tersalai_pries_valyma/TersaluKiekis`[^manifest]
- **Dataset:** [Teršalų, išleidžiamų su nuotekomis, metinis kiekis](../tersalai_pries_valyma.md) (`datasets/gov/simno_komun/tersalai_pries_valyma`)
- **Manifest CSV:** [datasets/gov/simno_komun/tersalai_pries_valyma.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/tersalai_pries_valyma.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/tersalai_pries_valyma/TersaluKiekis`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Ataskaitos data nuo | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Ataskaitos data iki | — |
| `nuoteku_valymo_irenginys` | `string` | — | `4` | `open` | — | Nuotekų valymo įrenginys | — |
| `skend_medz` | `number` | `mg/l` | `4` | `open` | — | Skend. Medž., mg/l | — |
| `chdsmn` | `number` | — | `4` | `open` | — | ChDSMn, mgO2/l | — |
| `bds7` | `number` | — | `4` | `open` | — | BDS7, mgO2/l | — |
| `chloridai` | `number` | `mg/l` | `4` | `open` | — | Chloridai, mg/l | — |
| `naft_prod` | `number` | `mg/l` | `4` | `open` | — | Naft. prod., mg/l | — |
| `amonis` | `number` | — | `4` | `open` | — | Amonis, mgN/l | — |
| `nitratai` | `number` | — | `4` | `open` | — | Nitratai, mgN/l | — |
| `nitritai` | `number` | — | `4` | `open` | — | Nitritai, mgN/l | — |
| `fosfatai` | `number` | — | `4` | `open` | — | Fosfatai, mgP/l | — |
| `bendras_azotas` | `number` | — | `4` | `open` | — | Bendras azotas, mgN/l | — |
| `bendras_fosforas` | `number` | — | `4` | `open` | — | Bendras fosforas, mgP/l | — |
| `anijonines_pam` | `number` | `mg/l` | `4` | `open` | — | Anijoninės PAM, mg/l | — |
| `viso_per_metus_kg` | `number` | `kg` | `4` | `open` | — | Viso per metus, kg | — |
| `viso_per_metus_t` | `number` | `t` | `4` | `open` | — | Viso per metus, t | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/tersalai_pries_valyma.csv
