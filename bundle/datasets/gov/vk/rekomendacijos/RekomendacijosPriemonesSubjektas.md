---
type: Table
title: "RekomendacijosPriemonesSubjektas — Valstybinio audito rekomendacijų įgyvendinimas"
description: "Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/RekomendacijosPriemonesSubjektas"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# RekomendacijosPriemonesSubjektas — Valstybinio audito rekomendacijų įgyvendinimas

Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai

- **Model:** `datasets/gov/vk/rekomendacijos/RekomendacijosPriemonesSubjektas`[^manifest]
- **Dataset:** [datasets/gov/vk/rekomendacijos](../rekomendacijos.md) (`datasets/gov/vk/rekomendacijos`)
- **Manifest CSV:** [datasets/gov/vk/rekomendacijos.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/RekomendacijosPriemonesSubjektas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rekomendacijos_priemone` | `ref` | [RekomendacijosPriemone](RekomendacijosPriemone.md) | `4` | `open` | — | Priemonės ID | Priemonės kodas |
| `subjekto_pavadinimas` | `string` | — | `3` | `open` | — | Subjekto pavadinimas | Subjekto, kuris įgyvendina priemonę, pavadinimas |
| `subjekto_kodas` | `string` | — | `3` | `open` | — | Subjekto kodas | Subjekto, kuris įgyvendina priemonę, kodas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv
