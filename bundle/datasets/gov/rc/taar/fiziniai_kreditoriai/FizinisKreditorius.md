---
type: Table
title: "FizinisKreditorius"
description: "Spinta table datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/fiziniai_kreditoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# FizinisKreditorius

- **Model:** `datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie kreditorius (kreditoriai fiziniai asmenys)](../fiziniai_kreditoriai.md) (`datasets/gov/rc/taar/fiziniai_kreditoriai`)
- **Manifest CSV:** [datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `dokumento_statusas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `ai_tipas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/AI](../klasifikatoriai/AI.md) | `4` | `open` | — | Areštuojančios institucijos tipas iš TAAR areštuojančių institucijų klasifikatoriaus | — |
| `kreditoriausid` | `integer` | — | `4` | `open` | — | Fizinio asmens dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `amzius` | `string` | — | `4` | `open` | — | Fizinio asmens amžiaus grupė | — |
| `ar_uzsienietis` | `integer` | — | `4` | `open` | — | Požymis, ar asmuo įregistruotas Gyventojų registre ( 1 - Taip; 0 - Ne) | — |
| `taa_iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `taa_iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `taa_isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `taa_isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo mėnuo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `amzius` | `"0-24"` | — | — | Kai amžius nuo 0 iki 24 metų | — |
| `amzius` | `"25-34"` | — | — | Kai amžius nuo 25 iki 34 metų | — |
| `amzius` | `"35-44"` | — | — | Kai amžius nuo 35 iki 44 metų | — |
| `amzius` | `"45-54"` | — | — | Kai amžius nuo 45 iki 54 metų | — |
| `amzius` | `"55-64"` | — | — | Kai amžius nuo 55 iki 64 metų | — |
| `amzius` | `"65-84"` | — | — | Kai amžius nuo 65 iki 84 metų | — |
| `amzius` | `"85+"` | — | — | Kai amžius nuo 85 metų | — |
| `amzius` | `"Nenustatyta"` | — | — | Kai amžius nenurodytas | — |
| `ar_uzsienietis` | `1` | — | — | Taip | — |
| `ar_uzsienietis` | `0` | — | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/fiziniai_kreditoriai.csv
