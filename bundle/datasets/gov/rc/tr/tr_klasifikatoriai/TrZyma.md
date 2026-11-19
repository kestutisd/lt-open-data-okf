---
type: Table
title: "TrZyma — Testamentų registro testamentų žymų klasifikatorius"
description: "Spinta table datasets/gov/rc/tr/tr_klasifikatoriai/TrZyma (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai/TrZyma"
tags: [gov, rc, trzyma, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/tr_klasifikatoriai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2158/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/tr/tr_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TrZyma — Testamentų registro testamentų žymų klasifikatorius

- **Model:** `datasets/gov/rc/tr/tr_klasifikatoriai/TrZyma`[^manifest]
- **Dataset:** [Testamentų registro (TR) klasifikatoriai](../tr_klasifikatoriai.md) (`datasets/gov/rc/tr/tr_klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/tr/tr_klasifikatoriai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/tr_klasifikatoriai/TrZyma` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `tipas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipas` | `integer` | — | `4` | `open` | — | Žymos tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Žymos tipo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/tr_klasifikatoriai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/tr_klasifikatoriai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/tr/tr_klasifikatoriai (https://data.gov.lt/datasets/2158/)
