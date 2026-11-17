---
type: Table
title: "Paslauga — Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius"
description: "Spinta table datasets/gov/rc/ir/klasifikatoriai/Paslauga (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai/Paslauga"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga — Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius

- **Model:** `datasets/gov/rc/ir/klasifikatoriai/Paslauga`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/ir/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/rc/ir/klasifikatoriai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai/Paslauga`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Paslaugos tipo identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Paslaugos tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Paslaugos tipo pavadinimas | — |
| `teikejo_kodas` | `integer` | — | `4` | `open` | — | Paslaugos teikėjo kodas | — |
| `teikejo_pavadinimas` | `string` | — | `3` | `open` | — | Paslaugos teikėjo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv
