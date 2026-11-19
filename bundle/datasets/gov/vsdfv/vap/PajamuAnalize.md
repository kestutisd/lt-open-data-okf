---
type: Table
title: "PajamuAnalize"
description: "Spinta table datasets/gov/vsdfv/vap/PajamuAnalize (6 columns)."
tags: [gov, vsdfv, pajamuanalize, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L25"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L25"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PajamuAnalize

- **Model:** `datasets/gov/vsdfv/vap/PajamuAnalize`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/vap](../vap.md) (`datasets/gov/vsdfv/vap`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/vap.csv#L25](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L25)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metai, menuo`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `amzius` | `integer` | — | `3` | `open` | — | Apdraustojo amžius (metų tikslumu) | — |
| `lytis` | `string` | — | `4` | `open` | — | Apdraustojo lytis | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=2` scalar) | `2` | `open` | — | Savivaldybė | — |
| `menesio_pajamos` | `number` | — | `3` | `open` | — | Apdraustojo mėnesio pajamos, Eur | Asmenų, dirbusių pilnų mėn. pajamos, nuo kurių buvo priskaičiuotos valstybinio socialinio draudimo įmokos per ataskaitinį laikotarpį. |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `menesio_pajamos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L25 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L25)
