---
type: Table
title: "Averages — Valandiniai oro kokybės matavimai"
description: "Spinta table datasets/gov/aaa/oro_stociu_matavimai/Averages (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages"
tags: [gov, aaa, averages, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L22"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L22"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/500/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Averages — Valandiniai oro kokybės matavimai

- **Model:** `datasets/gov/aaa/oro_stociu_matavimai/Averages`[^manifest]
- **Dataset:** [Lietuvos valstybinio oro monitoringo automatinių stočių matavimo duomenys](../oro_stociu_matavimai.md) (`datasets/gov/aaa/oro_stociu_matavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_stociu_matavimai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L22)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_stociu_matavimai/Averages` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Matavimo identifikacinis numeris | — |
| `stat_num` | `ref` | [Station](Station.md) (`level=4 UUID` via `Station[stat_num]`: `stat_num._id`) | `4` | `open` | — | Matavimo stoties identifikacinis numeris | — |
| `ldatetime` | `datetime` | `S` | `4` | `open` | — | Matavimo pabaigos laikas | — |
| `code_combi` | `string` | — | `4` | `open` | — | Tarpinės lentos kodas | Juo prie matavimo prijungiamas teršalo arba meteorologinio parametro pavadinimas ir matavimo vienetas |
| `lvalue` | `number` | — | `4` | `open` | — | Išmatuota vertė arba teršalo koncentracija | — |
| `atribut` | `integer` | — | `4` | `open` | — | Atlikto matavimo verifikacija | Verifikaciją (atlikto matavimo kokybės patvirtinimą) atlieka AAA specialistai |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_stociu_matavimai.csv#L22 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_stociu_matavimai.csv#L22)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_stociu_matavimai (https://data.gov.lt/datasets/500/)
