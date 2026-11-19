---
type: Table
title: "SutartiesTipas — Sutarčių registro sutarčių tipų archyvinis klasifikatorius"
description: "Spinta table datasets/gov/rc/sr/klasifikatoriai/SutartiesTipas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/sr/klasifikatoriai/SutartiesTipas"
tags: [gov, rc, sutartiestipas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/klasifikatoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/sr/klasifikatoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2133/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/sr/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SutartiesTipas — Sutarčių registro sutarčių tipų archyvinis klasifikatorius

- **Model:** `datasets/gov/rc/sr/klasifikatoriai/SutartiesTipas`[^manifest]
- **Dataset:** [Reorganizuoto Sutarčių registro (SR) archyviniai duomenys](../klasifikatoriai.md) (`datasets/gov/rc/sr/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/sr/klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/klasifikatoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/sr/klasifikatoriai/SutartiesTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Sutarties tipo identifikatorius | — |
| `aprasymas` | `string` | — | `3` | `open` | — | Sutarties tipo aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/sr/klasifikatoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/klasifikatoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/sr/klasifikatoriai (https://data.gov.lt/datasets/2133/)
