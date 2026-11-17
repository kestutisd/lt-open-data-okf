---
type: Table
title: "Tikrinimas — Karšto vandens skaitiklių tikrinimo registras"
description: "Teisinei metrologijai priskirtų matavimo priemonių (karšto vandens skaitiklių) tikrinimo registras"
resource: "https://get.data.gov.lt/datasets/gov/ast/skaitikliu_tikrinimai/Tikrinimas"
tags: [gov, ast, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ast/skaitikliu_tikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/skaitikliu_tikrinimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tikrinimas — Karšto vandens skaitiklių tikrinimo registras

Teisinei metrologijai priskirtų matavimo priemonių (karšto vandens skaitiklių) tikrinimo registras

- **Model:** `datasets/gov/ast/skaitikliu_tikrinimai/Tikrinimas`[^manifest]
- **Dataset:** [Karšto vandens skaitiklių tikrinimo registras](../skaitikliu_tikrinimai.md) (`datasets/gov/ast/skaitikliu_tikrinimai`)
- **Manifest CSV:** [datasets/gov/ast/skaitikliu_tikrinimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/skaitikliu_tikrinimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/skaitikliu_tikrinimai/Tikrinimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `skaitiklio_tipas` | `string` | — | `4` | `open` | — | Karšto vandens skaitiklio tipas | — |
| `buto_adresas_lt` | `string` | — | `4` | `open` | — | Objekto adresas, kuriame bus vykdoma skaitiklio patikra | — |
| `skaitiklio_nr` | `string` | — | `4` | `open` | — | Šifruotas tikrinamo skaitiklio numeris | — |
| `ar_patikrinta` | `boolean` | — | `4` | `open` | — | Požymis ar skaitiklis patikrintas | — |
| `metrologijos_centras` | `string` | — | `4` | `open` | — | Lietuvos Metrologijos inspekcijos padalinys, kuriam priklauso objektas | — |
| `skaitiklio_patikros_data` | `date` | `D` | `4` | `open` | — | Skaitiklio tikrinimo data | — |
| `skaitiklio_patikros_metai` | `integer` | `yr` | `4` | `open` | — | Skaitiklio tikrinimo metai | — |
| `teisinis_pagrindas` | `string` | — | `4` | `open` | — | Tikrinimo teisinis pagrindas | — |
| `sekancios_patikros_data` | `date` | `D` | `4` | `open` | — | Numatoma sekančio skaitiklio patikrinimo data | — |
| `sekancios_patikros_metai` | `integer` | `yr` | `4` | `open` | — | Numatoma sekančio skaitiklio patikrinimo metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `buto_adresas_lt` | `update(property: "buto_adresas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/skaitikliu_tikrinimai.csv
