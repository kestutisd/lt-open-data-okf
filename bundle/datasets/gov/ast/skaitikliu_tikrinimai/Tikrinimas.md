---
type: Table
title: "Tikrinimas — Karšto vandens skaitiklių tikrinimo registras"
description: "Teisinei metrologijai priskirtų matavimo priemonių (karšto vandens skaitiklių) tikrinimo registras"
resource: "https://get.data.gov.lt/datasets/gov/ast/skaitikliu_tikrinimai/Tikrinimas"
tags: [gov, ast, tikrinimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/skaitikliu_tikrinimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/ast/skaitikliu_tikrinimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2769/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ast/skaitikliu_tikrinimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Tikrinimas — Karšto vandens skaitiklių tikrinimo registras

Teisinei metrologijai priskirtų matavimo priemonių (karšto vandens skaitiklių) tikrinimo registras[^manifest]

- **Model:** `datasets/gov/ast/skaitikliu_tikrinimai/Tikrinimas`[^manifest]
- **Dataset:** [Karšto vandens skaitiklių tikrinimo registras](../skaitikliu_tikrinimai.md) (`datasets/gov/ast/skaitikliu_tikrinimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ast/skaitikliu_tikrinimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/skaitikliu_tikrinimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/skaitikliu_tikrinimai/Tikrinimas` (`deployed`)[^manifest]
- **Provider:** `ast` — Alytaus šilumos tinklai *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/skaitikliu_tikrinimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/skaitikliu_tikrinimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ast/skaitikliu_tikrinimai (https://data.gov.lt/datasets/2769/)
