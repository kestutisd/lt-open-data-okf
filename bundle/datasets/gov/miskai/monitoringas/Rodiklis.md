---
type: Table
title: "Rodiklis — Miškų sveikumo monitoringo duomenys"
description: "Spinta table datasets/gov/miskai/monitoringas/Rodiklis (21 columns)."
tags: [gov, miskai, rodiklis, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/monitoringas.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/miskai/monitoringas.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rodiklis — Miškų sveikumo monitoringo duomenys

- **Model:** `datasets/gov/miskai/monitoringas/Rodiklis`[^manifest]
- **Dataset:** [datasets/gov/miskai/monitoringas](../monitoringas.md) (`datasets/gov/miskai/monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/monitoringas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/monitoringas.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `barnr` | `string` | — | `4` | `open` | — | Barelio numeris | — |
| `task` | `integer` | — | `2` | `open` | — | Barelio padėtis | — |
| `mnr` | `integer` | — | `4` | `open` | — | Medžio numeris | — |
| `mrr` | `string` | — | `3` | `open` | — | Medžio rūšis | — |
| `buk` | `integer` | — | `4` | `open` | — | Medžio būklė, padaringumas | — |
| `kraft` | `integer` | — | `4` | `open` | — | Medžio krafto klasė | — |
| `perim` | `integer` | — | `3` | `open` | — | Medžio stiebo perimetras 1,3 m aukštyje nuo šaknies kaklelio | — |
| `vbuk` | `string` | — | `2` | `open` | — | Viršūnės būklė | — |
| `sausu` | `integer` | — | `4` | `open` | — | Sausų šakų kiekis | — |
| `derej` | `integer` | — | `4` | `open` | — | Derėjimo laipsnis | Derėjimo laipsnis pušims ir eglėms |
| `spamz` | `number` | — | `3` | `open` | — | Spyglių amžius | Spyglių amžius pušims |
| `lpaz` | `integer` | — | `4` | `open` | — | Lajos pažeidimo tipas | — |
| `def13` | `integer` | — | `4` | `open` | — | Viršutinio lajos trečdalio defoliacija | — |
| `defol` | `integer` | — | `4` | `open` | — | Visos lajos defoliacija | — |
| `dechr` | `integer` | — | `4` | `open` | — | Visos lajos dechromacija | — |
| `viet1` | `integer` | — | `4` | `open` | — | Pažeidimų vieta medyje | — |
| `viet2` | `integer` | — | `4` | `open` | — | Pažeidimų vieta medyje | — |
| `paz1` | `integer` | — | `4` | `open` | — | Pažeidimų pavadinimas | — |
| `paz2` | `integer` | — | `4` | `open` | — | Pažeidimų pavadinimas | — |
| `int1` | `integer` | — | `4` | `open` | — | Pažeidimų intensyvumas | — |
| `int2` | `integer` | — | `4` | `open` | — | Pažeidimų intensyvumas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `task` | `1` | — | — | šiaurė | — |
| `task` | `2` | — | — | rytai | — |
| `task` | `3` | — | — | pietūs | — |
| `task` | `4` | — | — | vakarai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/monitoringas.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/monitoringas.csv#L8)
