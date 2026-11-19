---
type: Table
title: "KenkejoPogrupis"
description: "Spinta table datasets/gov/miskai/sanitarine/KenkejoPogrupis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoPogrupis"
tags: [gov, miskai, kenkejopogrupis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/827/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KenkejoPogrupis

- **Model:** `datasets/gov/miskai/sanitarine/KenkejoPogrupis`[^manifest]
- **Dataset:** [Miškų sanitarinė būklė](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoPogrupis` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupe` | `ref` | [KenkejoGrupe](KenkejoGrupe.md) (`level=4 UUID`: `grupe._id`) | `4` | `open` | — | Susijusi kenkėjo grupė | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Kenkėjo pogrupio pavadinimas | — |
| `kodas` | `string` | — | `3` | `open` | — | Kenkėjo pogrupio kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine (https://data.gov.lt/datasets/827/)
