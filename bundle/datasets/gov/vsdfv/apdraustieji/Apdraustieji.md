---
type: Table
title: "Apdraustieji"
description: "Spinta table datasets/gov/vsdfv/apdraustieji/Apdraustieji (12 columns)."
tags: [gov, vsdfv, apdraustieji, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/apdraustieji.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/apdraustieji.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apdraustieji

- **Model:** `datasets/gov/vsdfv/apdraustieji/Apdraustieji`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/apdraustieji](../apdraustieji.md) (`datasets/gov/vsdfv/apdraustieji`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/apdraustieji.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/apdraustieji.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `apdr_kateg_grupe, apdr_kateg_rusis`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | — |
| `apdr_kateg_grupe` | `string` | — | `3` | `open` | — | Apdraustųjų kategorijos grupė | — |
| `apdr_kateg_rusis` | `string` | — | `3` | `open` | — | Apdraustųjų kategorijos rūšis | — |
| `apdr_kateg_porusis` | `string` | — | `3` | `open` | — | Apdraustųjų kategorijos porūšis | — |
| `apdr_kateg_tipas` | `string` | — | `3` | `open` | — | Apdraustųjų kategorijos tipas | — |
| `draudejo_grupe` | `ref` | [Draudejai](../ds/Draudejai.md) (`level=4 UUID` via `Draudejai[draudeju_grupe]`: `draudejo_grupe._id`) | `4` | `open` | — | Draudėjo grupė | — |
| `draudejo_tipas` | `ref` | [Draudejai](../ds/Draudejai.md) (`level=4 UUID` via `Draudejai[draudeju_tipas]`: `draudejo_tipas._id`) | `4` | `open` | — | Draudėjo tipas | — |
| `prisk_suma_eur` | `number` | — | `2` | `open` | — | Priskaičiuota VSD ir PSD įmokų suma, Eur | — |
| `sumoketa_eur` | `number` | — | `2` | `open` | — | Sumokėta VSD ir PSD įmokų suma, Eur | — |
| `vid_a_darbo_apmok_suma_eur` | `number` | — | `2` | `open` | — | Vidutinė darbo apmokėjimo suma, Eur | — |
| `vid_b_apdraustuju_sk` | `number` | — | `4` | `open` | — | Vidutinis apdraustųjų skaičius | Apdraustieji – fiziniai asmenys kurie valstybinio socialinio draudimo įmokas moka patys arba už juos šias įmokas moka draudėjai |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `draudejo_grupe` | `update(property: "draudejo_grupe.draudeju_grupe", type: "")` | `type` | `4` | — | — | — | — |
| `draudejo_tipas` | `update(property: "draudejo_tipas.draudeju_tipas", type: "")` | `type` | `4` | — | — | — | — |
| `prisk_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sumoketa_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_a_darbo_apmok_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/apdraustieji.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/apdraustieji.csv#L6)
