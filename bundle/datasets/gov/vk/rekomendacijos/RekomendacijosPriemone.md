---
type: Table
title: "RekomendacijosPriemone — Valstybinio audito rekomendacijų įgyvendinimas"
description: "Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/RekomendacijosPriemone"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# RekomendacijosPriemone — Valstybinio audito rekomendacijų įgyvendinimas

Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai

- **Model:** `datasets/gov/vk/rekomendacijos/RekomendacijosPriemone`[^manifest]
- **Dataset:** [datasets/gov/vk/rekomendacijos](../rekomendacijos.md) (`datasets/gov/vk/rekomendacijos`)
- **Manifest CSV:** [datasets/gov/vk/rekomendacijos.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/RekomendacijosPriemone`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priemonesid` | `integer` | — | `3` | `open` | — | Priemonės ID | Priemonės kodas |
| `rekomendacija` | `ref` | [Rekomendacija](Rekomendacija.md) | `4` | `open` | — | Rekomendacijos ID | Rekomendacijos kodas |
| `priemone` | `string` | — | `3` | `open` | — | Priemonės turinys | Priemonės turinys |
| `rezultatas` | `string` | — | `3` | `open` | — | Priemonės rezultatas | Priemonės rezultatas |
| `igyvendinimo_bukle` | `string` | — | `3` | `open` | — | įgyvendinimo būklė | Priemonės įgyvendinimo būklė |
| `igyvendinimo_data` | `date` | `D` | `4` | `open` | — | įgyvendinimo data | Priemonės įgyvendinimo data |
| `laiko_bukle` | `string` | — | `3` | `open` | — | Laiko būklė | Priemonės įgyvendinimo laiko būklė |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv
