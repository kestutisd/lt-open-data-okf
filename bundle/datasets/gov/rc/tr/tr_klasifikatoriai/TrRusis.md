---
type: Table
title: "TrRusis — Testamentų registro testamentų rūšių klasifikatorius"
description: "Spinta table datasets/gov/rc/tr/tr_klasifikatoriai/TrRusis (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai/TrRusis"
tags: [gov, rc, trrusis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/tr_klasifikatoriai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2158/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/tr/tr_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TrRusis — Testamentų registro testamentų rūšių klasifikatorius

- **Model:** `datasets/gov/rc/tr/tr_klasifikatoriai/TrRusis`[^manifest]
- **Dataset:** [Testamentų registro (TR) klasifikatoriai](../tr_klasifikatoriai.md) (`datasets/gov/rc/tr/tr_klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/tr/tr_klasifikatoriai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai/TrRusis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Testamento rūšies identifikatorius | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Testamento rūšies pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/tr_klasifikatoriai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/tr/tr_klasifikatoriai (https://data.gov.lt/datasets/2158/)
