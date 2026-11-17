---
type: Table
title: "PagrindiniaiDuomenys — Įgaliojimų registro pagrindiniai duomenys"
description: "Spinta table datasets/gov/rc/ir/pagrindiniai_duomenys/PagrindiniaiDuomenys (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/pagrindiniai_duomenys/PagrindiniaiDuomenys"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/pagrindiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/pagrindiniai_duomenys.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# PagrindiniaiDuomenys — Įgaliojimų registro pagrindiniai duomenys

- **Model:** `datasets/gov/rc/ir/pagrindiniai_duomenys/PagrindiniaiDuomenys`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) pagrindiniai duomenys​](../pagrindiniai_duomenys.md) (`datasets/gov/rc/ir/pagrindiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/rc/ir/pagrindiniai_duomenys.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/pagrindiniai_duomenys.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/pagrindiniai_duomenys/PagrindiniaiDuomenys`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais užregistruotas įgaliojimas | — |
| `ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis, kurį užregistruotas įgaliojimas | — |
| `kas_patvirtino` | `string` | — | `3` | `open` | — | Įgaliojimą patvirtinusio asmens tipas | — |
| `igaliojimo_tipas` | `string` | — | `3` | `open` | — | Įgaliojimo tipo pavadinimas | — |
| `igaliojimu_kiekis` | `string` | — | `3` | `open` | — | Įgaliojimų kiekis per ketvirtį | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/pagrindiniai_duomenys.csv
