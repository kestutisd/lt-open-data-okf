---
type: Table
title: "PaskatinimasApdovanojimas — Valstybės kontrolės darbuotojų paskatinimai ir apdovanojimai"
description: "Valstybės kontrolės darbuotojų paskatinimo ir apdovanojimo duomenys ketvirčiais"
resource: "https://get.data.gov.lt/datasets/gov/vk/apdovanojimai/PaskatinimasApdovanojimas"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/apdovanojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/apdovanojimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaskatinimasApdovanojimas — Valstybės kontrolės darbuotojų paskatinimai ir apdovanojimai

Valstybės kontrolės darbuotojų paskatinimo ir apdovanojimo duomenys ketvirčiais

- **Model:** `datasets/gov/vk/apdovanojimai/PaskatinimasApdovanojimas`[^manifest]
- **Dataset:** [datasets/gov/vk/apdovanojimai](../apdovanojimai.md) (`datasets/gov/vk/apdovanojimai`)
- **Manifest CSV:** [datasets/gov/vk/apdovanojimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/apdovanojimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/apdovanojimai/PaskatinimasApdovanojimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `integer` | — | `2` | `open` | — | Metai | Metai |
| `ataskaitinis_ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | Ketvirtis |
| `tipas` | `string` | — | `3` | `open` | — | Tipas | Paskatinimo ar apdovanojimo tipas |
| `priezastis` | `string` | — | `3` | `open` | — | Priežastis | Paskatinimo ar apdovanojimo priežastis |
| `darbuotoju_skaicius` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius | Darbuotojų skaičius, kuriems skirtas paskatinimas ar apdovanojimas |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/apdovanojimai.csv
