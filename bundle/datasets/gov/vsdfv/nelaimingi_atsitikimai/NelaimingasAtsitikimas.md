---
type: Table
title: "NelaimingasAtsitikimas"
description: "Spinta table datasets/gov/vsdfv/nelaimingi_atsitikimai/NelaimingasAtsitikimas (11 columns)."
tags: [gov, vsdfv, nelaimingasatsitikimas, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# NelaimingasAtsitikimas

- **Model:** `datasets/gov/vsdfv/nelaimingi_atsitikimai/NelaimingasAtsitikimas`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/nelaimingi_atsitikimai](../nelaimingi_atsitikimai.md) (`datasets/gov/vsdfv/nelaimingi_atsitikimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pasalpos_rusis, pasalpos_priezastis`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metu_menuo` | `date` | `1M` | `2` | `open` | — | Metų mėnuo | — |
| `pasalpos_rusis` | `string` | — | `3` | `open` | — | Pašalpos rūšis | — |
| `pasalpos_priezastis` | `string` | — | `3` | `open` | — | Pašalpos priežastis | — |
| `net_darb_lygis` | `string` | — | `3` | `open` | — | Netekto darbingumo lygis | — |
| `net_darb_tipas` | `string` | — | `3` | `open` | — | Netekto darbingumo tipas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=2` scalar) | `2` | `open` | — | Savivaldybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `gaveju_sk` | `number` | — | `4` | `open` | — | Gavėjų skaičius | — |
| `prisk_suma_eur` | `number` | — | `2` | `open` | — | Priskaičiuota suma, Eur | — |
| `ismoku_sk` | `number` | — | `4` | `open` | — | Išmokų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `prisk_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nelaimingi_atsitikimai.csv#L6)
