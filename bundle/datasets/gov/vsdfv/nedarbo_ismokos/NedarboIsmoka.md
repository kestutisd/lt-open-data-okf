---
type: Table
title: "NedarboIsmoka"
description: "Spinta table datasets/gov/vsdfv/nedarbo_ismokos/NedarboIsmoka (9 columns)."
tags: [gov, vsdfv, nedarboismoka, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/nedarbo_ismokos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# NedarboIsmoka

- **Model:** `datasets/gov/vsdfv/nedarbo_ismokos/NedarboIsmoka`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/nedarbo_ismokos](../nedarbo_ismokos.md) (`datasets/gov/vsdfv/nedarbo_ismokos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/nedarbo_ismokos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metu_menuo`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metu_menuo` | `date` | `1M` | `2` | `open` | — | Mėnuo | — |
| `uz_pilna_men` | `string` | — | `4` | `open` | — | Ar išmoka uš pilną mėnesį? | Išmoka mokama už visas mėnesio dienas arba nevisas |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=2` scalar) | `2` | `open` | — | Savivaldybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Amžius | — |
| `ismokos_dydis_eur` | `number` | — | `2` | `open` | — | Išmokos dydis, Eur | — |
| `gaveju_sk` | `number` | — | `4` | `open` | — | Gavėjų skaičius | — |
| `prisk_suma_eur` | `number` | — | `2` | `open` | — | Priskaičiuota suma, Eur | — |
| `mok_trukme_sum` | `number` | — | `3` | `open` | — | Mokėjimo trukmė, mėn. | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `uz_pilna_men` | `"Už nepilną mėnesį"` | — | — | Darbo išmokos už nepilną mėnesį | — |
| `uz_pilna_men` | `"Už pilną mėnesį"` | — | — | Darbo išmokos už pilną mėnesį | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | — | — | — | — |
| `ismokos_dydis_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `prisk_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/nedarbo_ismokos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L6)
