---
type: Table
title: "Averages — Valandiniai oro kokybės matavimai"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Averages (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# Averages — Valandiniai oro kokybės matavimai

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Averages`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Matavimo identifikacinis numeris | — |
| `stat_num` | `ref` | [/datasets/gov/aaa/oro_stociu_matavimai/Station[stat_num]](Station.md) | `4` | `open` | — | Matavimo stoties identifikacinis numeris | — |
| `ldatetime` | `datetime` | `S` | `4` | `open` | — | Matavimo pabaigos laikas | — |
| `code_combi` | `string` | — | `4` | `open` | — | Tarpinės lentos kodas | Juo prie matavimo prijungiamas teršalo arba meteorologinio parametro pavadinimas ir matavimo vienetas |
| `lvalue` | `number` | — | `4` | `open` | — | Išmatuota vertė arba teršalo koncentracija | — |
| `atribut` | `integer` | — | `4` | `open` | — | Atlikto matavimo verifikacija | Verifikaciją (atlikto matavimo kokybės patvirtinimą) atlieka AAA specialistai |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv
