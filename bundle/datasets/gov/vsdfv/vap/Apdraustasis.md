---
type: Table
title: "Apdraustasis"
description: "Spinta table datasets/gov/vsdfv/vap/Apdraustasis (10 columns)."
tags: [gov, vsdfv, apdraustasis, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apdraustasis

- **Model:** `datasets/gov/vsdfv/vap/Apdraustasis`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/vap](../vap.md) (`datasets/gov/vsdfv/vap`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/vap.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metu_menuo, darbo_uzmok_eur`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agregavimas` | `string` | — | `3` | `open` | — | Agregavimo lygmuo | — |
| `metu_menuo` | `date` | `1M` | `2` | `open` | — | Metų mėnuo | — |
| `apdraustuju_rusis` | `string` | — | `3` | `open` | — | Apdraustųjų rūšis | — |
| `draudejo_grupe` | `ref` | [Draudejai](../ds/Draudejai.md) (`level=4 UUID` via `Draudejai[draudeju_grupe]`: `draudejo_grupe._id`) | `4` | `open` | — | Draudėjo grupė | — |
| `draudejo_tipas` | `ref` | [Draudejai](../ds/Draudejai.md) (`level=4 UUID` via `Draudejai[draudeju_tipas]`: `draudejo_tipas._id`) | `4` | `open` | — | Draudėjo tipas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=2` scalar) | `2` | `open` | — | Savivaldybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `darbo_uzmok_eur` | `number` | — | `2` | `open` | — | Darbo užmokestis, Eur | — |
| `apdr_asm_sk` | `integer` | — | `4` | `open` | — | Apdraustųjų asmenų skaičius | Apdraustieji fiziniai asmenys kurie valstybinio socialinio draudimo įmokas moka patys arba už juos šias įmokas moka draudėjai |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `draudejo_grupe` | `update(property: "draudejo_grupe.draudeju_grupe", type: "")` | `type` | `4` | — | — | — | — |
| `draudejo_tipas` | `update(property: "draudejo_tipas.draudeju_tipas", type: "")` | `type` | `4` | — | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `darbo_uzmok_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L5)
