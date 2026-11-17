---
type: Table
title: "UkioSektoriai — Ūkio sektoriai"
description: "Spinta table datasets/gov/aaa/oro_tersalu_duomenys/UkioSektoriai (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys/UkioSektoriai"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L16"
    last_modified: "2026-11-11T14:39:20Z"
---

# UkioSektoriai — Ūkio sektoriai

- **Model:** `datasets/gov/aaa/oro_tersalu_duomenys/UkioSektoriai`[^manifest]
- **Dataset:** [datasets/gov/aaa/oro_tersalu_duomenys](../oro_tersalu_duomenys.md) (`datasets/gov/aaa/oro_tersalu_duomenys`)
- **Manifest CSV:** [datasets/gov/aaa/oro_tersalu_duomenys.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L16)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys/UkioSektoriai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nfr_kodas` | `ref` | [IAtmosferaIsmetamiTersalai](IAtmosferaIsmetamiTersalai.md) | `4` | `open` | — | Teršalų išmetimo šaltinis | Kodiniai teršalų išmetimo šaltinių pavadinimai. NFR kodai ir metodologija, pagal kurią atliekami skaičiavimai yra nurodyti EMEP/EEA Emission inventory guidebook. |
| `ukio_sektorius` | `string` | — | `4` | `open` | — | Ūkio sektorius | Išmetimo šaltinio kodų paaiškinimas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv
