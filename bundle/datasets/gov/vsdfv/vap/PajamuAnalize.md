---
type: Table
title: "PajamuAnalize"
description: "Spinta table datasets/gov/vsdfv/vap/PajamuAnalize (6 columns)."
tags: [gov, vsdfv, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L25"
    last_modified: "2026-11-11T14:39:20Z"
---

# PajamuAnalize

- **Model:** `datasets/gov/vsdfv/vap/PajamuAnalize`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/vap](../vap.md) (`datasets/gov/vsdfv/vap`)
- **Manifest CSV:** [datasets/gov/vsdfv/vap.csv#L25](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L25)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `metai, menuo`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `amzius` | `integer` | — | `3` | `open` | — | Apdraustojo amžius (metų tikslumu) | — |
| `lytis` | `string` | — | `4` | `open` | — | Apdraustojo lytis | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[pavadinimas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `2` | `open` | — | Savivaldybė | — |
| `menesio_pajamos` | `number` | — | `3` | `open` | — | Apdraustojo mėnesio pajamos, Eur | Asmenų, dirbusių pilnų mėn. pajamos, nuo kurių buvo priskaičiuotos valstybinio socialinio draudimo įmokos per ataskaitinį laikotarpį. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `menesio_pajamos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv
