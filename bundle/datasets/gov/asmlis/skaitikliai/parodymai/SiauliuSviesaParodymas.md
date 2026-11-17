---
type: Table
title: "SiauliuSviesaParodymas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šiaulių šviesa“ skaitiklių parodymų įrašai."
description: "Spinta table datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas"
tags: [gov, asmlis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# SiauliuSviesaParodymas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šiaulių šviesa“ skaitiklių parodymų įrašai.

- **Model:** `datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai.](../parodymai.md) (`datasets/gov/asmlis/skaitikliai/parodymai`)
- **Manifest CSV:** [datasets/gov/asmlis/skaitikliu_parodymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus lentelės raktas | — |
| `skaitliuko_id` | `string` | — | `4` | `open` | — | Skaitiklio identifikatorius | — |
| `skaitliuko_tipas` | `string` | — | `4` | `open` | — | Skaitiklio tipas | — |
| `periodas` | `date` | `D` | `4` | `open` | — | Deklaruotų duomenų periodas | — |
| `nuo` | `number` | — | `4` | `open` | — | Data nuo | — |
| `iki` | `number` | — | `4` | `open` | — | Data iki | — |
| `skirtumas` | `number` | — | `4` | `open` | — | Skirtumas | — |
| `matavimo_vienetai` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv
