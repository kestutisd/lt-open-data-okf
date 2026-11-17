---
type: Table
title: "Skundas — VVTAT ištirtų skundų rezultatai"
description: "Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai/Skundas"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/skundu_rezultatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Skundas — VVTAT ištirtų skundų rezultatai

Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus.

- **Model:** `datasets/gov/vvtat/skundu_rezultatai/Skundas`[^manifest]
- **Dataset:** [VVTAT ištirtų skundų rezultatai](../skundu_rezultatai.md) (`datasets/gov/vvtat/skundu_rezultatai`)
- **Manifest CSV:** [datasets/gov/vvtat/skundu_rezultatai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai/Skundas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Skundo registracijos VVTAT data | — |
| `issprendimas` | `date` | `D` | `4` | `open` | — | Skundo išsprendimo data | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės juridinio asmens kodas | — |
| `imone` | `string` | — | `2` | `open` | — | Įmonės pavadinimas | — |
| `skundo_priezastis` | `string` | — | `4` | `open` | — | Skundo teikimo priežastis | — |
| `ar_pagristas` | `boolean` | — | `4` | `open` | — | Žyma, ar skundas yra pagrįstas | — |
| `nenustatymo_priezastis` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios VVTAT nenustatė skundo | — |
| `nepagristumo_priezastis` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios VVTAT skundo nelaiko pagrįstu | — |
| `rezultatas` | `string` | — | `4` | `open` | — | Ištirto skundo rezultatas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `skundo_priezastis` | `"update(property: ""skundo_priezastis[]"", type: ""array"", source: ""Skundo_priezastis"")"` | `property` | `4` | — | — | — | — |
| `nepagristumo_priezastis` | `"update(property: ""nepagristumo_priezastis[]"", type: ""array"", source: ""Nepagristumo_priezastis"")"` | `property` | `4` | — | — | — | — |
| `rezultatas` | `"update(property: ""rezultatas[]"", type: ""array"", source: ""Rezultatas"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/skundu_rezultatai.csv
