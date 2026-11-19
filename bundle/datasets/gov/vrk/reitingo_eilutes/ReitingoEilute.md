---
type: Table
title: "ReitingoEilute"
description: "Spinta table datasets/gov/vrk/reitingo_eilutes/ReitingoEilute (14 columns)."
tags: [gov, vrk, reitingoeilute, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/reitingo_eilutes.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vrk/reitingo_eilutes.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ReitingoEilute

- **Model:** `datasets/gov/vrk/reitingo_eilutes/ReitingoEilute`[^manifest]
- **Dataset:** [datasets/gov/vrk/reitingo_eilutes](../reitingo_eilutes.md) (`datasets/gov/vrk/reitingo_eilutes`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/reitingo_eilutes.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/reitingo_eilutes.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `rink_turo_apyg_id, rink_turo_apyl_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rink_turo_id` | `integer` | — | `4` | `open` | — | Rinkimų turo identifikatorius | — |
| `rink_turo_pavad` | `string` | — | `4` | `open` | — | Rinkimų turo pavadinimas | — |
| `rink_turo_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apygardos identifikatorius | — |
| `rink_turo_apyl_id` | `integer` | — | `4` | `open` | — | Rinkimų turo apylinkės identifikatorius | — |
| `saraso_id` | `integer` | — | `4` | `open` | — | Kandidatų sąrašo (rinkimų organizacijos), keliamo daugiamandatėje apygardoje, identifikatorius | — |
| `saraso_nr` | `integer` | — | `4` | `open` | — | Kandidatų sąrašo numeris | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, numeris |
| `saraso_pavad` | `string` | — | `4` | `open` | — | Kandidatų sąrašo pavadinimas | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, pavadinimas |
| `saraso_ja_kodas` | `string` | — | `4` | `open` | — | Kandidatų sąrašo juridinio asmens kodas Juridinių asmenų registre | — |
| `biul_eiles_nr` | `integer` | — | `4` | `open` | — | Biuletenio eilės numeris | Biuletenio su reitingo balsais eilės numeris |
| `kand_reit_1` | `integer` | — | `4` | `open` | — | Kandidato rinkimų numeris, nurodytas biuletenio 1-ame laukelyje | — |
| `kand_reit_2` | `integer` | — | `4` | `open` | — | Kandidato rinkimų numeris, nurodytas biuletenio 2-ame laukelyje | — |
| `kand_reit_3` | `integer` | — | `4` | `open` | — | Kandidato rinkimų numeris, nurodytas biuletenio 3-iame laukelyje | — |
| `kand_reit_4` | `integer` | — | `4` | `open` | — | Kandidato rinkimų numeris, nurodytas biuletenio 4-ame laukelyje | — |
| `kand_reit_5` | `integer` | — | `4` | `open` | — | Kandidato rinkimų numeris, nurodytas biuletenio 5-ame laukelyje | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/reitingo_eilutes.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/reitingo_eilutes.csv#L4)
