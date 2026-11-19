---
type: Table
title: "Terminas — Įgaliojimų registro terminų klasifikatorius"
description: "Spinta table datasets/gov/rc/ir/klasifikatoriai/Terminas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai/Terminas"
tags: [gov, rc, terminas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2167/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Terminas — Įgaliojimų registro terminų klasifikatorius

- **Model:** `datasets/gov/rc/ir/klasifikatoriai/Terminas`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) įgaliojimų rūšių, terminų ir paslaugų klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/ir/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/klasifikatoriai/Terminas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Įgaliojimo termino kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Įgaliojimo termino pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/klasifikatoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/klasifikatoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/klasifikatoriai (https://data.gov.lt/datasets/2167/)
