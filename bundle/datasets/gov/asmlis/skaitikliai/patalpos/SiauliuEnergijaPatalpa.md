---
type: Table
title: "SiauliuEnergijaPatalpa — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” AB „Šiaulių energija“ patalpų įrašai."
description: "Spinta table datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa"
tags: [gov, asmlis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L60"
    last_modified: "2026-11-11T14:39:20Z"
---

# SiauliuEnergijaPatalpa — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” AB „Šiaulių energija“ patalpų įrašai.

- **Model:** `datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa`[^manifest]
- **Dataset:** [datasets/gov/asmlis/skaitikliai/patalpos](../patalpos.md) (`datasets/gov/asmlis/skaitikliai/patalpos`)
- **Manifest CSV:** [datasets/gov/asmlis/skaitikliu_parodymai.csv#L60](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L60)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa`
- **Primary Key (`ref`):** `patalpos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikatorius | — |
| `patalpos_plotas` | `number` | — | `4` | `open` | — | Patalpos plotas | — |
| `patalpos_turis` | `number` | — | `4` | `open` | — | Patalpos tūris | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos platumos koordinatė wgs | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos ilgumos koordinatė wgs | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinatės wgs | — |
| `koord_adreso_tipas` | `string` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinačių tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv
