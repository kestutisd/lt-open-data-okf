---
type: Table
title: "ParametrasVienetas — Parametrai, vienetai"
description: "Spinta table datasets/gov/aaa/integruotas_monitoringas/ParametrasVienetas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/ParametrasVienetas"
tags: [gov, aaa, parametrasvienetas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ParametrasVienetas — Parametrai, vienetai

- **Model:** `datasets/gov/aaa/integruotas_monitoringas/ParametrasVienetas`[^manifest]
- **Dataset:** [Integruoto monitoringo duomenys](../integruotas_monitoringas.md) (`datasets/gov/aaa/integruotas_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/ParametrasVienetas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ptm_kodas` | `string` | — | `2` | `open` | — | Parametro kodas (gali būti sutrumpintas parametro pavadinimas) | — |
| `ptm_pavad` | `string` | — | `2` | `open` | — | Parametro pavadinimas | — |
| `mvn_kodas` | `string` | — | `2` | `open` | — | Matavimo vieneto kodas | — |
| `mvn_pavad` | `string` | — | `2` | `open` | — | Matavimo vieneto pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas (https://data.gov.lt/datasets/1792/)
