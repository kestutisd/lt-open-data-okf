---
type: Table
title: "PranesimoTipas — Įgaliojimų registrui teikiamų pranešimų klasifikatorius"
description: "Spinta table datasets/gov/rc/ir/kiti_klasifikatoriai/PranesimoTipas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/kiti_klasifikatoriai/PranesimoTipas"
tags: [gov, rc, pranesimotipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2168/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/kiti_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PranesimoTipas — Įgaliojimų registrui teikiamų pranešimų klasifikatorius

- **Model:** `datasets/gov/rc/ir/kiti_klasifikatoriai/PranesimoTipas`[^manifest]
- **Dataset:** [Kiti Įgaliojimų registro (ĮR) klasifikatoriai](../kiti_klasifikatoriai.md) (`datasets/gov/rc/ir/kiti_klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/kiti_klasifikatoriai/PranesimoTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Pranešimo tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pranešimo tipo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/kiti_klasifikatoriai.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/kiti_klasifikatoriai (https://data.gov.lt/datasets/2168/)
