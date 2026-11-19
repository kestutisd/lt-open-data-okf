---
type: Table
title: "FizinisKreditorius"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie kreditorius, kai kreditoriai fiziniai asmenys, jų amžiaus grupę ir pilietybę, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius"
tags: [gov, rc, fiziniskreditorius, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2234/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/fiziniai_kreditoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# FizinisKreditorius

**Dataset Context:** Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie kreditorius, kai kreditoriai fiziniai asmenys, jų amžiaus grupę ir pilietybę, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją.[^manifest]

- **Model:** `datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie kreditorius (kreditoriai fiziniai asmenys)](../fiziniai_kreditoriai.md) (`datasets/gov/rc/taar/fiziniai_kreditoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai/FizinisKreditorius` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `dokumento_statusas` | `ref` | [DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) (`level=4 UUID`: `dokumento_statusas._id`) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `ai_tipas` | `ref` | [AI](../klasifikatoriai/AI.md) (`level=4 UUID`: `ai_tipas._id`) | `4` | `open` | — | Areštuojančios institucijos tipas iš TAAR areštuojančių institucijų klasifikatoriaus | — |
| `kreditoriausid` | `integer` | — | `4` | `open` | — | Fizinio asmens dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `amzius` | `string` | — | `4` | `open` | — | Fizinio asmens amžiaus grupė | — |
| `ar_uzsienietis` | `integer` | — | `4` | `open` | — | Požymis, ar asmuo įregistruotas Gyventojų registre ( 1 - Taip; 0 - Ne) | — |
| `taa_iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `taa_iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `taa_isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `taa_isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo mėnuo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/fiziniai_kreditoriai (https://data.gov.lt/datasets/2234/)
