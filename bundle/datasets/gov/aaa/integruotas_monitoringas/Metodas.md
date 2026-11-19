---
type: Table
title: "Metodas — Metodai"
description: "Spinta table datasets/gov/aaa/integruotas_monitoringas/Metodas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/Metodas"
tags: [gov, aaa, metodas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L35"
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L35"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Metodas — Metodai

- **Model:** `datasets/gov/aaa/integruotas_monitoringas/Metodas`[^manifest]
- **Dataset:** [Integruoto monitoringo duomenys](../integruotas_monitoringas.md) (`datasets/gov/aaa/integruotas_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L35)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/Metodas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mtd_id` | `string` | — | `4` | `open` | — | Metodo id | — |
| `mtd_standartas` | `string` | — | `2` | `open` | — | Standartas, reglamentuojantis tyrimo atlikimą. | — |
| `mtd_metodo_principas` | `string` | — | `2` | `open` | — | Principo, kuriuo pagrįstas metodas, įvardinimas | — |
| `mtd_aprasymas` | `string` | — | `2` | `open` | — | Tyrimo atlikimo metodo aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L35 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L35)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas (https://data.gov.lt/datasets/1792/)
