---
type: Table
title: "PaskatinimasApdovanojimas — Valstybės kontrolės darbuotojų paskatinimai ir apdovanojimai"
description: "Valstybės kontrolės darbuotojų paskatinimo ir apdovanojimo duomenys ketvirčiais"
resource: "https://get.data.gov.lt/datasets/gov/vk/apdovanojimai/PaskatinimasApdovanojimas"
tags: [gov, vk, paskatinimasapdovanojimas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/apdovanojimai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vk/apdovanojimai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1695/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/apdovanojimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PaskatinimasApdovanojimas — Valstybės kontrolės darbuotojų paskatinimai ir apdovanojimai

Valstybės kontrolės darbuotojų paskatinimo ir apdovanojimo duomenys ketvirčiais[^manifest]

- **Model:** `datasets/gov/vk/apdovanojimai/PaskatinimasApdovanojimas`[^manifest]
- **Dataset:** [Valstybės kontrolės darbuotojų paskatinimai ir apdovanojimai](../apdovanojimai.md) (`datasets/gov/vk/apdovanojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/apdovanojimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/apdovanojimai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/apdovanojimai/PaskatinimasApdovanojimas` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/apdovanojimai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/apdovanojimai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/apdovanojimai (https://data.gov.lt/datasets/1695/)
