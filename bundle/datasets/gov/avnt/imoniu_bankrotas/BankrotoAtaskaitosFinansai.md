---
type: Table
title: "BankrotoAtaskaitosFinansai — Įmonių bankroto ataskaitų duomenų finansiniai duomenys"
description: "Spinta table datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosFinansai (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosFinansai"
tags: [gov, avnt, bankrotoataskaitosfinansai, deployed, level-3, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L51"
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_bankrotas.csv#L51"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1979/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_bankrotas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# BankrotoAtaskaitosFinansai — Įmonių bankroto ataskaitų duomenų finansiniai duomenys

- **Model:** `datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosFinansai`[^manifest]
- **Dataset:** [Įmonių bankroto ataskaitų duomenys](../imoniu_bankrotas.md) (`datasets/gov/avnt/imoniu_bankrotas`)[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/imoniu_bankrotas.csv#L51](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L51)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosFinansai` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilutės numeris | — |
| `bankroto_metai` | `integer` | — | `2` | `open` | — | Bankroto pradžios metai | — |
| `turtas_proceso_pradzioje` | `number` | — | `2` | `open` | — | Turtas proceso pradžioje | — |
| `turtas_laikotarpio_pabaigoje` | `number` | — | `2` | `open` | — | Turtas ataskaitinio laikotarpio pabaigoje | — |
| `visi_kreditoriu_reikalavimai` | `number` | — | `2` | `open` | — | Visi kreditorių reikalavimai | — |
| `visi_patenkinti_reikalavimai` | `number` | — | `2` | `open` | — | Iš viso patenkinti kreditorių reikalavimai | — |
| `reikalavimai_laikotarpio_pabaigoje` | `number` | — | `2` | `open` | — | Kreditorių reikalavimai ataskaitinio laikotarpio pabaigoje | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "eil_nr")` | `ref` | `4` | `open` | — | — | — |
| `bankroto_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `turtas_proceso_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `turtas_laikotarpio_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `visi_kreditoriu_reikalavimai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `visi_patenkinti_reikalavimai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `reikalavimai_laikotarpio_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_bankrotas.csv#L51 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L51)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_bankrotas (https://data.gov.lt/datasets/1979/)
