---
type: Table
title: "Paslauga — Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius"
description: "Spinta table datasets/gov/rc/ir/klasifikatoriai/Paslauga (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai/Paslauga"
tags: [gov, rc, paslauga, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2167/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Paslauga — Įgaliojimų registro viešųjų ir administracinių paslaugų klasifikatorius

- **Model:** `datasets/gov/rc/ir/klasifikatoriai/Paslauga`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/ir/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/klasifikatoriai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai/Paslauga` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Paslaugos tipo identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Paslaugos tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Paslaugos tipo pavadinimas | — |
| `teikejo_kodas` | `integer` | — | `4` | `open` | — | Paslaugos teikėjo kodas | — |
| `teikejo_pavadinimas` | `string` | — | `3` | `open` | — | Paslaugos teikėjo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/klasifikatoriai (https://data.gov.lt/datasets/2167/)
