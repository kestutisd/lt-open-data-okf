---
type: Table
title: "ChemNaudotojai — Asmenys"
description: "Spinta table datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/chemijos_naudotojai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemijos_naudotojai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ChemNaudotojai — Asmenys

- **Model:** `datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai`[^manifest]
- **Dataset:** [datasets/gov/aaa/chemijos_naudotojai](../chemijos_naudotojai.md) (`datasets/gov/aaa/chemijos_naudotojai`)
- **Manifest CSV:** [datasets/gov/aaa/chemijos_naudotojai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemijos_naudotojai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `metai` | `integer` | — | `4` | `open` | — | Dokumento (ataskaitos) atsiskaitymo metai | Nuo 2017 m. |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `create(property: "imone", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |
| `jar_kodas` | `update(property: "imone.ja_kodas", type: "")` | `property` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/chemijos_naudotojai.csv
