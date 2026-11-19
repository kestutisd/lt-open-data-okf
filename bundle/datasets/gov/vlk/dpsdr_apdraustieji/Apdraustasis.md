---
type: Table
title: "Apdraustasis — Apdraustųjų skaičius"
description: "Spinta table datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis"
tags: [gov, vlk, apdraustasis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1591/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/dpsdr_apdraustieji"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Apdraustasis — Apdraustųjų skaičius

- **Model:** `datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis`[^manifest]
- **Dataset:** [Apdraustųjų skaičius, pagal DPSDR nustatytas draudimo grupes](../dpsdr_apdraustieji.md) (`datasets/gov/vlk/dpsdr_apdraustieji`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/dpsdr_apdraustieji.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji/Apdraustasis` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `M` | `4` | `open` | — | Laikotarpis | Laikotarpis mėnesio tikslumu |
| `asm_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `pagrindas` | `ref` | [Pagrindas](Pagrindas.md) (`level=4 UUID`: `pagrindas._id`) | `4` | `open` | — | Nuoroda į Pagrindas | Įregistravimo pagrindo unikalus numeris |
| `skaicius` | `number` | `U` | `4` | `open` | — | Apdraustųjų skaičius | Apdraustųjų skaičius (paskutinės mėnesio dienos duomenimis) |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asm_lytis` | `"Vyras"` | — | — | — | — |
| `asm_lytis` | `"Moteris"` | — | — | — | — |
| `asm_lytis` | `"Nenurodyta"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/dpsdr_apdraustieji (https://data.gov.lt/datasets/1591/)
