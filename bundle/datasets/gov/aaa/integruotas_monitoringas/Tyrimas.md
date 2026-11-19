---
type: Table
title: "Tyrimas — Tyrimai"
description: "Spinta table datasets/gov/aaa/integruotas_monitoringas/Tyrimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/Tyrimas"
tags: [gov, aaa, tyrimas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Tyrimas — Tyrimai

- **Model:** `datasets/gov/aaa/integruotas_monitoringas/Tyrimas`[^manifest]
- **Dataset:** [Integruoto monitoringo duomenys](../integruotas_monitoringas.md) (`datasets/gov/aaa/integruotas_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas/Tyrimas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tad_id` | `string` | — | `4` | `open` | — | Tyrimo id | — |
| `tad_laikotarpis_nuo` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis nuo | — |
| `tad_laikotarpis_iki` | `date` | `D` | `4` | `open` | — | Tyrimo laikotarpis iki | — |
| `tad_gis_taskas` | `geometry(point, 3346)` | — | `3` | `open` | — | Tyrimo vieta | — |
| `vkl_pavad` | `string` | — | `3` | `open` | — | Veiklos pavadinimas | — |
| `ttr_pavad` | `string` | — | `4` | `open` | — | Tyrimų terpės pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ttr_pavad` | `"Aplinkos oras"` | — | — | Aplinkos oras | — |
| `ttr_pavad` | `"Biota"` | — | — | Biota | — |
| `ttr_pavad` | `"Paviršinis vanduo"` | — | — | Paviršinis vanduo | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas (https://data.gov.lt/datasets/1792/)
