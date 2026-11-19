---
type: Table
title: "Draudejai"
description: "Spinta table datasets/gov/vsdfv/ds/Draudejai (5 columns)."
tags: [gov, vsdfv, draudejai, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Draudejai

- **Model:** `datasets/gov/vsdfv/ds/Draudejai`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/ds](../ds.md) (`datasets/gov/vsdfv/ds`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/ds.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `draudeju_grupe, draudeju_tipas`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | — |
| `draudeju_grupe` | `string` | — | `3` | `open` | — | Draudėjų grupė | — |
| `draudeju_tipas` | `string` | — | `3` | `open` | — | Draudėjų tipas | — |
| `draudeju_sk` | `integer` | — | `4` | `open` | — | Draudėjų skaičius | Draudėjų – visų juridinių asmenų bei jų filialų ir atstovybių, taip pat fizinių asmenų, kurie įstatymų nustatyta tvarka privalo mokėti valstybinio socialinio draudimo įmokas, skaičius per ataskaitinių metų ketvirčius. |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L6)
