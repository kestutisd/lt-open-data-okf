---
type: Table
title: "TyrimoRezultatas — Tyrimų rezultatai"
description: "Spinta table datasets/gov/aaa/integruotas_monitoringas/TyrimoRezultatas (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/TyrimoRezultatas"
tags: [gov, aaa, tyrimorezultatas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# TyrimoRezultatas — Tyrimų rezultatai

- **Model:** `datasets/gov/aaa/integruotas_monitoringas/TyrimoRezultatas`[^manifest]
- **Dataset:** [Integruoto monitoringo duomenys](../integruotas_monitoringas.md) (`datasets/gov/aaa/integruotas_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/TyrimoRezultatas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `trz_id` | `string` | — | `4` | `open` | — | Tyrimų rezultato id | — |
| `trz_neapibr` | `number` | — | `3` | `open` | — | Parametras, apibrėžiantis tyrimo rezultato tikslumą | — |
| `trz_rez_skaitinis` | `number` | — | `3` | `open` | — | Skaitinis tyrimo rezultatas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas (https://data.gov.lt/datasets/1792/)
