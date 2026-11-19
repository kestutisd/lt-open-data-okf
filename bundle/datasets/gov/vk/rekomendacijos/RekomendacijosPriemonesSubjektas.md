---
type: Table
title: "RekomendacijosPriemonesSubjektas — Valstybinio audito rekomendacijų įgyvendinimas"
description: "Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/RekomendacijosPriemonesSubjektas"
tags: [gov, vk, rekomendacijospriemonessubjektas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1696/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/rekomendacijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# RekomendacijosPriemonesSubjektas — Valstybinio audito rekomendacijų įgyvendinimas

Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai[^manifest]

- **Model:** `datasets/gov/vk/rekomendacijos/RekomendacijosPriemonesSubjektas`[^manifest]
- **Dataset:** [Valstybinio audito rekomendacijų įgyvendinimas](../rekomendacijos.md) (`datasets/gov/vk/rekomendacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/rekomendacijos.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/RekomendacijosPriemonesSubjektas` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rekomendacijos_priemone` | `ref` | [RekomendacijosPriemone](RekomendacijosPriemone.md) (`level=4 UUID`: `rekomendacijos_priemone._id`) | `4` | `open` | — | Priemonės ID | Priemonės kodas |
| `subjekto_pavadinimas` | `string` | — | `3` | `open` | — | Subjekto pavadinimas | Subjekto, kuris įgyvendina priemonę, pavadinimas |
| `subjekto_kodas` | `string` | — | `3` | `open` | — | Subjekto kodas | Subjekto, kuris įgyvendina priemonę, kodas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/rekomendacijos (https://data.gov.lt/datasets/1696/)
