---
type: Table
title: "KenkejoGrupe"
description: "Spinta table datasets/gov/miskai/sanitarine/KenkejoGrupe (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoGrupe"
tags: [gov, miskai, kenkejogrupe, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/827/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KenkejoGrupe

- **Model:** `datasets/gov/miskai/sanitarine/KenkejoGrupe`[^manifest]
- **Dataset:** [Miškų sanitarinė būklė](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/KenkejoGrupe` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Kenkėjo grupės pavadinimas | — |
| `kodas` | `string` | — | `3` | `open` | — | Kenkėjo grupės kodas | — |
| `vieta` | `ref` | [Vieta](Vieta.md) (`level=4 UUID`: `vieta._id`) | `4` | `open` | — | Vieta (medelynas ar miškas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine (https://data.gov.lt/datasets/827/)
