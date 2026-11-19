---
type: Table
title: "SandorioTipas — Hr sandorių tipų archyvinis klasifikatorius"
description: "Spinta table datasets/gov/rc/hr/tipu_klasifikatoriai/SandorioTipas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/tipu_klasifikatoriai/SandorioTipas"
tags: [gov, rc, sandoriotipas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2131/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/hr/tipu_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SandorioTipas — Hr sandorių tipų archyvinis klasifikatorius

- **Model:** `datasets/gov/rc/hr/tipu_klasifikatoriai/SandorioTipas`[^manifest]
- **Dataset:** [Likviduoto Lietuvos Respublikos HR archyviniai klasifikatoriai](../tipu_klasifikatoriai.md) (`datasets/gov/rc/hr/tipu_klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/tipu_klasifikatoriai/SandorioTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Sandorio tipo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Sandorio tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/tipu_klasifikatoriai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/hr/tipu_klasifikatoriai (https://data.gov.lt/datasets/2131/)
